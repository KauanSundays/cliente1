from django.shortcuts import render
from posts_app.models import Posts

# Create your views here.
def post_list(request): #função post_list
    template_name = 'post-list.html' #template que iremos usar
    posts = Posts.objects.all() #todas as postagens do modelo
    context = {
        'posts':posts
    }
    return render(request, template_name, context)