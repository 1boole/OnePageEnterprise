from django.contrib import admin
from .models import Settings
from .models import Slider
from .models import Section1
from .models import Section2
from .models import Section3
from .models import Section4
from .models import Section5
from .models import Footer
from .models import Message

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','Name')
    list_display_links = ('id','Name')

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id','Title')
    list_display_links = ('id','Title')

class TextAdmin(admin.ModelAdmin):
    list_display=('id','Text')
    list_display_links = ('id','Text')

# Register your models here.
admin.site.register(Settings, GeneralAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Section1, GeneralAdmin)
admin.site.register(Section2, GeneralAdmin)
admin.site.register(Section3, GeneralAdmin)
admin.site.register(Section4, TextAdmin)
admin.site.register(Section5, GeneralAdmin)
admin.site.register(Footer, TextAdmin)
admin.site.register(Message, SliderAdmin)