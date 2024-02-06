from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views import View
from django.conf import settings


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class SendEmailView(View):
    def get(self, request):
        email = EmailMessage(
            'Hello from Django',
            'This is a test email.',
            settings.DEFAULT_FROM_EMAIL ,
            ['msgeorgem@gmail.com'],
           
            )
        email.send()
        print(settings.EMAIL_HOST, settings.EMAIL_PORT, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, settings.EMAIL_USE_TLS)
        return HttpResponse('Email sent to msgeorgem@gmail.com')
