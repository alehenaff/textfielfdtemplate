from templatefield.models import Substitution
def simplesubstitution(value,substitution):
    if Substitution.objects.filter(name=substitution, key=value).exists():
        r = Substitution.objects.get(name=substitution, key=value)
        return r.value
