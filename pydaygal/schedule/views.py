# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
# from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404

from pydaygal.speakers.models import Speaker

class ScheduleView(View):
    """Conference program."""

    @staticmethod
    def get(request):
        speakers = Speaker.objects.requested_objects(request)
        return render(request, "pages/schedule.html", {"speakers": speakers})
