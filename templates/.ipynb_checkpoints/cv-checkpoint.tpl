{% extends "base.html" %}
{% block head %}
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Tim Sainburg: Curriculum Vitae</title>
<link rel="stylesheet" type="text/css" href="../assets/css/cv.css">
{% endblock %}

{% block content %}
<div id="cv_div">
<h1 id="name">Tim Sainburg</h1> &nbsp; <span class="docname"><a href="mailto:timsainb@gmail.com">Curriculum Vit&aelig;</span>

<div class="vline"></div>

<div id="contactinfo">
    <span class="contact_details">Email: </span><a href="mailto:timsainb@gmail.com">timsainb@gmail.com</a>
    <br />
    <span class="contact_details">Phone: </span>814-574-7780
    <br />
    <span class="contact_details">Website: </span><a href="http://timsainburg.com">http://timsainburg.com</a>
    <br />
    <span class="contact_details">Github: </span><a href="http://github.com/timsainb">github.com/timsainb</a>
    <br />
</div> 
<div id="address">
    9500 Gilman Drive    <br />            
    Department of Psychology         <br /> 
    UC San Diego <br />
    La Jolla, CA  92093-0109 USA <br />
</div>
{{ super() }}
{% endblock %}


