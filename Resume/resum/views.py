from django.shortcuts import render
from . models import Resume

def resume_view(request):
    resume=Resume.objects.first()
    return render(request,'index.html',{'resume':resume})
