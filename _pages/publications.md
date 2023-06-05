---
layout: page
permalink: /publications/
title: publications
description: Publications in reversed chronological order by date of preprint.
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

All of my papers are available on the <a href="https://arxiv.org/a/flammia_s_1.html">arXiv</a> and on my <a href="https://scholar.google.com/citations?user=-VnX0xYAAAAJ">Google Scholar</a> page. 

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} -q @*[]* %}


</div>
