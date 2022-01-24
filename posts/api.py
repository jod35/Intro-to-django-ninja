from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List
from .schemas import PostInSchema, PostOutSchema
from .models import Post

post_router = Router()


@post_router.get("/posts", response={200: List[PostOutSchema]})
def index(request):
    return Post.objects.all()


@post_router.post("/posts", response={201: PostOutSchema})
def create_post(request, payload: PostInSchema):
    new_post = Post.objects.create(**payload.dict())

    return 201, new_post


@post_router.get("/post/{post_id}", response={200: PostOutSchema})
def get_one_post(request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return 200, post


@post_router.put("post/update/{post_id}", response={200: PostOutSchema})
def update_post(request, post_id: int, post: PostInSchema):
    post_to_update = get_object_or_404(Post, pk=post_id)

    post_to_update.title = post.title
    post_to_update.content = post.content

    post_to_update.save()

    return 200, post_to_update


@post_router.delete("post/delete/{post_id}", response={204: None})
def delete_post(request, post_id):
    post_to_delete = get_object_or_404(Post, pk=post_id)

    post_to_delete.delete()

    return 204
