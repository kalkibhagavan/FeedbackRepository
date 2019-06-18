from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'feedback'
            }
        )
    )