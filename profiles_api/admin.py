from django.contrib import admin
from .models import StatusUpdate, UserProfile, Message, ProfileFeedItem

# Register your models here.

admin.site.register(ProfileFeedItem)
admin.site.register(UserProfile)
admin.site.register(StatusUpdate)
admin.site.register(Message)
