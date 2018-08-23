from jinja2 import Environment, BaseLoader, select_autoescape,TemplateNotFound
import os
import codecs
import yaml

class WidgetLoader(BaseLoader):
    def __init__(self, path):
        self.path = path
    def get_source(self, environment, type):
        path = os.path.join(self.path, type,"template.py.tpl")
        if not os.path.exists(path):
            raise TemplateNotFound(type)
        mtime = os.path.getmtime(path)
        with  codecs.open(path, "r", "utf-8")  as f:
            source = f.read()
        return source, path, lambda: mtime == os.path.getmtime(path)



env = Environment(
    loader=WidgetLoader('templates'),
    autoescape=select_autoescape(['html', 'xml']),
    extensions=['jinja2.ext.do']
)


def render_quiz(quiz_data):
    return env.get_template(quiz_data["type"]).render(data=quiz_data)
