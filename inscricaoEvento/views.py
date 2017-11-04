from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from inscricaoEvento.serializers import UserSerializer
from inscricaoEvento.serializers import PessoaSerializer
from inscricaoEvento.serializers import EventoSerializer
from inscricaoEvento.serializers import TicketSerializer
from inscricaoEvento.serializers import InscricaoSerializer
from inscricaoEvento.models import Pessoa
from inscricaoEvento.models import Evento
from inscricaoEvento.models import Inscricao
from inscricaoEvento.models import Ticket

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
