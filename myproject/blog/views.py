from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,detail

from .models import Blogs,Authors

class HomePage(TemplateView):
    template_name = 'blog/homepage.html'

class BlogListView(ListView):
    template_name = 'blog/bloglistpage.html'
    # context_object_name = 'blog_list'

    queryset = Blogs.objects.order_by('-posted_date')
    paginate_by = 5

class BlogDetailView(detail.DetailView):
    model = Blogs
    template_name = 'blog/blogdetailpage.html'

class AuthorDetailView(detail.DetailView):
    model = Authors
    template_name = 'blog/authordetailpage.html'



# def listing(request):
#     contact_list = Blogs.objects.all()
#     paginator = Paginator(contact_list, 4)

#     page_number = request.GET.get('p')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/bloglistpage.html', {'page_obj': page_obj})