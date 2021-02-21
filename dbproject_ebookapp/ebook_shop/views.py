from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import NewUserForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate,  login, logout

from .models import New_Arrivals
from math import ceil

def index(request):
    return render(request,'ebook_shop/index.html')


def eBooks(request):
    
    allProds = []
    catprods = New_Arrivals.objects.values('type', 'id')
    cats = {item['type'] for item in catprods}
    for cat in cats:
        prod = New_Arrivals.objects.filter(type=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'ebook_shop/BookViews.html', params)


def Details(request,id):
    bk= New_Arrivals.objects.all()
    print(bk)
    detail=New_Arrivals.objects.filter(id=id)
    print(detail)
    params = {"detail":detail[0]}
    return render(request,'ebook_shop/BookDetails.html',params)


def SignUp(request):
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match, try again")
             return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been created")
        return redirect('eBooks')

    else:
        return HttpResponse("404 - Not found")

def Login(request):
      if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        #messages.success(request, "Successfully Logged In")
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            
            return redirect("eBooks")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

        return HttpResponse("404- Not found")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def download(request,path):
    file_path= os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response= HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = New_Arrivals.objects.values('type', 'id')
    cats = {item['type'] for item in catprods}
    for cat in cats:
        prodtem = New_Arrivals.objects.filter(type=cat)
        prod= [item for item in prodtem if query if Match(query,item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'ebook_shop/BookViews.html', params)
    if len(allProds)==0:
       messages.error(request,"Not Found! Please try again")
       return redirect('eBooks')

def Match(query, item):
    if query in item.book_name.lower() or query in item.author_name.lower() or query in item.isbn:
        return True
    else:
        return False







    




 






