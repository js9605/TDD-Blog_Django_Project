from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegistrationForm


class AccountCreation(TestCase):
    def setUp(self) -> None:
        self.form_class = UserRegistrationForm
    
    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, "Create Your account today")

    def test_signup_form_works(self):        
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            "email": "testuser@app.com",
            "username": "testuser",
            "password1" : "p4sword123###",
            "password2" : "p4sword123###" 
        }

        form = self.form_class(sample_data)

        self.assertTrue(form.is_valid())