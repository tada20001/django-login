from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),

    path('', lambda reqest: redirect("blog:post_list"), name='root'),
]
