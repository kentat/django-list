from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Person

# Register your models here.
class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        #exclude = ('id') 

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'address',)
    list_display_links = ('name',)
    resource_class = PersonResource


