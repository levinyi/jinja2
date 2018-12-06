'''
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('yourapplication','templates'))

template = env.get_template('mytemplate.html')
print(template.render(the='variables',go='here'))
'''
import os
import jinja2

def render(tpl_path,**kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)

def test_simple():
    title = "Title H   "
    items = [{'href':'a.com','caption':'ACaption'},{'href':'b.com','caption':'Bcaption'}]
    content = "this is content"
    result = render('3.1.simple.html',**locals())
    print(result)
if __name__ == '__main__':
    test_simple()
