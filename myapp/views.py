from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response


from myapp.models import Student
from myapp.serializers import StudentSerializer


def home(request):
    return HttpResponse("DRF project")

@api_view(["GET","POST"])
def snippet_list(request):

    if request.method == "GET":
        snippets = Student.objects.all()
        serializer =StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)




@api_view(["GET","POST","DELETE","PUT"])
def snippet_detail(request, pk):
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = request.data
        serializer = StudentSerializer(snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)