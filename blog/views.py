from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .models import Author, Post, Tag

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "music.jpg",
#         "author": "Nidhi",
#         "date": date(2023, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "scaredy-cat.jpg",
#         "author": "Nidhi",
#         "date": date(2023, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "music.jpg",
#         "author": "Nidhi",
#         "date": date(2023, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

# def get_date(post):
#     return post['date']

# Create your views here.
def main_page(request):
    # don't call get_date instead we point to get date
    # not changing existing list

    latest_posts = Post.objects.all().order_by("-date")

    # sorted_posts = sorted(all_posts, key = get_date)
    # latest_posts = sorted_posts[-3:]
    response = render(request, "blog/index.html", {
        "posts" : latest_posts
    })
    return HttpResponse(response)

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts" : Post.objects.all()
    })

def the_post(request, slug):
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html",{
        "post" : identified_post,
        "tags" : identified_post.tags.all()
    })