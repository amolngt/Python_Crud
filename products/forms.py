from django import forms
from products.models import Products


class ProductsForm(forms.Form):
    product_name = forms.CharField(required=False)
    product_type = forms.CharField(required=False)
    quantity = forms.IntegerField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("proname")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
