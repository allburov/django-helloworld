from django.http import HttpResponse

def index(request):
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.all()
    except:
        return HttpResponse("Oh, ah, you don't have a DB!")
    
    return HttpResponse("Hello, world!")
