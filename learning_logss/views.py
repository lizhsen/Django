# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logss/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logss/topics.html', context)


def topic(request,topic_id):
    """显示单个主题以及所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logss/topic.html', context)

