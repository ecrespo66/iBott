from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

# Create your views here.
from blog.models import Subscriber
from blog.models import Post


def index(request):
    if request.method == "POST":
        Subscriber(mail=request.POST['mail']).save()
        return redirect("/")
    posts = Post.objects.all()
    return render(request, "templates/index.html", context={"posts": posts})

def product(request):
    return render(request, "templates/product.html")

def services(request):
    return render(request, "templates/service.html")


def contact(request):
    return render(request, "templates/contact.html")


def blog(request):
    posts = Post.objects.all()
    return render(request, "templates/blog.html", context={"posts": posts})


def single_post(request, url):
    post = Post.objects.get(url=url)
    return render(request, "templates/single-post.html", context={"post": post})


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'title', 'excerpt', 'image', 'content']

    def __init__(self, *args, **kwargs):
        super(PostForm,self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Post url', 'required': 'required'})
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Post title', 'required': 'required'})
        self.fields['excerpt'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Post resume', 'required': 'required'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})

@login_required
def new_post(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'creator': request.user})
        form = PostForm(updated_request, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'submitted succesfully {}'.format(post))
            return redirect('/')
    form = PostForm()

    return render(request, "templates/new_post.html", {'form': form})


@requires_csrf_token
def upload_image_view(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    filename = str(f).split('.')[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse({'success': 1, 'file': {'url': fileurl}})


@requires_csrf_token
def uploadi(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    filename = str(f).split('.')[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse({'success': 1, 'file': {'url': fileurl}})


@requires_csrf_token
def uploadf(request):
    f = request.FILES['file']
    fs = FileSystemStorage()
    filename, ext = str(f).split('.')
    file = fs.save(str(f), f)
    fileurl = fs.url(file)
    fileSize = fs.size(file)
    return JsonResponse({'success': 1, 'file': {'url': fileurl, 'name': str(f), 'size': fileSize}})


def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup
    url = request.GET['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    metas = soup.find_all('meta')
    description = ""
    title = ""
    image = ""
    for meta in metas:
        if 'property' in meta.attrs:
            if (meta.attrs['property'] == 'og:image'):
                image = meta.attrs['content']
        elif 'name' in meta.attrs:
            if (meta.attrs['name'] == 'description'):
                description = meta.attrs['content']
            if (meta.attrs['name'] == 'title'):
                title = meta.attrs['content']
    return JsonResponse({'success': 1, 'meta':
        {"description": description, "title": title, "image": {"url": image}
         }})


def site_pages(request, url=None):
    if url is not None:
        post = Post.objects.get(url=url)
        return render(request, "templates/single-post.html", context={"post": post})

