from django import forms

class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        label="Enter userName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'userName',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter mobile number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'mobile number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':"Enter email-id",
                'class':'form-control'
            }
        )
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter userName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'userName',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'form-control'
            }
        )
    )


























