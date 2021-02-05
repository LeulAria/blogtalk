from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 2

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

#     def get_context_date(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = get_object_or_404(Post, slug=slug)
#         context['comments'] = post.comments.order_by('created_on')


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.order_by('created_on')

    paginator = Paginator(comments, 2)
    page = request.GET.get('comments')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    # if request.method == 'POST':
    #     pass
    # else:
    #     comment_form = Commentform()

    return render(request, template_name, {
        "post": post,
        "page": page,
        "comments": comments
    })