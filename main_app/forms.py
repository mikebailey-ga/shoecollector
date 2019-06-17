from django.forms import ModelForm
from .models import Wearings

class WearingsForm(ModelForm):
    class Meta:
        model = Wearings
        fields = ['date','fly']