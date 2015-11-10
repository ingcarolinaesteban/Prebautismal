from django import forms
from django.forms.models import inlineformset_factory
from .models import padres, bautizado


class PadresForm(forms.ModelForm):
    class Meta:
        model = padres
        fields = ('Nombre_Padre','Apellidos_Padre','Cedula_Padre','Email_Padre','Nombre_Abuelo_Paterno','Nombre_Abuela_Paterna',
        	      'Nombre_Madre','Apellidos_Madre','Cedula_Madre','Email_Madre','Nombre_Abuelo_Materno','Nombre_Abuela_Materna' )

# class MadreForm(forms.ModelForm):
#     class Meta:
#         model = madre
#         fields = ('Nombre_Madre','Apellidos_Madre','Cedula_Madre','Email_Madre','Nombre_Abuelo_Materno','Nombre_Abuela_Materna' )

class BautizadoForm(forms.ModelForm):
    class Meta:
        model = bautizado
        fields = ('Padres', 'Nombre_Bautizado','Apellidos_Bautizado','Id_Reg_Civil','Fecha_Nacimiento',
        	      'Lugar_Nacimiento','Telefono','Celular','Direccion','Registro_civil','Nombre_Padrino','Apellidos_Padrino',
                  'Cedula_Padrino','Estado_Civil_Padrino','Email_Padrino','Fotocopia_Cedula_Padrino',
                  'Nombre_Madrina','Apellidos_Madrina','Cedula_Madrina','Estado_Civil_Madrina','Email_Madrina','Fotocopia_Cedula_Madrina')
        	
BautizadoFormSet = inlineformset_factory(padres, bautizado, extra=0,can_delete=False, min_num=1, fields=('Padres', 'Nombre_Bautizado','Apellidos_Bautizado','Id_Reg_Civil','Fecha_Nacimiento',
                                                                                                          'Lugar_Nacimiento','Telefono','Celular','Direccion','Registro_civil','Nombre_Padrino','Apellidos_Padrino',
                                                                                                          'Cedula_Padrino','Estado_Civil_Padrino','Email_Padrino','Fotocopia_Cedula_Padrino',
                                                                                                          'Nombre_Madrina','Apellidos_Madrina','Cedula_Madrina','Estado_Civil_Madrina','Email_Madrina','Fotocopia_Cedula_Madrina'))