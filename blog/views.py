from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


# This is using Django's generic view
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

# This isn't using Django's generic view
# When we created function based views in the Hello Django project, we pass the request object as an argument to the view, you can
# check if the request methord was get or post so that you could decide what you wanted to do.  Class based views are different. Instead
# of using an if statement to check the request method, we simply create class methods called get or post
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )

