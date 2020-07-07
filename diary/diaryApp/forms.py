from django.forms import ModelForm
from .models import DiaryEntry


class DataEntryForm(ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
