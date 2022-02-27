from django.contrib import admin
from first_app.models import Topic, WebPage, AccessRecord, Users, UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(Users)
admin.site.register(UserProfileInfo)


