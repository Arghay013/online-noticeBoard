from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice

def index(request):
    notices = sorted(Notice.objects.all(), key=lambda notice: notice.title)
    
    return render(request, 'noticelist/index.html', {'notices': notices})

def add_notice(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Notice.objects.create(title=title, content=content)
    return redirect('index')

def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)

    if request.method == 'POST':
        notice.delete()
        return redirect('index')

    return render(request, 'noticelist/delete_notice.html', {'notice': notice})