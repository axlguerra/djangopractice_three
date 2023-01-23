from enum import unique
from operator import le
from tkinter.messagebox import NO
from wsgiref.validate import validator
from django.forms import ModelForm
from django import forms
from django.core import validators



# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME NEEDS TO START WITH Z')

class FormForm(forms.Form):
    # name = forms.CharField(max_length=200, validators=[check_for_z])
    name = forms.CharField(max_length=200)

    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again ')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])




    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure email match!')


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #          print('GOTCHA')
    #          raise forms.ValidationError ('test')
        
    #     return botcatcher


