from django import forms

class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Introduce the URL'}), label=False)
