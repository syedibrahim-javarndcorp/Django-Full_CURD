from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"#['productname', 'price','vendor','quantity','waranty']

    # def __init__(self,*args,**kwargs):
    #     super(ProductForm,self).__init__(*args,**kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class' : 'input'})

class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }

        # def __init__(self,*args,**kwargs):
        #     super(CustomUser,self).__init__(*args,**kwargs)

        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class' : 'input'})