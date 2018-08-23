{% set options=[i["label"] for i in data["inputs"]] %}

wg.RadioButtons(
    options={{ options }},
    description='N/A',
    disabled=False
)

myName = wg.Text(value='Name')
myAge = wg.IntSlider(description='Age:')
display(myName,myAge)

### new cell
print(myName.value + ' is ' + str(myAge.value) + ' years old')
