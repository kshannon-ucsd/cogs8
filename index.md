---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Overview
layout: default
nav_exclude: false
nav_order: 1
---

{% assign variables = site.data[site.data_folder].variables %}
{% assign course_calendar = site.data[site.data_folder].course_calendar %}

{: .text-grey-dk-200 .lh-0 .pt-4 }
# Hands on Computing

{: .text-grey-dk-300 .fw-300 .lh-0 }
## COGS 8 - UC San Diego - Prof. Kyle Shannon 

{{ variables.quarter }}
{: .md-badge-purple }

{{ variables.building }}
{: .md-badge-purple }

{{ variables.timings }}
{: .md-badge-purple }


## Welcome <span title="https://jarv.is/" class="wave">👋</span> 

We are all very excited that you decided to join us on this introduction to computing, robotics, data, and cognitive science. All relevant info, e.g. due dates, assignment links, etc. are found on this website.
We look forward to teaching and working with all of you and hope to meet you in office hours. Check out the getting started section so you can hit the ground running when class starts!
{: .fs-3 }

{: .note .fs-2 }
Week one I try to take as many students from the **waitlist** as I can, please email [{{ variables.cogsadvising }}](mailto:{{ variables.cogsadvising }}) with further questions.

## Discussion Section Times

<table style="table-layout: fixed; text-align: center; width: 100%;">
    <thead>
        <tr class="header">
            <th style="width: 10%;"></th>
            <th style="width: 10%;"> Day </th>
            <th style="width: 25%;"> Time </th>
            <th style="width: 15%;"> Location </th>
            <th style="width: 25%;"> Staff </th>
            <th style="width: 15%;"> Materials </th>
        </tr>
    </thead>
    <tbody>
        {% for ds in variables.discussion_sections %}
        <tr>
            <td> {{ ds.section }} </td>
            <td> {{ ds.day }} </td>
            <td> {{ ds.time }} </td>
            <td> {{ ds.location }} </td>
            <td> {{ ds.ta }}, {{ ds.ia }} </td>
            <td> <a href="{{ ds.materials }}"> view </a> </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

## Course Calander

{% assign first_date = course_calendar[0].date | date: '%s' %}
{% assign first_day = course_calendar[0].date | date: '%w' %}
{% assign prev_week_no = 0 %}
<table style="table-layout: fixed; text-align: left; width: 100%;">
    <colspan>
        <col style="width: 25%;">
        <col style="width: 10%; border: none">
        <col style="width: 65%; border: none">
    </colspan>
    <thead>
        <tr class="header">
            <th colspan="3" style="padding-left:8%; font-size-adjust:0.75"> Week 0 </th>
        </tr>
    </thead>
    <tbody>
{% for row in course_calendar %}
    {% assign week_no = row.date | date: '%s' | minus: first_date | divided_by: 60 | divided_by: 60 | divided_by: 24 | plus: first_day | divided_by: 7 | plus: 1 %}
    {% if week_no != prev_week_no %}
    </tbody>
</table>
<table style="table-layout: fixed; text-align: left; width: 100%;">
    <colspan>
        <col style="width: 25%;">
        <col style="width: 10%; border: none">
        <col style="width: 65%; border: none">
    </colspan>
    <thead>
        <tr class="header">
            <th colspan="3" style="padding-left:8%; font-size-adjust:0.75"> Week {{ week_no }} </th>
        </tr>
    </thead>
    <tbody>
    {% endif %}
    {% assign prev_week_no = week_no %}
        <tr>
            <td style="text-align: center"> {{ row.date | date: "%a, %b %d" }} </td>
            <td style="text-align: center">
              {% if row.label == "LECT" %} <span class="md-cal-badge md-cal-badge-blue"> {{ row.label }} </span>
              {% elsif row.label == "GLCT" %} <span class="md-cal-badge md-cal-badge-purple"> {{ row.label }} </span>
              {% elsif row.label == "CNCL" %} <span class="md-cal-badge md-cal-badge-red"> {{ row.label }} </span>
              {% elsif row.label == "ASSG" %} <span class="md-cal-badge md-cal-badge-green"> {{ row.label }} </span>
              {% elsif row.label == "EXAM" %} <span class="md-cal-badge md-cal-badge-gray"> {{ row.label }} </span>
              {% elsif row.label == "QUIZ" %} <span class="md-cal-badge md-cal-badge-green"> {{ row.label }} </span>
              {% elsif row.label == "DISC" %} <span class="md-cal-badge md-cal-badge-yellow"> {{ row.label }} </span>
              {% else %}
                {% if row.label %} <span class="md-cal-badge md-cal-badge-black"> {{ row.label }} </span>
                {% endif %}
              {% endif %}
            </td>
            <td style="padding-left: 4%"> {% if row.link %} <a href="{{ row.link }}"> {{ row.title }} </a> {% else %} {{ row.title }} {% endif %} </td>
        </tr>
{% endfor %}
    </tbody>
</table>
