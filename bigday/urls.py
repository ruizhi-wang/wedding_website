from django.conf.urls import url, include

from django.contrib import admin

admin.autodiscover()

import wedding.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    url(r'^', include('wedding.urls'))
]
