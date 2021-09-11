from django.shortcuts import render,redirect,get_object_or_404
from .models import Entry, Topic
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    """home page"""
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """topic page list all topics"""

    topics = Topic.objects.filter(owner = request.user).order_by('date_added')

    context ={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """shows some specifi topic"""
    topic = get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        # no data submitted; create a blank file
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit= False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    
    #display blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """allow users to add entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted; create a blank form
        form = EntryForm()
    else:
        #post data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id = topic_id)
    # display a blank or invaild form
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # intial request prefileed form with existing entry
        form = EntryForm(instance=entry)
    else:
        #post data submitted; process data.
        form= EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

