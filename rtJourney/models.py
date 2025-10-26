from django.db import models

# This model represents one part of your learning journey
# Each record stores a topic you learned, its description, and the date.

# Create your models here.
class LearningJourney(models.Model):
    title = models.CharField(max_length=200) # Title of your learning topic
    description = models.TextField()   # Detailed explanation
    date = models.DateField(auto_now_add=True) # Automatically adds today's date

    def __str__(self):
        return self.title # Display title in the admin interface
