from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

def home(request):
	return render(request, 'ProbationHomePage/home.html')

def about(request):
	return render(request, 'ProbationAbout/about.html')

def mapel(request):
	return render(request, 'ProbationMapel/mapel.html')

def mtk(request):
	return render(request, 'ProbationBankSoal/MTK/bankSoal-mtk.html')

def bing(request):
	return render(request, 'ProbationBankSoal/B Ing/bankSoal-bing.html')

def bindo(request):
	return render(request, 'ProbationBankSoal/B Indo/bankSoal-bindo.html')

def ipa(request):
	return render(request, 'ProbationBankSoal/IPA/bankSoal-ipa.html')