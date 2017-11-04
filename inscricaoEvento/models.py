from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    usuario = models.ForeignKey(User, null=True, blank=False)
    def __str__(self):
        return '{}'.format(self.nome)
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=256)
    sigla = models.CharField(max_length=14)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=256)
    logotipo = models.CharField(max_length=40)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    def __str__(self):
        return '{}'.format(self.nome)
class Ticket(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    evento = models.ForeignKey(Evento, null=True, blank=False)
    def __str__(self):
        return '{}'.format(self.nome)

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, related_name = 'Evento_Inscricao', null = True, blank = False)
    participante = models.ForeignKey(Pessoa, related_name = 'Pessoa_Inscricao', null = True, blank = False)
    ticket = models.ForeignKey(Ticket, related_name = 'Ticket_Inscricao', null = True, blank = False)
    validacao = models.BooleanField("Pagamento Confirmado",default=True)
    def __str__(self):
        return '{}'.format(self.evento)
    