from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):
#inputタグを書いて書くのが面倒、ユーザーの書いたテータが正しいとは限らない
  class Meta:
    model= Day
    fields='__all__'
