from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# def index(request):
#    return HttpResponse("hello world!")


class IndexAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "base/index.html"

    def get(self, request):
        return Response()
