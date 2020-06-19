from django.contrib import admin
from .models import *
from twilio.rest import Client


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'freedate', 'phone', 'callstatus']
    ordering = ['freedate']
    actions = ['sendsms']

    def sendsms(self, request, queryset):
        account_sid = 'ACc0d6a4806ca9101d81f263e84c64ef78'
        auth_token = ''
        client = Client(account_sid, auth_token)
        for c in queryset.all():
            if c.callstatus == 'n':
                message = client.messages.create(
                    body='Здравствуйте, {name}! Вы записаны на видеосессию {date}. Ждем вас.'.format(name=c.name, date=c.freedate),
                    from_='+12563644920',
                    to=c.phone
                )
                print(message.sid)
                queryset.update(callstatus='c')
            else:
                self.message_user(request, 'Этому клиенту уже отправлено уведомление')
    sendsms.short_description = "Send SMS"


admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(VacantDate)
# admin.site.register(Session, SessionAdmin)
