#!/usr/bin/env python

from jinja2 import Template,Environment,FileSystemLoader


project = "us.gcr.io/molten-turbine-123703"
num_workers=6

obj={}
obj["if_image"] = project+"/tf_if"
obj["server_image"] = project+"/tf_server"
obj["num_workers"] = num_workers

cs="master|localhost:2222"
for i in range(num_workers):
    cs+=",worker%d|localhost:%d" % (i,2223+i)

obj["cluster_spec"] = cs

env = Environment(loader=FileSystemLoader('./template', encoding='utf-8'))
tmpl = env.get_template("podspec_template.yml")
print tmpl.render(obj)
