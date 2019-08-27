#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

from django.shortcuts import render
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup

class OrderView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/adm_index.html', ret)


class OrderInView(LoginRequiredMixin, View):
    """
    入场
    """
    def get(self, request):
        pass

    def post(self, request):
        pass

class OrderOutView(LoginRequiredMixin, View):
    """
    出场
    """
    def get(self, request):
        pass

    def post(self, request):
        pass