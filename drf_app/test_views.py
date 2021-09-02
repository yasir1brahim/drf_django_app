from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from . import views
from .models import User, Seminar


class UserViewCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            first_name='philipp', last_name='hafner')

    def test_get(self):
        status_code = 200
        view_class = views.UserView

        req = self.factory.get('/api/user/')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_post(self):
        status_code = 201
        view_class = views.UserView

        data = {'first_name':'philipp', 'last_name':'hafner'}
        req = self.factory.post('/api/user/', data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_put(self):
        status_code = 200
        view_class = views.UserView

        data = {'first_name': 'philipp', 'last_name': 'hazner'}
        req = self.factory.put(
            '/api/user/?pk=' + str(self.user.id), data=data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_delete(self):
        status_code = 204
        view_class = views.UserView

        req = self.factory.delete(
            '/api/user/?pk=' + str(self.user.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)


class SeminarViewCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            first_name='philipp', last_name='hafner')
        self.seminar = Seminar.objects.create(
            title='Computer Programming',
            description='Programming is fun',
        )
        self.seminar.users.add(self.user)

    def test_get(self):
        status_code = 200
        view_class = views.SeminarView

        req = self.factory.get('/api/seminar/')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_post(self):
        status_code = 201
        view_class = views.SeminarView

        data = {'title':'Computer Information',
                'description':'Computer Information and their impact in our society',
                'users': list(str(self.user.id))}
        req = self.factory.post('/api/seminar/', data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_put(self):
        status_code = 200
        view_class = views.SeminarView

        data = {'title': 'Computer Information',
                'description': 'Computer Information and their impact in our society',
                'users': list(str(self.user.id))}
        req = self.factory.put(
            '/api/seminar/?pk=' + str(self.seminar.id), data=data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_delete(self):
        status_code = 204
        view_class = views.SeminarView

        req = self.factory.delete(
            '/api/seminar/?pk=' + str(self.seminar.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)