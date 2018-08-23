{% set labels=[] %}
{% for input in data["inputs"] %}
  {% do labels.append(input['label']) %}
{% endfor %}

rb=wg.RadioButtons(
    options={{ labels }},
    description='N/A',
    disabled=False
)
display(rb)
