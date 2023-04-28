---
layout: default
title: Staff Information
has_children: false
nav_order: 9
permalink: /staff-info/
---

{% assign variables = site.data[site.data_folder].variables %}
{% assign course_calendar = site.data[site.data_folder].course_calendar %}

# Staff Information

## Contact Info

**Instructor** <br/> {{ variables.instructor.name }} - [{{ variables.instructor.email }}](mailto:{{ variables.instructor.email }})

**Teaching Assistants (TAs)**
{% for ta in variables.teaching_assistants %} <br/> {{ ta.name }} - [{{ ta.email }}](mailto:{{ ta.email }}) {% endfor %}

**Instructional Assistants (IAs)**
{% for ia in variables.instructional_assistants %} <br/> {{ ia.name }} - [{{ ia.email }}](mailto:{{ ia.email }}) {% endfor %}
<!-- {: .fs-3 } -->

## Office Hours & Zoom Info

Office hours are a great place to personally interact. Beyond projects and course material, we are interested in your goals, career endeavors, and what you want to gain from COGS 8. 

<table style="table-layout: fixed; text-align: center; width: 100%;">
    <thead>
        <tr class="header">
            <th style="width: 25%;"> Staff </th>
            <th style="width: 25%;"> Day & Time </th>
            <th style="width: 25%;"> Location </th>
            <th style="width: 12.5%;"> Link </th>
            <th style="width: 12.5%;"> Pass </th>
        </tr>
    </thead>
    <tbody>
        {% for oh in variables.instructor.office_hours %}
        <tr>
            <td> {{ variables.instructor.name }} </td>
            <td> {{ oh.day }} {{ oh.time }} </td>
            <td> {{ oh.location }} </td>
            <td> <a href='{{ oh.zoom_link }}' target="_blank" rel="noopener">Join &#x2197;</a> </td>
            <td> {% if oh.zoom_pw %} {{ oh.zoom_pw }} {% endif %} </td>
        </tr>
        {% endfor %}
        {% for row in variables.teaching_assistants %}
            {% for oh in row.office_hours %}
            <tr>
                <td> {{ row.name }} </td>
                <td> {{ oh.day }} {{ oh.time }} </td>
                <td> {{ oh.location }} </td>
                <td> <a href='{{ oh.zoom_link }}' target="_blank" rel="noopener">Join &#x2197;</a> </td>
                <td> {% if oh.zoom_pw %} {{ oh.zoom_pw }} {% endif %} </td>
            </tr>
            {% endfor %}
        {% endfor %}
        {% for row in variables.instructional_assistants %}
            {% for oh in row.office_hours %}
            <tr>
                <td> {{ row.name }} </td>
                <td> {{ oh.day }} {{ oh.time }} </td>
                <td> {{ oh.location }} </td>
                <td> <a href='{{ oh.zoom_link }}' target="_blank" rel="noopener">Join &#x2197;</a> </td>
                <td> {% if oh.zoom_pw %} {{ oh.zoom_pw }} {% endif %} </td>
            </tr>
            {% endfor %}
        {% endfor %}
    </tbody>
</table>

{: .note .fs-3 }
If you are unable to join or are having other issues, please reach out after class (I tend to do impromptu office hours after each class if I have time). Additionally, we are more than happy, to set up additional 1:1 or 1:group meetings when necessary.
