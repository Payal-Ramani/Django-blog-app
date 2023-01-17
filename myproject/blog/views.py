from django.views.generic import TemplateView,ListView,detail

from .models import Blogs,Authors,Comment

class HomePage(TemplateView):
    template_name = 'blog/homepage.html'

class BlogListView(ListView):
    template_name = 'blog/bloglistpage.html'
    queryset = Blogs.objects.order_by('-posted_date')
    paginate_by = 5

class BlogDetailView(ListView):
    model = Comment
    template_name = 'blog/blogdetailpage.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(blog_id = self.kwargs['pk']).order_by('commented_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["context"] = Blogs.objects.filter(id = self.kwargs["pk"]).first()
        return context

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

class AuthorListView(ListView):
    template_name = 'blog/authorlistpage.html'
    queryset = Authors.objects.all()
