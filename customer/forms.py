from django import forms

from customer.models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ['num_ref', 'lastname', 'firstname', 'age', "phone", "email", "customer_type", "image"]