from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    # post = Post.objects.get(id=1)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)

    # return HttpResponse('Burası post detail sayfası')

def post_create(request):
    # form = PostForm()


    # return HttpResponse('Burası post create sayfası')
    # if request.method == "POST":
    #     print(request.POST)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title = title, content=content)
    #
    # ya boyle:
    # if request.method == "POST":
    #     # formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     # formu kullanıcıya göster
    #     form = PostForm()
    # ya da
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'form': form, }
    return render(request, 'post/form.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    print(post)
    # form = PostForm(request.POST, instance=post)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz.', extra_tags='mesaj-basarili')
        # bu sekilde css class tanimi ekledik mesaj-basarili seklinde
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'form': form, }
    return render(request, 'post/form.html', context)
    # return HttpResponse('Burası post update sayfası')

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')
    # return HttpResponse('Burası post delete sayfası')
