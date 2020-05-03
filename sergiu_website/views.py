from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    """
    This will return text on my website
    :param request: request, context=variabila
    :return: text on website
    """
    return render(request, 'my_personal_blog/basics.html')


def users(request):
    users = User.objects.order_by('first_name')
    users_dict = {'users': users}
    return render(request,"my_personal_blog/help.html", context=users_dict)


# def help_me(request):
#     help_page = {'insert_help': 'This is my help from views.py'}
#     return render(request, "my_personal_blog/help.html", context=help_page)



