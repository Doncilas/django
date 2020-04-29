from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    This will return text on my website
    :param request: request, context=variabila
    :return: text on website
    """
    my_dict = {'insert_me': "Hello i am from views.py"}
    return render(request, 'my_personal_blog/basics.html', context=my_dict)


def help_me(request):
    help_page = {'insert_help': 'This is my help from views.py'}
    return render(request, "my_personal_blog/help.html", context=help_page)



