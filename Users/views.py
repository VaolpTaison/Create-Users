import hashlib
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import User
from .forms import RegForm, UpdForm
from rest_framework.authtoken.models import Token


def Register(request):
    global upd
    if request.POST.get('_register'):
        upd = 0
        reg = RegForm
        update_f = UpdForm
        username = request.POST.get("username")
        domain = request.POST.get("domain")
        password = request.POST.get("password")
        hashId = hashlib.md5()
        key = hashlib.sha256(("" + password).encode('utf-8')).hexdigest()
        b = User(users='%s' % username, domain='%s' % domain, password='%s' % key)
        b.save()
        post_d = User.objects.all()
        token_all = Token.objects.order_by('user_id')
        return render(request, "Register.html", {"register": reg, "post_d": post_d, "token_all": token_all, "upd": upd,
                                                 "upd_f": update_f})
    else:
        upd = 0
        reg = RegForm
        update_f = UpdForm
        post_d = User.objects.all()
        token_all = Token.objects.order_by('user_id')
        return render(request, "Register.html", {"register": reg, "post_d": post_d, "token_all": token_all, "upd": upd,
                                                 "upd_f": update_f})
