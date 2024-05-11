from typing import Any
from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    number = forms.CharField(max_length=12)
    password = forms.CharField(max_length=50)

    def clean(self) -> dict[str, Any]:
        cd = self.cleaned_data
        if len(cd.get("password")) < 8:
            raise ValueError("password is less than 8")
        if len(cd.get("number")) != 11 or cd.get("number")[0:2] != "09":
            raise ValueError("invalid number")
        print("clean i'm here")
        return super().clean()