from django.shortcuts import render, redirect
from .models import Comment

# Create your views here.
def index(request): 
    return render(request, 'sandbox/signin.html', locals()) 
def demo25(request):
    return render(request, 'sandbox/demo25.html', locals())
def signup(request):
    return render(request, 'sandbox/signup.html', locals())




def blogpost(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        comment_text = request.POST.get('comment')

        Comment.objects.create(
            name=name,
            email=email,
            website=website,
            comment=comment_text
        )
        return redirect( 'sandbox/blog-post.html')  # Замените 'your_redirect_url' на адрес, куда перенаправлять после отправки комментария
    return render(request,  'sandbox/blog-post.html')  # Замените 'your_template.html' на имя вашего шаблона

def show_comments(request):
    comments = Comment.objects.all()
    return render(request,  'sandbox/blog-post.html', {'comments': comments})  # Замените 'comments.html' на имя вашего шаблона для отображения комментариев
