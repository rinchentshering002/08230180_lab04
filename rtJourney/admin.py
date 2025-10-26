from django.contrib import admin
from .models import LearningJourney


# Register your models here.
@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Show these columns in the admin
    search_fields = ('title', 'description')  # Add search functionality