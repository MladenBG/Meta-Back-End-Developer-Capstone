from django.shortcuts import render, redirect
from datetime import datetime
from .models import Menu, Booking
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
import requests

# Homepage
def index(request):
    return render(request, 'restaurant/index.html', {'current_year': datetime.now().year})


# Registration page
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        response = requests.post("http://127.0.0.1:8000/auth/users/",
                                 data={"username": username, "email": email, "password": password})

        if response.status_code == 201:
            return redirect("restaurant-login")
        else:
            return render(request, "restaurant/register.html", {"error": "Registration failed"})
    return render(request, "restaurant/register.html")



# Login page
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Call Djoser API internally
        response = requests.post("http://127.0.0.1:8000/auth/token/login/",
                                 data={"username": username, "password": password})

        if response.status_code == 200:
            token = response.json().get("auth_token")
            # Store token in session for later API calls
            request.session["auth_token"] = token
            return redirect("home")   # redirect to homepage
        else:
            return render(request, "restaurant/login.html", {"error": "Invalid credentials"})

    return render(request, "restaurant/login.html")
def logout_page(request):
    token = request.session.get("auth_token")
    if token:
        requests.post("http://127.0.0.1:8000/auth/token/logout/",
                      headers={"Authorization": f"Token {token}"})
    request.session.flush()   # clear everything
    return redirect("home")   # back to homepage


# Menu API views
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Booking API viewset
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]




