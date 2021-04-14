from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
	return render(request, 'arithmetic/home.html')

# Create your views here.
@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    num = req.get('queryResult').get('parameters')
    n1 = int(num.get('number'))
    n2 = int(num.get('number1'))
    if action == 'addition':
    # return a fulfillment message
    	fulfillmentText = {'fulfillmentText': n1+n2}

    elif action == 'subtraction':
    	fulfillmentText = {'fulfillmentText': n1-n2}

    elif action == 'division':
    	fulfillmentText = {'fulfillmentText': n1/n2}

    elif action == 'multiplication':
    	fulfillmentText = {'fulfillmentText': n1*n2}
    
    else:
        fulfillmentText = {'fulfillmentText': "Invalid operation!!"}
    # return response
    return JsonResponse(fulfillmentText, safe=False)