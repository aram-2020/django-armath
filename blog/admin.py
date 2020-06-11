from django.contrib import admin
from .models import Blog, Contact, Comment

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','message')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','price')

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","message")

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.site_header = "Armath Admins"
admin.site.site_title = "Armath Admin Portal"
admin.site.index_title = "Welcome to Armath Researcher Portal"
