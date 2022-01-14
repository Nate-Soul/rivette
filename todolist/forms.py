from django import forms

class TodoForm(forms.Form):
    task_input = forms.CharField(max_length=55,
                                widget = forms.TextInput({
                                    'id': 'task_field',
                                    'class': 'form-control',
                                    'placeholder': 'Enter new task'
                                }))