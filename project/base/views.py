from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe 

stripe.api_key = "sk_test_51IithQSHTaAN3caOp5aP9VtENQM37RrHa6d9fd1BJltW5u8reUjbMvCmfjdrxM4ks2fOlfPsJ8Aqg3S9XDx1MufP00Uh8Zkk6r"

# Create your views here.

def index(request):
	
	return render(request, 'base/index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})