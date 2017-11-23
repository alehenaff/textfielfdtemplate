from django.db import models
from django.template import Template, Context
from django.template.base import VariableNode
import jinja2
from jinja2 import Environment, meta
import json

# Create your models here.
class TextFieldTemplate(models.Model):
    template = models.TextField()
    context = models.TextField() #JSONField

    def rendertemplate(self):
        try:
            t=Template(self.template)
            try:
                c=Context(json.loads(self.context))
                return t.render(c)
            except:
                return("context error")
        except:
            return("error")

    def get_variable_nodes(self):
        try:
            t=Template(self.template)
            return t.nodelist.get_nodes_by_type(VariableNode)
        except:
            return("error")

    def get_undefined_variables(self):
        try:
            env = Environment()
            parsed_context = env.parse(self.template)
            return meta.find_undeclared_variables(parsed_context)
        except Exception as ex:
            return(ex)

    def rendertemplatejinja(self, filters= None):
        try:
            e = jinja2.Environment()
            if filters:
                for filtername, filter in filters:
                    e.filters[filtername]=filter
            tem = e.from_string(self.template)    
            return tem.render(json.loads(self.context))
        except Exception as ex:
            return(ex)

class Substitution(models.Model):
    name = models.CharField(max_length=70)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    class Meta:
        unique_together = (('name','key','value'))