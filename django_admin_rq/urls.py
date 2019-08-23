# -*- coding: utf-8 -*-
from django.urls import path
from django_admin_rq import views

urlpatterns = [
    path('job/status/<string:job_uuid>/', views.JobStatusView.as_view(), name='admin-rq-job-status'),
]
