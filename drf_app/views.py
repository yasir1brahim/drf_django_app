from .models import User, Seminar, Section
from .serializers import UserSerializer, SeminarSerializer, SectionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserView(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeminarView(APIView):
    """
    Retrieve, update or delete a seminar instance.
    """
    def get_object(self, pk):
        try:
            return Seminar.objects.get(pk=pk)
        except Seminar.DoesNotExist:
            raise Http404

    def get(self, request):
        seminar = Seminar.objects.all()
        serializer = SeminarSerializer(seminar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SeminarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        seminar = self.get_object(pk)
        serializer = SeminarSerializer(seminar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        seminar = self.get_object(pk)
        seminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SectionView(APIView):
    """
    Retrieve, update or delete a section instance.
    """
    def get_object(self, pk):
        try:
            return Section.objects.get(pk=pk)
        except Section.DoesNotExist:
            raise Http404

    def get_seminar_object(self, pk):
        try:
            return Seminar.objects.get(pk=pk)
        except Seminar.DoesNotExist:
            raise Http404

    def get(self, request):
        seminar_id = request.GET["seminar_id"]
        seminar = self.get_seminar_object(seminar_id)
        sections = Section.objects.filter(seminar_id=seminar.id)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('pk')
        section = self.get_object(pk)
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('pk')
        section = self.get_object(pk)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)