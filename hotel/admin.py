from django.contrib import admin

from .models import Reserve, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'price', 'number_seats')
    search_fields = ('number', 'price', 'number_seats')


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'start_date', 'end_date')
    search_fields = ('room_number', 'start_date', 'end_date')

    def room_number(self, obj):
        return obj.room.number

    room_number.short_description = 'номер комнаты'
