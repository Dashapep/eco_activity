from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView
from .models import Events


class MainView(TemplateView):
    template_name = 'events_main.html'

    def get(self, request):
        if request.user.is_authenticated:
            events = Events.objects.filter(author=request.user)
            ctx = {'events': events}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/events/'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid()

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid()

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/events/')
