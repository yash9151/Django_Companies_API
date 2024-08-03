
from django.http import HttpResponse, JsonResponse

def home(request):
    print("In Home Page")
    # return HttpResponse("From Home method in views")
    context = [
        "Yash",
        "SUnny"
    ]
    return JsonResponse(context, safe=False)