from django.db import models
from django.template import Template, Context
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
