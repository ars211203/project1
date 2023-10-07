from django.contrib import admin
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)  # Sử dụng TextInput widget cho trường "title"

    class Meta:
        model = Post
        fields = '__all__'
class PostAdmin(admin.ModelAdmin):
    fields = ('content', 'title')
    list_display = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('title',)
admin.site.register(Post, PostAdmin)