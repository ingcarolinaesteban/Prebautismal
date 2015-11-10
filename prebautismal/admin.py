from django.contrib import admin
from .models import padres, bautizado
from actions import export_as_excel

class BautizadoAdmin(admin.ModelAdmin):
    list_display = ('Nombre_Bautizado','Apellidos_Bautizado','imagen_Registro_civil', 'Padres', 'Fecha_Nacimiento','Telefono','Nombre_Padrino','Apellidos_Padrino','Nombre_Madrina','Apellidos_Madrina','Registro_civil','Aprobado' )
    list_filter = ('Nombre_Bautizado','Apellidos_Bautizado')
    search_fields = ('Nombre_Bautizado','Apellidos_Bautizado','Padres__Nombre_Padre')
    list_editable = ('Aprobado',)
    actions = (export_as_excel,)
    # raw_id_fields =('Padres')


    def imagen_Registro_civil(self, obj):
        return '<img src="%s">' % obj.Registro_civil.url
   

class PadreAdmin(admin.ModelAdmin):
    list_display = ('Nombre_Padre','Apellidos_Padre','Cedula_Padre','Email_Padre','Nombre_Madre','Apellidos_Madre','Cedula_Madre','Email_Madre','Nombre_Abuelo_Paterno','Nombre_Abuela_Paterna', 'Nombre_Abuelo_Materno','Nombre_Abuela_Materna',) 


        
    # imagen_Registro_civil.allow_tags = True

admin.site.register(padres,PadreAdmin)
admin.site.register(bautizado,BautizadoAdmin)
