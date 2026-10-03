from django.test import RequestFactory, TestCase

from .views import home


class HomeViewTests(TestCase):
    def test_home_passes_students_to_template(self):
        request = RequestFactory().get('/')
        response = home(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('students', response.context_data)
