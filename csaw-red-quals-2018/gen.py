#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import errno
import re
import sys
import codecs
import json
import pymustache
import stringcase

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.stderr = codecs.getwriter("utf-8")(sys.stderr)

def mkdir_p(path):
	try: os.makedirs(path)
	except OSError as ex:
		if ex.errno == errno.EEXIST and os.path.isdir(path): pass
		else: raise

def transform(name):
	name = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
	return re.sub('([a-z0-9])([A-Z])', r'\1-\2', name).lower()

if __name__ == "__main__":
	tpl = """
# CSAW RED Quals 2018 : {{name}}

**Category:** {{category}}
**Points:** {{value}}
**Solves:** {{nsolve}}
**Description:**

{{&description}}

## Write-up

## Other write-ups and resources

"""
	tpl_compiled = pymustache.compiled(tpl)

	lookup = {}
	with codecs.open("chals-solves.json","r","utf-8") as f:
		obj = json.load(f)
		lookup = {int(k):int(v) for k,v in obj.iteritems()}

	with codecs.open("chals.json","r","utf-8") as f:
		obj = json.load(f)
		for task in obj["game"]:
			task["nsolve"] = lookup[task["id"]]
			basedir_p0 = task["category"].lower()
			name = task["name"]
			name = re.sub(r"\([^)]+\)","",name)
			name = name.strip()
			name = name.replace("'","")
			name = name.replace(" ","-")
			name = name.replace("_","-")
			name = name.strip()
			if "-" not in name:
				ms = re.findall(r"[A-Z][a-z]",name)
				if len(ms) > 1:
					name = stringcase.spinalcase(name)
			name = name.lower()
			basedir_p1 = "%s-%d"%(name,int(task["value"]))
			basedir = os.path.join(basedir_p0,basedir_p1)
			fp = os.path.join(basedir,"README.md")
			if os.path.isfile(fp): continue
			mkdir_p(basedir)
			with codecs.open(fp,"w","utf-8") as g: print>>g, tpl_compiled.render(task)
