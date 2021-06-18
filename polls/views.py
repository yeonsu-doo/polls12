from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate, Poll, Choice
import datetime


def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'polls/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달

def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(area = area, startdate__lte=today, enddate__gte=today)
        candidates = Candidate.objects.filter(area=area)
    except:
        poll = None
        candidates = None
    context = {'candidates': candidates,
    'area': area,
    'poll': poll}
    return render(request, 'polls/area.html', context)