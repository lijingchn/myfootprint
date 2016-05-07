#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
        url(r'^$', 'intro.views.first_page'),
        url(r'^introduction_template/', 'intro.views.introduction_template'),
        url(r'^footprint_template/', 'intro.views.footprint_template'),
        url(r'^form/', 'intro.views.form'),
        url(r'^handle_form/', 'intro.views.handle_form'),
        url(r'^investigate/', 'intro.views.investigate'),
        url(r'^investigate_handle/', 'intro.views.investigate_handle'),
)

