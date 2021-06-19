from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Candidate, Poll, Choice
import datetime


def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}  # context에 모든 후보에 대한 정보를 저장
    return render(request, 'polls/index.html', context)  # context로 html에 모든 후보에 대한 정보를 전달


def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(area=area, startdate__lte=today, enddate__gte=today)
        candidates = Candidate.objects.filter(area=area)
    except:
        poll = None
        candidates = None
    context = {'candidates': candidates,
               'area': area,
               'poll': poll}
    return render(request, 'polls/area.html', context)


def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']

    try:
        choice = Choice.objects.get(poll_id=poll.id, candidate_id=selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id=poll.id, candidate_id=selection, votes=1)
        choice.save()

    return HttpResponse("투표가 완료되었습니다. 결과는 투표 종료 후에 공지하겠습니다.")

