from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


#def UserDetails(request):
    #product=product.objects.all()
    #return render(request,'user.html',{'product':product})