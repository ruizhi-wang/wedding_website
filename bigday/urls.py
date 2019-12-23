from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import bigday.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", bigday.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("contact/", bigday.views.contact, name='contact'),
    path("success/", bigday.views.success, name='success')
]