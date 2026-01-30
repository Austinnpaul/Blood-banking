from django.shortcuts import render



# Home page
def index(request):
    return render(request, 'index.html')

# Login page
def login_view(request):
    return render(request, 'login.html')

# Register page
def register_view(request):
    return render(request, 'register.html')
