import uuid
from django.db import models
from django.conf import settings

class AcaoSustentavel(models.Model):
    CATEGORY_CHOICES = [
        ('Reciclagem', 'Reciclagem'),
        ('Energia', 'Energia'),
        ('Água', 'Água'),
        ('Mobilidade', 'Mobilidade'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='acoes')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"Profile of {self.user.username}"
