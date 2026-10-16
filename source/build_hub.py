"""Builds ../letras-y-mezcla.html (dropdown page with both apps) from ../index.html (Letra del día) and ../tablero-de-mezcla.html. Run build.py first if you changed Letra del día, then: python3 build_hub.py"""
import json
SK=open('../tablero-de-mezcla.html',encoding='utf8').read()
HEAD=SK[:SK.index('<title>')]   # doctype + head + <body> from the published skeleton
assert HEAD.startswith('<!doctype html>') and HEAD.rstrip().endswith('<body>'),HEAD[-60:]
letra=open('../index.html',encoding='utf8').read()
A=HEAD+letra+'\n</body></html>'
B=SK.replace('</head>','<style>section[aria-labelledby="hLang"]{display:none!important}</style></head>',1)
assert B!=SK
def lit(s):
    j=json.dumps(s,ensure_ascii=False)
    return j.replace('</','<\\/').replace('<!--','<\\!--').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
t=open('hub_template.html',encoding='utf8').read().replace('__A__',lit(A)).replace('__B__',lit(B))
open('../letras-y-mezcla.html','w',encoding='utf8').write(t)
print(len(t)/1e6,'MB')
