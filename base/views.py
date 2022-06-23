
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import NewUserForm, NeighbourhoodForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Profile,Neighborhoods_cool
from django.contrib.auth import logout



from django.contrib.auth.decorators import login_required

# Create your views here.
class LoginInterfaceView(LoginView):
    template_name= 'base/registration/login.html'


class SignupView(CreateView):
    form_class=NewUserForm
    template_name= 'base/registration/register.html'
    success_url='/'

    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request,*args, **kwargs)



def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    form= NeighbourhoodForm()
    if request.method =='POST':
        form= NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.admin=request.user
            hood.save()

    posts = Neighborhoods_cool.objects.all()


    context=dict(form=form,posts=posts)
    
    return render(request,'base/home.html',context)

def neighbor(request,id):
    neighbor = Neighborhoods_cool.objects.get(id=id)
   
    context=dict(neighbor=neighbor)

    return render(request,'base/neighborhood.html',context)


def userProfile(request,pk):
    user= Profile.objects.get(user=pk)
    neighborhoods = user.neighborhoods_cool_set.all()
    messages = user.message_set.all()
    context=dict(user=user,neighborhoods=neighborhoods,messages=messages)

    return render( request , 'base/profile.html' ,context)
