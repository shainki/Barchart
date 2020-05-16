
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Survey

class show(View):
    template_name = 'CSPlatform/basic.html'
    print("hello brother ")

    def get(self, request):
        obj = Survey.objects.all()
        context = {
            'table': obj
        }

        # p = Survey(Comapny_name='Apress', Realtionship_name='Berkeley',
        #            Survey_name='shainky', Name='shashank1',
        #            Email='shashank@gmail.com', Score='10',
        #            Created_date='2020-02-12 15:08:42', updated_date='2020-02-12 15:08:42')
        # p.save()

        return render(request, self.template_name, context)


