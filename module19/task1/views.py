import random
from django.shortcuts import render
from django.http import HttpResponse

from task1.models import Buyer, Game
from task1.forms import UserRegisterForm


users = Buyer.objects.values_list('name', flat=True)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = 'Имя пользователя уже занято.'
                return HttpResponse('Имя пользователя уже занято.')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают.'
                return HttpResponse('Пароли не совпадают.')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет.'
                return HttpResponse('Вы должны быть старше 18 лет.')
            Buyer.objects.create(
                name=username,
                age=age,
                balance=random.randint(0, 1000)
            )
            info['welcome_message'] = f"Приветствуем, {username}!"
            return render(request, 'fifth_task/redirect_link.html', info)
    else:
        form = UserRegisterForm()
        info['message'] = form
    return render(request, 'fifth_task/registration_page.html', {'form': info})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username in users:
            info['error'] = 'Имя пользователя уже занято.'
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают.'
            return HttpResponse('Пароли не совпадают')
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет.'
            return HttpResponse('Вы должны быть старше 18')
        Buyer.objects.create(
                name=username,
                age=age,
                balance=random.randint(0, 1000)
            )
        info['welcome_message'] = f'Приветствуем, {username}!'
        return render(request, 'fifth_task/redirect_link.html', info)

    return render(request, 'fifth_task/registration_page.html', context=info)


def main(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/main.html', context=context)


def games_list(request):
    title = 'Игры'
    games = Game.objects.all()
    context = {
        'title': title,
        'text': games,
    }
    return render(request, 'fourth_task/games.html', context)


def cart_list(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/cart.html', context)
