from django.shortcuts import render

def home(request):
    import json
    import requests

    # Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,USDC,BUSD,XPR,DOGE,ADA,MATIC&tsyms=USD")
    price = json.loads(price_request.content)

    # Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    if request.method == 'POST':
        import json
        import requests
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter the cryptocurrency symbol in the search box on the right above. "
        return render(request, 'prices.html', {'notfound': notfound})

