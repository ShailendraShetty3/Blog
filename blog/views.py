

# import logging

# logger = logging.getLogger('django_debug')

# def some_view(request):
#     logger.debug("This is a debug message")
#     logger.error("This is an error message")





# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Blog
# from .serializers import BlogSerializer

# @api_view(['GET', 'POST'])
# def blog_post_list(request):
#     if request.method == 'GET':
#         blog_posts = Blog.objects.all()
#         serializer = BlogSerializer(blog_posts, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
import logging

logger = logging.getLogger('django_debug')

@api_view(['GET', 'POST'])
def blog_post_list(request):
    if request.method == 'GET':
        try:
            blog_posts = Blog.objects.all()
            serializer = BlogSerializer(blog_posts, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving blog posts: {e}", exc_info=True)
            return Response({"detail": "Error retrieving blog posts"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating blog post: {e}", exc_info=True)
            return Response({"detail": "Error creating blog post"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
