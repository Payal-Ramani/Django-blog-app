from django.views.generic import TemplateView,ListView,detail

from .models import Blogs
from .models import Authors

class HomePage(TemplateView):
    template_name = 'blog/homepage.html'

class BlogListView(ListView):
    template_name = 'blog/bloglistpage.html'
    queryset = Blogs.objects.order_by('-posted_date')
    paginate_by = 5

class BlogDetailView(detail.DetailView):
    model = Blogs
    template_name = 'blog/blogdetailpage.html'

class AuthorDetailView(ListView):
    model = Blogs
    template_name = 'blog/authordetailpage.html'
    context_object_name = 'author_detail'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author_id=self.kwargs["pk"]).order_by('-posted_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["context"] = Authors.objects.filter(id=self.kwargs["pk"]).first()
        return context
