from django.shortcuts import render
from .models import PostModel
def index(request):
      allpost = PostModel.objects.all()
      d={
          'posts': all post
      }
    
    return render(request, 'photo_app/index.html')
