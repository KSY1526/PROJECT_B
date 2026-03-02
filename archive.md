---
layout: default
title: "아카이브"
permalink: /archive/
---

<div class="archive">
  <h1>아카이브</h1>

  {% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  {% for year in postsByYear %}
  <section class="archive-year">
    <h2>{{ year.name }}</h2>
    <ul class="archive-list">
      {% for post in year.items %}
      <li>
        <time>{{ post.date | date: "%m. %d" }}</time>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% for tag in post.tags %}
        <a href="#{{ tag }}" class="tag">{{ tag }}</a>
        {% endfor %}
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}

  {% assign allTags = site.posts | map: "tags" | flatten | uniq | sort %}
  {% if allTags.size > 0 %}
  <section class="archive-tags">
    <h2>태그</h2>
    <div class="tag-cloud">
      {% for tag in allTags %}
      <a href="#{{ tag }}" class="tag" id="{{ tag }}">{{ tag }}</a>
      {% endfor %}
    </div>
  </section>
  {% endif %}
</div>
