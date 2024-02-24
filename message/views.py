from django.shortcuts import render
from .models import query
def message(request):
    if request.method == 'POST':
        n = request.POST['name']
        e = request.POST['email']
        sub = request.POST['sub']
        msg = request.POST['msg']
        data = query.objects.create(name=n,email=e,subject=sub,msg=msg)
        data.save()
    return render(request,'home.html')
# Create your views here.
