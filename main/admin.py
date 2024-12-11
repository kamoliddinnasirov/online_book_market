from django.contrib import admin
from main.models import Author, Book, BookInstance, Status, Language, Publisher, Genre
from django.utils.safestring import mark_safe
from django.utils.html import format_html



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", 'first_name', 'date_of_birth', 'show_photo')
    fields = ('last_name', 'first_name', ("date_of_birth", 'photo'))   

    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return format_html(f"<img src='{obj.photo.url}' style='max-height: 100px;'>")
    
    show_photo.short_description = 'Photo'




class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}' style='max-height: 100px;'>") 
    
    show_photo.short_description = 'Muqova'


# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ("book", 'status')
#     list_filter = ("book", 'status',)   






@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", )





@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", )



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )