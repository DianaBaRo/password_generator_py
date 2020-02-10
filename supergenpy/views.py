from django.shortcuts import render
from django.utils import timezone
from .models import Login

def login_list(request):
    logins = Login.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'views/login_list.html', {'logins': logins})