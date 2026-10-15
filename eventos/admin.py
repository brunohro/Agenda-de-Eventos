from django.contrib import admin
from .models import Local, Categoria, Evento, Atividade, Inscricoes, Relatorio

admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Atividade)
admin.site.register(Inscricoes)
admin.site.register(Relatorio)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'local')
    list_filter = ('local', 'categoria')
    search_fields = ('titulo', 'evento')

    

