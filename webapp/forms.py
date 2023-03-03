from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.SelectMultiple)
        status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), widget=forms.RadioSelect)
        fields = {'description', 'detailed_description', 'status', 'type'}
        labels = {
            'description': 'Описание',
            'detailed_description': 'Подробно',
            'status': 'Статус',
            'type': 'Тип',
        }
        widgets = {
            'status': forms.RadioSelect,
            'type': forms.SelectMultiple
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 2:
            raise ValidationError('Описание должно быть длиннее 2 символов!')
        return description
