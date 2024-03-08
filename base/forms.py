# Não criar formulário no HTML, mas sim em uma aba forms

from django import forms
from base.models import Cadastro

class CadastroForm(forms.ModelForm): # classe, campos (field), widget
        class Meta: 
              model = Cadastro
              fields = ['nome', 'email', 'senha']
              widgets = {'senha': forms.PasswordInput()}