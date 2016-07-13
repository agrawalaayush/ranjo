'''
Created on 13-Jul-2016

@author: aayush.agrawal
'''
from django.test import TestCase
from models import Student
from django.core.urlresolvers import reverse
class StudentTests(TestCase):
    def test_check_unique(self):
        stud = Student(name='Aayush',roll_no=1)
        stud.save()
        self.assertEqual((stud.roll_no==1),True)
    
class LoginViewTests(TestCase):
    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        