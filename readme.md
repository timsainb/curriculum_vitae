### Tim Sainburg Curriculum Vitae 
This repo makes an HTML Curriculum Vitae (CV) from a set of json files. It is [based on Colin Raffel's CV](https://github.com/craffel/craffel.github.io)

## Usage
If all you want to do is generate an HTML file, just run `python3 generate.py`. It will look inside of templates, and generate HTML using Jinja from those templates and the related JSON files (inside of data).

For my own specific uses, I created a Makefile, that will need to be re-created specifically for your use case. That file is just used to do things like git push the updated CV repo, copy files over to my websites repo, build that repo, and push it it github. To run the makefile, just run `make buildwebsite` or another make command. 


### Quick explanation

Data is stored in a JSON, like this:
```
{"research":
    [
        
        {
            "Organization": "University of California, San Diego",
            "lab": "Auditory Neurscience Laboratory",
            "location": "La Jolla, CA",
            "advisor": "Timothy Q Gentner",
            "start": "2015",
            "end": "now",
            "title": "PhD Student"
        }
    ]
}
```

The `.tpl` Jinja template for the HTML output, is generated using the JSON data, like this:

```
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <title>Tim Sainburg: Curriculum Vitae</title>
    </head>
    <body>
        <h2>Education</h2>
        <div class="block">
            {% for item in education %}
            <div class="item">
                <div class="yearrange">{{item.start}}&#8211;{{item.end}}</div>
                <div class="yearright">
                    <strong>{{item.place}}</strong><br />
                    {{item.degree}}<br />
                    {% if item.lab %}{{item.lab}}<br />{% endif %}
                    {% if item.advisor %}Advisor: {{item.advisor}}<br />{% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
    </body>
</html>
```

This is all orchestrated by the `generate.py` script, which just finds all of the json files, loads them up, generates the HTML from .tpl, and writes it to a file:

```
env = jinja2.environment.Environment(
    loader=jinja2.FileSystemLoader('/MY/TEMPLATE/PATH')
)
template = env.get_template('MYTEMPLATE.TPL')
with open('/MY/OUTPUT/PATH/MYTEMPLATE.HTML', "w") as f:
    f.write(template.render(**data))
```  



