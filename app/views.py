from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    print(data)
    return JsonResponse(data)

def success(request):
	return HttpResponse('Registered successfully!')

class SignUpView(CreateView):
    template_name = 'app/signup.html'
    form_class = UserCreationForm

    def get_absolute_url(self): # new
    	return reverse('')