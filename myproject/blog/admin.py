from django.contrib import admin
from .models import Blogs,Authors,Comment

admin.site.register(Blogs)
admin.site.register(Authors)
admin.site.register(Comment)