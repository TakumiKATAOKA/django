from django.shortcuts import render,redirect,get_object_or_404
from .forms import DayCreateForm
from .models import Day

def index(request):
  context={
    'day_list':Day.objects.all(),
  }
  return render(request,'diary/day_list.html',context)

def add(request):
  #送信の内容を基にフォームを作る。postじゃなければ空に
  form=DayCreateForm(request.POST or None)
#送信ボタンを押したとき、入力内容に問題がなければ保存
  if request.method=="POST" and form.is_valid():
    form.save()
    return redirect('diary:index')
#通常のアクセスや、入力ないように誤りがあればまたページを表示
  context={
  'form': form
  }
  return render(request,'diary/day_form.html',context)
# Create your views here.


def update(request,pk):
  day=get_object_or_404(Day,pk=pk)

  form=DayCreateForm(request.POST or None,instance=day)
#送信ボタンを押したとき、入力内容に問題がなければ保存
  if request.method=="POST" and form.is_valid():
    form.save()
    return redirect('diary:index')
#通常のアクセスや、入力ないように誤りがあればまたページを表示
  context={
  'form': form
  }
  return render(request,'diary/day_form.html',context)

def delete(request,pk):
  day=get_object_or_404(Day,pk=pk)


#送信ボタンを押したとき、入力内容に問題がなければ保存
  if request.method=="POST":
    day.delete()
    return redirect('diary:index')
#通常のアクセスや、入力ないように誤りがあればまたページを表示
  context={
  'day':day,
  }
  return render(request,'diary/day_confirm_delete.html',context)

def detail(request,pk):
  day=get_object_or_404(Day,pk=pk)

#通常のアクセスや、入力ないように誤りがあればまたページを表示
  context={
  'day':day,
  }
  return render(request,'diary/day_detail.html',context)
