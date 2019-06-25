{% extends "base.html" %}

{% block head %}
<title>Curriculum Vitae</title>
<meta name="date" content="2012-07-09 22:28" />
<meta name="category" content="pages" />
<meta name="authors" content="Tim Sainburg" />
<meta name="slug" content="cv" />
<meta name="summary" content="My Academic Curriculum Vitae" />
{% endblock %}

{% block content %}

<link rel="stylesheet" type="text/css" href="../assets/css/cv.css">
<a id="printlink" href="../curriculumvitae.html">Print Version</a>
<div id="cv_div">
<div class="vline"></div>

<div class="vline"></div>

{{ super() }}

{% endblock %}

