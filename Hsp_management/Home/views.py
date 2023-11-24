from django.shortcuts import render

def home(req):
    return render(req, "home.html")


def about(req):
    return render(req, "about.html")


def booking(req):
    return render(req, "booking.html")


def doctors(req):
    return render(req, "doctors.html")


def contact(req):
    return render(req, "contact.html")


def department(req):
    return render(req, "department.html")
