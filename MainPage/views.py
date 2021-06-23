from django.shortcuts import render
from django.http import HttpResponse


from .models import Settings
from .models import Slider
from .models import Section1
from .models import Section2
from .models import Section3
from .models import Section4
from .models import Section5
from .models import Footer
from .models import Message

# Create your views here.
def index(request):
    Settings1 = Settings.objects.all()
    Sliders = Slider.objects.all()
    Sections1 = Section1.objects.all()
    Sections2 = Section2.objects.all()
    Sections3 = Section3.objects.all()
    Sections4 = Section4.objects.all()
    Sections5 = Section5.objects.all()
    Footers = Footer.objects.all()
    if request.method == 'POST':
        Message1= Message()
        name=request.POST.get('fullName')
        mail=request.POST.get('email')
        message=request.POST.get('message')
        Message1.Name=name
        Message1.Mail=mail
        Message1.Messaged=message
        Message1.save()
        return render(request, 'pages/Message.html')

    
    context = {
        'settings':Settings1,
        'sliders': Sliders,
        'sections1':Sections1,
        'sections2':Sections2,
        'sections3':Sections3,
        'sections4':Sections4,
        'sections5':Sections5,
        'footers': Footers,

    }
    return render(request, 'pages/index.html',context)
