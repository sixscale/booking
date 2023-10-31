from rest_framework import serializers

from .models import Reserve, Room

RESERVE_EXIST = 'Бронь уже существует'
ROOM_NOT_EXIST = 'Комнаты не существует'
DATE_END_ERROR = 'Невозможно забронировать на эту дату'
DATE_EQUALLY = 'Бронь доступна только на один день'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number', 'price', 'number_seats')


class ReserveSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(source='room.number')

    class Meta:
        model = Reserve
        fields = ('id', 'number', 'start_date', 'end_date')

    def validate(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        if end_date < start_date:
            raise serializers.ValidationError(DATE_END_ERROR)
        if end_date == start_date:
            raise serializers.ValidationError(DATE_EQUALLY)
        number = data['room']['number']
        try:
            room = Room.objects.get(number=number)
        except Exception:
            raise serializers.ValidationError(ROOM_NOT_EXIST)
        if (Reserve.objects.filter(room=room, start_date__lte=start_date, end_date__gte=end_date).exists()
                or Reserve.objects.filter(room=room, start_date__gte=start_date, start_date__lt=end_date).exists()
                or Reserve.objects.filter(room=room, end_date__lte=start_date, end_date__gte=end_date).exists()):
            raise serializers.ValidationError(RESERVE_EXIST)
        return super().validate(data)

    def create(self, validated_data):
        user = validated_data['user']
        number = validated_data['room']['number']
        room = Room.objects.get(number=number)
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']
        reserve = Reserve(user=user, room=room, start_date=start_date, end_date=end_date)
        reserve.save()
        return reserve
