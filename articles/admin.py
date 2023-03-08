from django.contrib import admin

from .models import Article , Comment

class Commentİnline(admin.TabularInline):
    model=Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        Commentİnline
    ]

admin.site.register(Article,ArticleAdmin)

admin.site.register(Comment)



# Register your models here.
