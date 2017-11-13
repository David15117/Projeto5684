from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from inscricaoEvento.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')
	def create(self, validated_data):
		user = User.objects.create(**validated_data)# pega todos objetos de usuario
		return user#Sempre deve retorna
			

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
	usuario = UserSerializer(many=False)
	class Meta:
		model = Pessoa
		fields = ('usuario','nome', 'sexo', 'idade')
	def create(self,dados):
		dados_user=dados.pop('usuario')# remove usuario
		u = User.objects.create(**dados_user)# criar o usuario
		p = Pessoa.objects.create(usuario=u,**dados)#criar pessoa, e em dados insere objetivo de usuario
		return p
class EventoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Evento
		fields = '__all__'
	def create(self, dados):
		dados_evento = 	Evento.objects.create(**dados)
		return dados_evento

class TicketSerializer(serializers.HyperlinkedModelSerializer):
	evento = EventoSerializer(many=False)
	class Meta:
		model = Ticket
		fields = ('__all__')
	def create(self,dados):
		dados_evento = dados.pop('evento')
		evento = Evento.objects.get(nome=dados_evento)
		ticket = Ticket.objects.create(evento = evento,**dados)
		#evento = Evento.objects.create(**dados_evento)
		#ticket = Ticket.objects.create(evento = evento,**dados)
		return ticket
class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
	participante = PessoaSerializer(many=False)
	ticket = TicketSerializer(many=False)
	#evento = EventoSerializer(many=False)
	class Meta:
		model = Inscricao
		fields = ('__all__')
	def create(self,dados):
		dados_tickets = dados.pop('ticket')
		#dados_evento = dados.pop('evento')
		dados_participante = dados.pop('participante')
		#evento = Evento.objects.create(**dados_evento)
		pessoa = Pessoa.objects.create(**dados_participante)
		tickets = Ticket.objects.create(**dados_tickets)
		I = Inscricao.objects.create( ticket = tickets, participante = pessoa, **dados)
		return I