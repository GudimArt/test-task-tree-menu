from django import template
from django.urls import reverse

from treemenu.models import MenuItem

register = template.Library()


def build_menu_tree(menu_items, parent=None):
    tree = []
    for item in menu_items:
        if item.parent == parent:
            item_data = {
                'title': item.title,
                'url': item.url,
                'children': build_menu_tree(menu_items, item),
                'menu': item.menu
            }
            tree.append(item_data)
    return tree


def build_html(menu_tree, current_url):
    html = "<ul>"
    for item in menu_tree:
        title = item['title']
        url = item['url']
        children = item['children']

        if url == current_url:
            html += f"<li><strong>{title}</strong>"
        else:
            html += f"<li><a href='{url}'>{title}</a>"

        if current_url.startswith(url):
            html += build_html(children, current_url)
        elif children:
            # Если текущий url находится в дочерних пунктах, развернуть их
            if any(child['url'] == current_url for child in children):
                html += build_html(children, current_url)
            # Если текущий url не найден, отобразить только верхние пункты меню
            elif not current_url:
                html += build_html(children, "")

        html += "</li>"

    html += "</ul>"
    return html

def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(menu__name=menu_name)
    menu_tree = build_menu_tree(menu_items)
    html = build_html(menu_tree, current_url)
    return {'menu_html': html, 'menu_items': menu_tree, 'current_url': current_url}


@register.inclusion_tag('menu.html')
def show_menu(menu_name, current_url):
    menu = draw_menu(menu_name, current_url)
    return menu
