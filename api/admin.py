from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

class VolumeInline(admin.StackedInline):
    model = Volume
    pk_name = 'light_novel'
    readonly_fields = ["image"]

    def image(self, volume):
        return mark_safe('''
                <img src='{url}' alt='{alt}' width='150px'/>
            '''.format(url=volume.illustration, alt=volume.name))

class AlternateNameInline(admin.StackedInline):
    model = AlternateName
    pk_name = 'light_novel'


class LightNovelAdmin(admin.ModelAdmin):
    inlines = (VolumeInline, AlternateNameInline, )
    search_fields = ["title"]
    filter_horizontal = ["genres", "illustrators", "publishers", "authors"]
    readonly_fields = ["image"]

    def image(self, lightnovel):
        return mark_safe('''
            <img src='{url}' alt='{alt}' width='150px'/>
        '''.format(url=lightnovel.illustration, alt=lightnovel.title))


# Register your models here.
admin.site.register(LightNovel, LightNovelAdmin)
admin.site.register(Illustrator)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)