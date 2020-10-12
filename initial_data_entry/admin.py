from django.contrib import admin
from .models import *




class InitialDataEntryAdmin(admin.ModelAdmin):
    list_display= ('army_no','name','rank','i_card_no','trade','wpn_type','regd_no','butt_no','issue_type')

class AttendanceAdmin(admin.ModelAdmin):

    list_display= ('person', 'weapon_out', 'weapon_in', 'date')    

admin.site.register(InitialDataEntry,InitialDataEntryAdmin)

admin.site.register(Attendance,AttendanceAdmin)