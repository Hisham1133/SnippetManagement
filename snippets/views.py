from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snipets,Tag,SnipetNotes
from snippets.serializers import SnipetSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class SnippetList(APIView):
    def get(self, request,pk=None,*args,**kwarg):
        id=self.kwargs.get('pk')
        if id!=None:
            snippets = Snipets.objects.get(id=id)
            serializer = SnipetSerializer(snippets)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        snippets = Snipets.objects.all()
        serializer = SnipetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnipetSerializer(data=request.data)
        data=request.data
        tag_name = data.get('tag',None)
        snippet_body = data.get('snippet_body',None)

        if tag_name !=None and snippet_body!=None:

            # Tag name creation
            t1 = Tag.objects.filter(tag_name=tag_name)
            if t1.count() < 1:
                new_tag=Tag.objects.create(tag_name=tag_name)
                new_tag.save()

            # snippet Body Creation
            new_body = SnipetNotes.objects.create(body=snippet_body)
            new_body.save()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

