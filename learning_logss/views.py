# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logss/index.html')