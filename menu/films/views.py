from django.http import HttpResponse
from django.shortcuts import render, redirect
from films.models import *

dat = Menu.objects.all()
FCSDict1 = {'cartoons':'мультфильма','films':'фильма','series':'сериала'}
FCSDict2 = {'director':'режиссеру','genre':'жанру','year':'году'}

def main_menu(request):
	one = {}
	one_l = []
	for i in dat:
		one_l.append(i.one_l)
	one_l = list(set(one_l))
	for i in one_l:
		one.update({i: i.lower()+'/'})	
	data = {'one':one}    
	return render(request, 'main_menu.html', context=data)

def one_layer(request):
	lay = 'Критерии выбора:'
	one = {}
	one_l = ['Director', 'Genre', 'Year']
	for i in one_l:
		one.update({i: i.lower()+'/'})
	data = {'lay':lay,'one':one}
	return render(request, 'second_layer.html', context=data)

def two_layer(request):
	pat = request.path
	FCS1 = pat[1:].split('/')[0]
	FCS2 = pat[1:].split('/')[1]
	lay = 'Меню выбора '+ FCSDict1[FCS1] +' по ' + FCSDict2[FCS2]
	one = {}
	l = []
	a = ''
	for i in dat:
		if FCS1==i.one_l.lower():
			if (FCS2=='director'):
				a = i.two_l
			elif (FCS2=='genre'):
				a = i.three_l
			elif (FCS2=='year'):
				a = str(i.four_l)
			l.append(a)
	l = list(set(l))
	for i in l:
		a = i.replace(' ', '')
		one.update({i: a.lower()+'/'})
	data = {'lay':lay,'one':one} 
	return render(request, 'second_layer.html', context=data)

def finSel(request):
	
	def calc(datFin,FCS1,FCS2,FCS3):
		res=[]
		for i in datFin:
			if (FCS2=='director'):
				a = i.director
			elif (FCS2=='genre'):
				a = i.genre
			elif (FCS2=='year'):
				a = str(i.year)
			a = a.replace(' ', '').lower()
			if a == FCS3:
				res.append(i)	
		return res
		
	one = {}
	lay = 'Был выбран: '
	pat = request.path
	FCS1 = pat[1:].split('/')[0]
	FCS2 = pat[1:].split('/')[1]
	FCS3 = pat[1:].split('/')[2]
	
	if FCS1 == 'cartoons':
		datFin = Cartoons.objects.all()
	if FCS1 == 'films':
		datFin = Films.objects.all()
	if FCS1 == 'series':
		datFin = Series.objects.all()	
	one = calc(datFin,FCS1,FCS2,FCS3)
	data = {'lay':lay,'one':one} 
	return render(request, 'fin.html', context=data)
	
