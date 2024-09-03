from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import Blog


# def year_archive(request, year):
#     a_list = Blog.objects.filter(pub_date__year=year)
#     context = {"year": year, "article_list": a_list}
#     return render(request, "news/year_archive.html", context)



def blog_post_list(request):
    if request.method == 'GET':
        blog_posts = Blog.objects.all()
        return render(request, {'blog_posts': blog_posts})

    elif request.method == 'POST':
        # Use case: Create a new blog post
        pub_date = request.POST['pub_date']
        headline = request.POST['headline']
        content = request.POST['content']
        new_post = Blog.objects.create(pub_date=pub_date, headline=headline, content=content)
        new_post.save()
        return redirect('blog-post-list')