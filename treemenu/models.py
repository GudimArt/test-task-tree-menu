from django.db import models

class Menu(models.Model):
    name = models.CharField(null=True, max_length=255)
    def __str__(self):
        return f'{self.name}'
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE, related_name='items')
    url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'