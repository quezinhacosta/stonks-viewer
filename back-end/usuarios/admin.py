from django.contrib import admin
from .models import Transacao, MetaFinanceira, Lembrete

admin.site.register(Transacao)
admin.site.register(MetaFinanceira)
admin.site.register(Lembrete)
