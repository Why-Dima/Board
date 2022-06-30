from django.forms import ModelForm
from .models import Ads, Reactions


class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'


class ReactionsForms(ModelForm):
    class Meta:
        model = Reactions
        fields = ['reaction', ]

