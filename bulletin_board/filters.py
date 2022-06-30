from django_filters import FilterSet
from .models import *


class ReactionsFilter(FilterSet):
    class Meta:
        pass
        model = Reactions
        fields = ('ads',)
