from django.test import TestCase
from templatefield.models import TextFieldTemplate

# Create your tests here.
class TextFieldTemplateTest(TestCase):
    def setUp(self):
        TextFieldTemplate.objects.create(template='Bonjour {{client.name}}, {{client.address}}',
        context='{"client":{"name":"toto","address":"Paris"}}')
    
    def test_simple_render(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.rendertemplate(),'Bonjour toto, Paris')
    
    def test_jinja_render(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.rendertemplate(),'Bonjour toto, Paris')

    def test_undefined_variables(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.get_undefined_variables(),{'client'})

