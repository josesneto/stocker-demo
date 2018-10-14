from django.shortcuts import render


def index(request):
	context_dict = {'boldmessage': "stocker!!"}
	return render(request, 'stocker/index.html', context=context_dict)
