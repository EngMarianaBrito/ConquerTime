from django.db import models
from django import forms

# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField('Nome Categoria', max_length=250)
    descricao = models.TextField('Descricao')
    #falta inserir dps as estatisticas
    def __str__(self) -> str:
        return self.nome_categoria

class DadosSede(models.Model):
    nome_empresa = models.CharField('Nome da empresa', max_length=250)
    texto_sobre = models.TextField('Sobre nós')
    chamada = models.TextField('Chamada', null=True)
    whatsapp = models.TextField('Whatsapp', null=True, blank=True)
    localizacao = models.TextField('Localização', null=True, blank=True)
    instagram = models.TextField("Instagram", null=True, blank=True)
    email = models.TextField(null=True);

    def __str__(self) -> str:
        return self.nome_empresa

class Formulario(forms.Form):
    DIAS_CHOICES =(
        ("SE", "Segunda"),
        ("TE", "Terça"),
        ("QA", "Quarta"),
        ("QI", "Quinta"),
        ("SX", "Sexta"),
        ("SA", "Sabado"),
        ("DM", "Domingo"),
    )

    dias = forms.MultipleChoiceField(choices=DIAS_CHOICES)

class Tarefa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    nome_tarefa = models.CharField('Nome Tarefa', max_length=250)
    descricao = models.TextField('Descrição')
    duracao = models.TimeField()
    hora_notificacao = models.TimeField()
    hora_criacao = models.DateTimeField()
    #frequencia_semana = models.OneToOneField(Formulario, on_delete=models.CASCADE) nao funciona assim
    frequencia_dias = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)

class Insignia(models.Model):
    nome_insignia = models.CharField(max_length=100)
    xp_maximo = models.IntegerField(default=500)
    lvl_maximo = models.IntegerField(default=10)
    lvl_atual = models.IntegerField(default=0)

class Medalha(models.Model):
    nome_medalha = models.CharField(max_length=100)
    xp_atribuido = models.IntegerField(default=100)
