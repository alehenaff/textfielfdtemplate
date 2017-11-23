from django.test import TestCase
from templatefield.models import TextFieldTemplate, Substitution
from templatefield.filters import simplesubstitution

# Create your tests here.
class TextFieldTemplateTest(TestCase):
    def setUp(self):
        TextFieldTemplate.objects.create(template='Bonjour {{client.name}}, {{client.address}}',
        context='{"client":{"name":"toto","address":"Paris"}}')
        TextFieldTemplate.objects.create(template='{{domaine.name|simplesubstitution("aerodom")}}',
        context='{"domaine":{"name":"atlantique"}}')
        Substitution.objects.create(name='aerodom',key='atlantique',value='z')
    
    def test_simple_render(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.rendertemplate(),'Bonjour toto, Paris')
    
    def test_jinja_render(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.rendertemplatejinja(),'Bonjour toto, Paris')

    def test_undefined_variables(self):
        a = TextFieldTemplate.objects.first()
        self.assertEqual(a.get_undefined_variables(),{'client'})

    def test_filter(self):
        a = TextFieldTemplate.objects.last()
        self.assertEqual(a.rendertemplatejinja(filters=[('simplesubstitution',simplesubstitution)]),'z')
