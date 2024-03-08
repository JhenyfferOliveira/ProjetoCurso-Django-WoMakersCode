import email
from django.db import models

# Create your models here.
# Cria uma classe que herda de outra classe chamada models
# Basicamente banco de dados
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta: # chamada das metas informações
        verbose_name = 'Formulário de contato' # indica o verbose para o valor
        verbose_name_plural = 'Formulários de contatos' # indica o verbose para o valor
        ordering = ['-data'] # parametro que indica ordenação no banco de dados (descrecente)