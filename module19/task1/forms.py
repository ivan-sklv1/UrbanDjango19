from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(
        label='Введите пароль',
        min_length=8
    )
    repeat_password = forms.CharField(
        label='Повторите пароль',
        min_length=8
    )
    age = forms.IntegerField(
        label='Введите свой возраст'
    )
