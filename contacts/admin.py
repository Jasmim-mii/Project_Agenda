from django.contrib import admin

from .models import Category_type, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'lastName', 'telephone',
                    'email', 'date_created', 'category', 'visible')
    list_display_links = ('id', 'first_name', 'lastName')
    list_per_page = 10

    search_fields = ('first_name', 'lastName', 'telephone',
                     'email', 'date_created', 'full_name')
    list_editable = ('telephone', 'visible')


admin.site.register(Category_type)
admin.site.register(Contact, ContactAdmin)
