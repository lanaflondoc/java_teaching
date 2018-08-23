{% set script_id=range(1, 100000) | random %}
{% set labels=[] %}
{% set truth=[] %}
{% for input in data["inputs"] %}
  {% do labels.append(input['label']) %}

  {% if input['value']=="True" or input['value']=="true" or input['value']==True %}
    {% do truth.append(input['label']) %}

  {% endif %}
{% endfor %}

title{{script_id}}=wg.HTML(
    value="<h2>{{data["title"]}}</h2>"

)

rb{{script_id}}=wg.RadioButtons(
    options={{ labels }},
    description='',
    disabled=False
)

text{{script_id}}=wg.Textarea(
    value='',
    placeholder='',
    description='String:',
    disabled=True
)



validate{{script_id}} = wg.Button(description="Valider")

def on_success{{script_id}}(button,item):
    button.button_style='success'
    text{{script_id}}.value=item['hint']


def on_failure{{script_id}}(button,item):
    button.button_style='danger'
    text{{script_id}}.value=item['hint']

def on_button_clicked{{script_id}}(button):
    {% for item in data["inputs"] %}
    if "{{item["label"]}}"==rb{{script_id}}.value:
        item={{item}}
    {% endfor %}
    if rb{{script_id}}.value=="{{truth[0]}}":
        on_success{{script_id}}(button,item)
    else:
        on_failure{{script_id}}(button,item)

validate{{script_id}}.on_click(on_button_clicked{{script_id}})

display(title{{script_id}},rb{{script_id}},validate{{script_id}},text{{script_id}})
