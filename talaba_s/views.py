from django.shortcuts import render


from .models import Talaba

def talaba(request):
    talabalar = Talaba.objects.all()
    context = {
        'news': talabalar
    }

    return render(request, 'talaba_s/index.html', context=context)

