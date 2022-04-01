from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from Xamination.views import home
import random

jawaban_user = []
K_jawaban_mtk = ['b','b','b','b','a']
K_jawaban_ipa = ['a','a','d','b','c']
K_jawaban_indo = ['b','c','d','c','d']
K_jawaban_ing = ['c','b','b','b','c']

def quote():
	isi = [
	['Tak ada penyakit yang tak bisa disembuhkan kecuali kemalasan. Tak ada obat yang tak berguna selain kurangnya pengetahuan', 'Ibnu Sina'],
	['Nafsu bisa membuat seorang Raja menjadi Budak. Sementara sabar bisa membuat seorang Budak menjadi Raja.', 'Imam Al-Ghazali'],
	['If you can’t explain it simply, you don’t understand it well enough.', 'Albert Einstein'],
	['Ilmu tidak akan dapat diraih kecuali dengan ketabahan.', "Imam Syafi'i"],
	['Untuk mendapatkan apa yang Anda sukai, Anda harus bersabar dengan apa yang Anda benci.', 'Abu Hamid Al Ghazali'],
	['Akar pendidikan itu pahit, tapi buahnya manis.', 'Aristoteles'],
	['Live as if you were to die tomorrow. Learn as if you were to live forever.', 'Mahatma Gandhi'],
	['Untuk mendapatkan apa yang Anda sukai, Anda harus bersabar dengan apa yang Anda benci.', 'Abu Hamid Al Ghazali']]

	random.shuffle(isi)
	quotenya = isi[0][0]
	orangnya = isi[0][1]

	return [quotenya, orangnya]


def soal_mtk(request):
	jawaban = ''
	print(request.POST)
	respon = request.POST	
	if str(request) == "<WSGIRequest: GET '/mapel/mtk/soal'>" and len(jawaban_user) == 5:
		print('masuk')
		for i in range(5):
			print(jawaban_user)
			if jawaban_user[0] in 'abcd':
				jawaban_user.remove(jawaban_user[0])
			else:
				jawaban_user.remove(' ')
		jawaban = ''

	if request.method == 'POST':
		urut = 1
		for i in range(5):
			if f'soal_{urut}' in respon:
				jawaban += respon[f'soal_{urut}']
				urut += 1
			else:
				jawaban += ' '
				urut += 1
	for i in jawaban:
		jawaban_user.append(i)
	print(jawaban_user)
	a = request
	print(str(a))
	if request.method == 'POST':
		return redirect('hasil_mtk')
	return render(request, 'ProbationSoal/mtk.html')
	
def jawaban_mtk(request):
	benar = 0
	salah = 0
	if len(jawaban_user) >= 1:
		for i in range(5):
			if jawaban_user[i] == K_jawaban_mtk[i]:
				benar += 1
			else:
				salah += 1
	else:
		return redirect('soal_mtk')

	context = {
	'jawaban_benar' : benar,
	'jawaban_salah' : salah,
	'isi_quote' : quote()[0],
	'orang_quote' : quote()[1]
	}
	return render(request, 'selamat/selamat_mtk.html', context)

def soal_ipa(request):
	jawaban = ''
	print(request.POST)
	respon = request.POST	
	if str(request) == "<WSGIRequest: GET '/mapel/ipa/soal'>" and len(jawaban_user) == 5:
		print('masuk')
		for i in range(5):
			print(jawaban_user)
			if jawaban_user[0] in 'abcd':
				jawaban_user.remove(jawaban_user[0])
			else:
				jawaban_user.remove(' ')
		jawaban = ''

	if request.method == 'POST':
		urut = 1
		for i in range(5):
			if f'soal {urut}' in respon:
				jawaban += respon[f'soal {urut}']
				urut += 1
			else:
				jawaban += ' '
				urut += 1
	for i in jawaban:
		jawaban_user.append(i)
	print(jawaban_user)
	a = request
	print(str(a))
	if request.method == 'POST':
		return redirect('hasil_ipa')
	return render(request, 'ProbationSoal/ipa.html')

def jawaban_ipa(request):
	benar = 0
	salah = 0
	if len(jawaban_user) >= 1:
		for i in range(5):
			if jawaban_user[i] == K_jawaban_ipa[i]:
				benar += 1
			else:
				salah += 1
	else:
		return redirect('soal_ipa')

	context = {
	'jawaban_benar' : benar,
	'jawaban_salah' : salah,
	'isi_quote' : quote()[0],
	'orang_quote' : quote()[1]
	}
	return render(request, 'selamat/selamat_ipa.html', context)


def soal_indo(request):
	jawaban = ''
	print(request.POST)
	respon = request.POST	
	if str(request) == "<WSGIRequest: GET '/mapel/indo/soal'>" and len(jawaban_user) == 5:
		print('masuk')
		for i in range(5):
			print(jawaban_user)
			if jawaban_user[0] in 'abcd':
				jawaban_user.remove(jawaban_user[0])
			else:
				jawaban_user.remove(' ')
		jawaban = ''

	if request.method == 'POST':
		urut = 1
		for i in range(5):
			if f'soal {urut}' in respon:
				jawaban += respon[f'soal {urut}']
				urut += 1
			else:
				jawaban += ' '
				urut += 1
	for i in jawaban:
		jawaban_user.append(i)
	print(jawaban_user)
	a = request
	print(str(a))
	if request.method == 'POST':
		return redirect('hasil_indo')
	return render(request, 'ProbationSoal/indo.html')

def jawaban_indo(request):
	benar = 0
	salah = 0
	if len(jawaban_user) >= 1:
		for i in range(5):
			if jawaban_user[i] == K_jawaban_indo[i]:
				benar += 1
			else:
				salah += 1
	else:
		return redirect('soal_indo')

	context = {
	'jawaban_benar' : benar,
	'jawaban_salah' : salah,
	'isi_quote' : quote()[0],
	'orang_quote' : quote()[1]
	}
	return render(request, 'selamat/selamat_bindo.html', context)
	
def soal_ing(request):
	jawaban = ''
	print(request.POST)
	respon = request.POST	
	if str(request) == "<WSGIRequest: GET '/mapel/b_ing/soal'>" and len(jawaban_user) == 5:
		print('masuk')
		for i in range(5):
			print(jawaban_user)
			if jawaban_user[0] in 'abcd':
				jawaban_user.remove(jawaban_user[0])
			else:
				jawaban_user.remove(' ')
		jawaban = ''

	if request.method == 'POST':
		urut = 1
		for i in range(5):
			if f'soal {urut}' in respon:
				jawaban += respon[f'soal {urut}']
				urut += 1
			else:
				jawaban += ' '
				urut += 1
	for i in jawaban:
		jawaban_user.append(i)
	print(jawaban_user)
	a = request
	print(str(a))
	if request.method == 'POST':
		return redirect('hasil_ing')
	return render(request, 'ProbationSoal/inggris.html')

def jawaban_ing(request):
	benar = 0
	salah = 0
	if len(jawaban_user) >= 1:
		for i in range(5):
			if jawaban_user[i] == K_jawaban_ing[i]:
				benar += 1
			else:
				salah += 1
	else:
		return redirect('soal_ing')

	context = {
	'jawaban_benar' : benar,
	'jawaban_salah' : salah,
	'isi_quote' : quote()[0],
	'orang_quote' : quote()[1]
	}
	return render(request, 'selamat/selamat_bing.html', context)
