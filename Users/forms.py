from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label='Логин ', max_length=70)
    domain = forms.CharField(label='Домен', max_length=70)
    password = forms.CharField(label='Пароль', max_length=70)


class UpdForm(forms.Form):
    upd_user = forms.CharField(max_length=70)
    upd_pass = forms.CharField(max_length=70)
