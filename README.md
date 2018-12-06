
# 1.模版介绍

这里将会介绍在python的web开发中广泛使用的模版语言jinja2.模版在web开发中使用最为广泛，但是模版的使用并不仅限于web开发，适合所有基于文本的格式，因此系统管理员和开发工程师也经常使用模版来管理配置文件。模版在python的web开发中广泛使用。他能够有效的将业务逻辑和页面逻辑分离，使得工程师编写出可读性更好，更加容易理解和维护的代码。试想一下，要为一个大型的表格构建HTML代码，表格中的数据由数据库中读取的数据以及必要的HTML字符串连接在一起。这个时候，最简单也最直接的方式就是在Python代码中使用字符串拼接的方式生成HTML代码。如果真的这么做了，对工程师来说将是个噩梦，而且代码无法维护。此时，可以使用模版将业务逻辑与页面逻辑分隔开来。
#2. Jinja2语法入门

Jinja2是Flask作者开发的一个模版系统，期初是仿Django模版的一个模版引擎，为Flask提供模版支持。但是，由于其灵活、快速和安全等优点被广泛使用。补充资料：Flask是一个使用python编写的轻量级web应用框架，本来只是作者的一个愚人节玩笑，不过发布后大受欢迎，进而成为一个正式的项目。Flask是python生态中最流行的web框架之一，本身的代码也写的非常优雅，所以有不少python工程师学习Flask的源码。Jinja2模版引擎之所以使用广泛，是因为它有以下优点：
	* 相对于Template，Jinja2更加灵活，它提供了控制结构、表达式和继承等，工程师可以在模版中做更多的事情；
	* 相对于Mako，Jinja2提供了仅有的控制结构，不允许在模版中编写太多的业务逻辑，避免了工程师乱用行为；
	* 相对于Django模版，Jinja2的性能更好；
	* Jinja2模版的可读性很好。

Jinja2是Flask的一个依赖，如果已经安装 了Flask，Jinja2也会随之安装。当然也可以单独安装Jinja2：
```
pip install jinja2
python -c "import jinja2"
```
2.1. 语法块
jinja2可以应用于任何基于文本的格式，如HTML、XML。大家知道，HTML本身就是超文本标记语言，里面包含了很多HTML标签，那么，如何区分一段本身是jinja2语法还是普通的文本呢？为了进行区分，Jinja2使用大括号的方式表示Jinja2的语法。在Jinja2中，存在3种语法：
	* 控制结构{%%}
	* 变量取值{{}}
	* 注释{##}

下面是使用Jinja2控制结构和注释的一个例子：
```
{# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor%}#}
```
可以看到，for循环的使用与python比较类似，但是没有了复合语句末尾的冒号。此外需要使用endfor作为结束标志。Jinja2中的if语句也一样，没有复合语句末尾的冒号，需要使用endif作为结束标志。如下所示:
```
{% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor%}
    </ul>
{% endif %}
```
2.2 变量
Jinja2模版中使用的{{}}语法表示一个变量，它是一种特殊的占位符，告诉模版引擎这个位置的值在渲染模版时获取。Jinja2识别所有的python数据类型，甚至是一些复杂的类型，如列表、字典和对象等，如下所示：
```
<p> A value from a dictionary: {{ mydict['key'] }}.</p>
<p> A value from a list: {{ mylist[3] }}.</p>
<p> A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p> A value from an object's method: {{ myobj.somemethod() }}.</p>
```
2.3 Jinja2中的过滤器
变量可以通过“过滤器”进行修改，过滤器可以理解为是Jinja2里面的内置函数和字符串处理函数。例如，存在一个名为lower的过滤器，它的作用与字符串对象的lower方法一模一样。常用过滤器：
```
safe     渲染值时不转义
capitalize    把值的首字母转换成大写，其它字母转换成小写
lower    把值转换成小写形式
upper    把值转换成大写形式
title    把值中每个单词的首字母都转换成大写
trim    把值的首位空格去掉
striptags    渲染之前把值中所有的HTML标签都删掉
join    拼接多个值为字符串
replace    替换字符串的值
round    默认对数字进行四舍五入，也可以用参数进行控制
int    把值替换成整型
```
在Jinja2中变量可以通过“过滤器”修改，过滤器与变量用管道|分割。多个过滤器可以链式调用，前一个过滤器的输出会作为后一个过滤器的输入。如下所示：
```
{{ " Hello World" | replace("Hello", "Goodbye") }}
    -> Goodbye World
{{ " Hello World" | replace("Hello", "Goodbye") | upper }}
    -> GOODBYE WORLD
{{ 42.5 | round }}
    -> 43.0
{{ 42.55 |round | int }}
    -> 43
```
2.4 Jinja2的控制结构
Jinja2 中的if语句类似于Python中的if语句，但是，需要使用endif语句作为条件判断的结束。我们可以使用if语句判断一个变量是否定义，是否为空，是否为真值。与Python中的if语句一样，也可以使用elif和else 构建多个分支，如下所示：
```
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny! You bastard!!!
{% esle %}
    Kenny looks okay ---so far
{% endif %}
```
2.5.Jinja2的for循环
Jinja2 中的for语句可用于迭代Python的数据类型，包括列表、元祖和字典。在Jinja中不存在while循环，这也符合了Jinja2的“提供仅有的控制结构，不允许在模版中编写太多的业务逻辑，避免了工程师乱用行为”设计原则。在Jinja2中迭代列表：
```
<h1>Members</h1>
<ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor%}
</ul>
```
在Jinja2中也可以遍历字典：
```
<dl>
    {% for key, value in d.iteritems() %}
        <dt>{{ key }}</dt>
        <dd>{{ value }}</dd>
        {% endfor%}
</dl>
```
除了基本的for 循环使用以外，Jinja2还提供了一些特殊的变量，我们不用定义就可以直接使用这些变量。下面列出了Jinja2循环中可以直接使用的特殊变量。for循环中的特殊变量
```
loop.index    当前循环迭代的次数（从1开始）
loop.index0    当前循环迭代的次数（从0开始）
loop.revindex    到循环结束的次数（从1开始）
loop.revindex0    到循环结束的次数（从0开始）
loop.first    如果是第一次迭代，为True，否则为False
loop.last    如果是最后一次迭代，为True，否则为False
loop.length    序列中的项目数
loop.cycle    在一串序列间取值的辅助函数
```
假设你有一个保存了联系人信息的字典，字典的key是联系人的名字，字典的value是联系人电话。你现在想把联系人的信息以表格的形式显示在HTML页面上。此时，除了姓名和电话以外，你还希望表格的第一列是序号。这个需求如果是在Python代码中实现，将会像下面这样：
```
data = dict(bob=1300000001,lily=1300000002,robin=130000003)
index = 0
for key,value in data.viewitems():
    index +=1
    print(index,key,value,sep=",")
```
Jinja2为了让工程师尽可能在模版中少写Python代码处理业务逻辑，仅在模版中处理显示工作问题，提供了一些特殊变量。对于前面这个例子，在Jinja2中的正确做法如下所示：
```
{% for key,value in data.iteritems() %}
    <tr class='info'>
        <td>{{ loop.index }}</td>
        <td>{{ key }}</td>
        <td>{{ value }}</td>
    </tr>
{% endfor%}
```
2.6.Jinja2的宏
宏类似于编程语言中的函数，它用于将行为抽象成可重复调用的代码块。与函数一样，宏分为定义和调用，下面是一个声明宏的例子：
```
{% macro input(name, type='text', value='') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}
```
在宏的定义中，使用macro关键字定义一个宏，input是宏的名称。他有三个参数，分别是name，type和value，其中type和value参数有默认值。可以看到宏的定义与python的函数定义非常相似，此外，它与Jinja2中的for循环和if语句一样，不需要使用复合语句的冒号，使用endmacro结束宏的定义。下面是宏的调用，与函数调用类似：
```
<p>{{ input('username', value='user') }}</p>
<p>{{ input('password', 'password') }}</p>
<p>{{ input('submit', 'submit', 'Submit') }}</p>
```
2.7.Jinja2的继承和Super函数
如果只是使用Jinja2进行配置文件管理，将基本用不到Jinja2继承功能。如果是使用Jinja2 进行web开发，那么继承是Jinja2最吸引人的功能。Jinja2中最强大的部分就是模版继承。模版继承允许你构建一个包含站点共同元素的基本模版“骨架”，并定义子墨本可以覆盖的块。假设我们有一个名为base.html的HTML文档，里面的内容如下：
```
<html lang="en"><head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %}-My Webpage</title>
    {% endblock %}
</head>
<body>
<div id="content">
    {% block content %}{% endblock %}
</div>
</body>
```
在base.html中，我们使用了{% block name %} 的方式定义了三个块，这些块可以在子模版中进行替换或调用。下面是一个名为index.html的HTML文档，文档的内容如下
```
{% extends "base.html" %}

{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color:#336699; }
    </style>
{% endblock %}

{% block content %}
    <h1>Index</h1>
    <p class="important">Welcome on my awesome homepage. </p>
{% endblock %}
```
在index.html中，我们是用{% extends "base.html" %}继承base.html，继承以后，base.html中的所有内容都会在index.html中展现。在index.html中，我们重新定义了title和content这两个块的内容。2.8.Jinja2的其他运算Jinja2中可以定义变量，为了对变量进行操作，Jinja2提供了算数操作、比较操作和逻辑操作。使用Jinja2模版时，应该尽可能在Python代码中进行逻辑处理，在Jinja2中仅处理显示问题。因此，一般很少用到Jinja2的变量和变量的运算操作。部分Jinja2中的运算操作：
	* 算数运算+-*/ // % * **
	* 比较操作 == ！= > >= < <=
	* 逻辑运算 not and or


#3.Jinja2实战
前面介绍了Jinja2的语法，下面来看两个例子来巩固前面的知识。
Jinja2模块中有个名为Environment的类，这个类的实例用于存储配置和全局对象，然后从文件系统或其他位置加载模版。
大多数应用都在初始化时创建一个Environment对象并用它加载模版。配置Jinja2为应用加载文档的最简单方式大概是这样：
```
from jinja2 import Enviroment, packageLoader
env = Enviroment(loader=PackageLoader('yourapplication','templates'))
```
上面的代码会创建一个Environment对象和一个包加载器，该加载器会在yourapplication这个python包的templates目录下查找模版。接下来，只需要以模版的名字作为参数调用Environment.get_template方法即可。该方法会返回一个模版，最后只用模版的render方法进行渲染，如下所示：
```
template = env.get_template('mytemplate.html')
print(template.render(the='variables',go='here'))
```
除了使用这个包加载器以外，也可以使用文件系统加载器。文件系统加载器不需要模版位于一个python包下，可直接访问系统中的文件。为了便于功能演示，我们将在接下来的例子中使用下面这个辅助函数：
```
import os
import jinja2
def render(tpl_path,**kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Enviroment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)
```
3.1 基本功能演示
下面来看一个模版渲染的例子，假设我们存在一个名为simple.html的文本文件，它的内容如下：
```
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 使用过滤器处理表达式的结果 -->
    <title>{{ title | trim }}</title>
</head>
<body>
    {# This is a Comment #}
    <ul id="navigation">
        {% for item in items %}
            <li><a href="{{ item.href }}">{{ item['caption'] }}</a></li>        
        {% endfor %}
    </ul>
    <p>{{ content }}</p>
</body>
</html>
```
在这个HTML模版中，我们使用for循环遍历一个列表，列表中的每一项是一个字典。字典中包含了文字和连接，我们将使用字典中的数据渲染成HTML的超链接。此外，我们还会使用Jinja2提供的过滤器trim删除title中的空格。
```
def test_simple():
    title = "Title H   "
    items = [{'href':'a.com','caption':'ACaption'},{'href':'b.com','caption':'Bcaption'}]
    content = "this is content"
    result = render('simple.html',**locals())
    print(result)
if __name__ == '__main__':
    test_simple()
```
执行上面的代码，渲染模版的结果如下：
```
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 表达式的结果，以及过滤器 -->
    <title>Title  H</title>
</head>
<body>
    <!-- 注释 -->

    <ul id="navigation">
        <!-- 语句，以endfor结束 -->

            <!-- 访问变量的属性 -->
            <li><a href="a.com">ACaption</a></li>

            <!-- 访问变量的属性 -->
            <li><a href="b.com">Bcaption</a></li>

    </ul>
    <p>This is content</p>
</body>
</html>
```
可以看到，使用Jinja2渲染后title中的空格已经被删除，for循环也正确渲染了多个超链接标签。

3.2 继承功能演示
为了演示继承的功能，我们需要使用两个HTML文件，分别是base.html 和index.html。
base.html的内容如下：
```
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 定义代码块，可以在子模块中重载 -->
    {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">
        <!-- 定义代码块，没有提供默认内容 -->
        {% block content %}
        {% endblock %}
    </div>
    <div id="footer">
        <!-- 定义代码块，没有提供默认内容 -->
        {% block footer %}
        {% endblock %}
    </div>
</body>
</html>
```
index.html的内容如下：
```
<!--写在开头，用以继承 -->
{% extends "base.html" %}

<!--标题模块被重载 -->
{% block title %}Index{% endblock %}

<!--head模块被重载，并且，使用super继承了base.html中的head的内容 -->
{% block head %}
    {{ super() }}
<style type="text/css"> .important { color: #336699; } </style>
{% endblock %}

<!--覆盖了content模块 -->
{% block content %}
<h1>This is h1 content</h1>
<p class="important">Welcome on my awesome homepage.</p>
{% endblock %}
```
我们使用下面的python代码渲染Jinja2模版：
```
def test_extend():
    result = render('index.html')
    print(result)
if __name__ == '__main__':
    test_extend()
```
渲染以后生成的结果如下：
```
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 定义代码块，可以在子模块中重载 -->
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Index - My Webpage</title>
    <style type="text/css"> .important { color: #336699; } </style>
</head>
<body>
    <div id="content">
        <!-- 定义代码块，没有提供默认内容 -->

<h1>This is h1 content</h1>
<p class="important">Welcome on my awesome homepage.</p>

    </div>
    <div id="footer">
        <!-- 定义代码块，没有提供默认内容 -->
    </div>
</body>
</html>
```
从这个例子中可以看到：
1）我们渲染的是index.html，并没有直接渲染base.html，但是最后生成的模版中包含了完整的HTML框架，这也是继承广泛的使用场景；
2）我们虽然在index.html中定义了title块，但是，因为我们使用{{ super() }}引用了base.html中的HEAD块，因此，最后渲染的结果中包含了base.html中的head块和index.html中的块。例如，最后渲染的结果中的title标签的内容是“Index - My Webpage”，这个字符串就来自index.html和base.html；
3）我们在index.html中重新定义了content块的内容，因此，最后生成的文档中在正确位置显示了content块的内容。
# 4. 案例：使用Jinja2生成HTML表格和XML配置文件

前面的例子只演示了Jinja2 的语法，接下来我们用两个更加实际的例子。
4.1 使用Jinja2 生成HTML表格
假如我们比较关心楼市的走向。因此我们写了一个爬虫爬去了某市楼市信息并通过电子邮件发送给自己。我们将爬去到的信息存放在一个HTML的表格中。我们需要一个模版。在这个例子中，模版的名称称为hzfc.html，内容如下：
```
<html>
<body>
    <table>
        {% for item in items %}
        <tr>
            <td>{{ loop.index }}</td>
            <td><a href="{{ item['href'] }}">{{ item['title'] }}</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
使用模版后，我们只需要在python代码中调用渲染函数即可，
```
#-*- coding: UTF-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import jinja2

links = [ {'title' : u'XXXX', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/21/021404496.shtml'},{'title' : u'XXXX23', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/21/021404496.shtml'},{'title' : u'XXXX23534', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/21/021404496.shtml'}]
content = render('hzfc.html', items=links)
print(content)
```
可以看到，当我们将业务逻辑与表现逻辑分离以后，代码自然就变得清晰易懂、易于维护了。

4.2 使用Jinja2 生成XML配置文件

在本例中，又一个名为base.cfg的配置文件，该文件保存了配置参数取值：
```
[DEFAULT]
issa_server_a_host = 10.166.226.151
issa_server_a_port = 8101

issa_server_b_host = 10.166.226.152
issa_server_b_port = 8102

issa_server_c_host = 10.166.226.153
issa_server_c_port = 8103
```
此外，还有个名为pass_servicel_template.xml的配置模版，模版的生成内容如下：
```
<?xml version="1.0" encoding="utf-8" ?>
<pass_servicel>
    <issa_server_a_host>{{ issa_server_a_host }}</issa_server_a_host>
    <issa_server_a_port>{{ issa_server_a_port }}</issa_server_a_port>
    <issa_server_c>{{ issa_server_c_host }}:{{ issa_server_c_port }}</issa_server_c>
</pass_servicel>
```
在本例中，存在两个上层服务。另外一个上层服务的配置模版名称为pass_service2_template.xml,内容如下：
```
<?xml version="1.0" encoding="utf-8" ?>
<pass_service2>
    <issa_server_b_host>{{ issa_server_b_host }}</issa_server_b_host>
    <issa_server_b_port>{{ issa_server_b_port }}</issa_server_b_port>
    <issa_server_c>{{ issa_server_c_host }}:{{ issa_server_c_port }}</issa_server_c>
</pass_service2>
```
现在的需求是读入配置文件，然后使用Jinja模版渲染技术将两个上层服务的配置模版渲染成配置文件。相关的python代码如下：
```
#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function

import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import jinja2

NAMES = ['issa_server_a_host',"issa_server_a_port","issa_server_b_host","issa_server_b_port","issa_server_c_host","issa_server_c_port"]

def render(tpl_path, **kwargs):
    path,filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)

def parser_vars_into_globals(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    for name in NAMES:
        globals()[name] = parser.get('DEFAULT', name)

def main():
    parser_vars_into_globals('base.cfg')
    with open('pass_service1.xml',"w") as f:
        f.write(render('pass_service1_template.xml',**globals()))

    with open('pass_service2.xml',"w") as f:
        f.write(render('pass_service2_template.xml',**globals()))

if __name__ == '__main__':
    main()
```
生成上层服务配置的Python 代码能够同时运行在python2和python3下。为了避免今后配置项较多，对于每个配置项都需要单独读取的问题，本例中使用了一个小技巧，即通过给globals字典赋值的方式定义全局变量，然后将所有的全局变量传递给模版。模版渲染时只会用到自己所需要的变量，渲染完成后会在当前目录下生成两个配置文件，分别是pass_service1.xml和pass_service2.xml。

