from django.contrib import admin

from .models import Profile, Businesses,Message,Neighborhoods_cool

# Register your models here.
admin.site.register(Profile)
admin.site.register(Businesses)
admin.site.register(Message)
admin.site.register(Neighborhoods_cool)
