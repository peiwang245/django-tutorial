# Create your tests here.
# from django.urls import reverse
# from django.test import TestCase
# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)

from django.urls import  reverse, resolve
from django.test import TestCase
from .views import home


class HomeTests(TestCase):
    # def test_home_view_status_code(self):
    #     url = reverse('home')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
        #Django使⽤resolve来将浏览器发起请求的URL与urls.py模块中列出的URL进⾏匹配
