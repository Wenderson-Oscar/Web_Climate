from django.shortcuts import render
from django.views.generic import View, TemplateView
from climate.settings import API_KEY, MEDIA_URL
import requests
import folium
import os

class Climate(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cidade = self.request.GET.get('cidade')
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        requisicao = requests.get(link)
        nomes_requisicao = requisicao.json()
        if requisicao:
            context['localizacao'] = nomes_requisicao['coord']
            context['clima'] = nomes_requisicao['weather'][0]['description']
            context['nome'] = nomes_requisicao['name']
            context['humidade'] = nomes_requisicao['main']['humidity']
            temp = nomes_requisicao['main']['temp'] - 273.15
            context['temperatura'] = f'{temp:.2f}'
            latitude = nomes_requisicao['coord']['lat']
            longitude = nomes_requisicao['coord']['lon']
            mapa = folium.Map(location=[latitude, longitude], zoom_start=10)
            folium.Marker([latitude, longitude], popup=context['nome']).add_to(mapa)
            map_file_path = f'mapa_{context["nome"]}.html'
            mapa.save(os.path.join(MEDIA_URL, map_file_path))
            context['map_file_path'] = os.path.join(MEDIA_URL, map_file_path)
        else:
            context['error_message'] = 'Cidade Não encontrada!'
        return context
