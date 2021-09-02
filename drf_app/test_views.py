from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from . import views
from .models import User, Seminar, Section, SubSection


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


class SectionViewCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            first_name='philipp', last_name='hafner')
        self.seminar = Seminar.objects.create(
            title='Computer Programming',
            description='Programming is fun',
        )
        self.seminar.users.add(self.user)
        self.section = Section.objects.create(
            title='Python',
            description='Basics of Python',
            seminar=self.seminar
        )

    def test_get(self):
        status_code = 200
        view_class = views.SectionView
        req = self.factory.get(
            '/api/section/?seminar_id=' + str(self.seminar.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_post(self):
        status_code = 201
        view_class = views.SectionView
        data = {'title': 'Java', 'description': 'Basics of Java',
                'seminar': str(self.seminar.id)}
        req = self.factory.post(
            '/api/section/', data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_put(self):
        status_code = 200
        view_class = views.SectionView
        data = {'title': 'Swift4', 'description': 'Basics of Swift4',
                'seminar': str(self.seminar.id)}
        req = self.factory.put(
            '/api/section/?pk=' + str(self.section.id), data=data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_delete(self):
        status_code = 204
        view_class = views.SectionView

        req = self.factory.delete(
            '/api/section/?pk=' + str(self.section.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)


class SubsectionViewCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            first_name='philipp', last_name='hafner')
        self.seminar = Seminar.objects.create(
            title='Computer Programming',
            description='Programming is fun',
        )
        self.seminar.users.add(self.user)
        self.section = Section.objects.create(
            title='Python',
            description='Basics of Python',
            seminar=self.seminar
        )
        self.subsection = SubSection.objects.create(
            content_type='TXT',
            content='Hello World!',
            section=self.section
        )

    def test_get(self):
        status_code = 200
        view_class = views.SubsectionView
        req = self.factory.get(
            '/api/subsection/?section_id=' + str(self.section.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_post(self):
        status_code = 201
        view_class = views.SubsectionView
        data = {'content_type': 'VID', 'content': 'youtube.com',
                'section': str(self.section.id)}
        req = self.factory.post(
            '/api/subsection/', data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_put(self):
        status_code = 200
        view_class = views.SubsectionView
        data = {'content_type': 'TXT', 'content': 'Hello World',
                'section': str(self.section.id)}
        req = self.factory.put(
            '/api/subsection/?pk=' + str(self.subsection.id),
            data=data, content_type='application/json')
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)

    def test_delete(self):
        status_code = 204
        view_class = views.SubsectionView

        req = self.factory.delete(
            '/api/subsection/?pk=' + str(self.subsection.id))
        resp = view_class.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, status_code)