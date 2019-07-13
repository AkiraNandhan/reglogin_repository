from django import forms

class EmpForm(forms.Form):
    ename=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your Name',
                'class':'form-control'
            }
        )
    )

    sal=forms.IntegerField(
        label="Enter your Salary",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your Salary',
                'class':'form-control'
            }
        )

    )

    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'your Email',
                'class':'form-control'
            }
        )
    )

    loc=forms.CharField(
        label="Enter your location",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your LOcation',
                'class':'form-control'
            }
        )
    )












