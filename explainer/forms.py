from django import forms

class CodeForm(forms.Form):
    code_snippet = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        label='Paste your code here'
    )
