from django.shortcuts import render

def home(request):
	import requests
	import json
	
	#Grab crypto price
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XML,ADA,USDT,MIOTA,TRX&tsyms=USD,INR")
	price = json.loads(price_request.content)

	#Grab crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price' :price}) 

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,INR")
		crypto = json.loads(crypto_request.content)
		
		return render(request, 'prices.html', {'crypto':crypto})
	else:
		notfound = "Enter the crypto curreny symbol in the form above"
		return render(request, 'prices.html', {'notfound': notfound})

def about(request):
	return render(request, 'about.html', {})
