from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Alliance, Choice, Question


class AllianceIndexView(generic.ListView):
    template_name = 'alliance/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Alliance.objects.order_by('-pub_date')[:5]


class AllianceDetailView(generic.DetailView):
    model = Alliance
    template_name = 'polls/detail.html'


class AllianceResultsView(generic.DetailView):
    model = Alliance
    template_name = 'polls/results.html'
