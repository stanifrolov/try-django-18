from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title = "my title %s" %(request.user)
    
    #add a form
    # if request.method == "POST":
    #   print (request.POST)
         
    context = {
        "title": title,
        "abc": 123,
        "form": form,
    }
   
    if form.is_valid():
        # form.save()
        ### print (request.POST['email']) # highly not recommended
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "new full name"
        instance.full_name = full_name
                       
        # if not instance.full_name:
        #     instance.full_name = "justin"
        
        instance.save()
        context = {
            "title": "Thank you"
        }
        # print (instance.email)
        # print (instance.timestamp)

    return render(request, "home.html", context)
    

def contact(request):
     form = ContactForm(request.POST or None)
     if form.is_valid():
        # for key,value in form.cleaned_data.items(): #iteritems() in 2.7
        #     print(key, value)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print (email, message, full_name)
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'stani_frolov@web.de']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False
                  )
        
     context = {
        "form": form,
      }
    
     return render(request, "forms.html", context)