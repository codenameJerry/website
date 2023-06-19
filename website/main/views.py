from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def menu(request):
    return render(request, 'main/menu.html')

def team(request):
    return render(request, 'main/team.html')

def contacts(request):
    return render(request, 'main/contacts.html')
