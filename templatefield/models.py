from django.db import models
from django.template import Template, Context
from django.template.base import VariableNode
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
        except:
            return("env error")
        try:
            parsed_context = env.parse(self.template)
            return meta.find_undeclared_variables(parsed_context)
        except:
            return("parse error")

    def rendertemplatejinja(self):
        try:
            t=jinja2.Template(self.template)
            try: 
                c=Context(json.loads(self.context))
                return t.render(c)
            except:
                return("context error")
        except:
            return("error")

