"""Builds ../index.html from template.html and the JSON files in data/. Run: python3 build.py"""
import json
d=json.load(open('data/data.json'))
syl=json.load(open('data/syl.json'))
ONE={'a':'La araña anda en la rama.','b':'Beto besa a su bebé.','c':'Cuca come coco.','ch':'Chucho toma leche.','d':'Dina da un dulce.','e':'El elefante es enorme.','f':'La foca Fifi usa una foto.','g':'El gato Gabo guarda la goma.','h':'Hilda come helado.','i':'La iguana está en la isla.','j':'La jirafa Jacinta salta.','k':'Karen hace karate.','l':'El loro Lalo ve la luna.','ll':'La lluvia llega a la calle.','m':'El mono mira la mesa.','n':'El nene Nico ve una nube.','ñ':'La niña Toña ve una piñata.','o':'Olga ve un oso.','p':'Pepe pinta un pato.','qu':'Quique quiere queso.','r':'Rita ve una rana.','rr':'El perro corre al carro.','s':'Sofía saca su silla al sol.','t':'Teo tiene un taco.','u':'Úrsula come uvas.','v':'Vera ve una vaca.','w':'Wanda come un wafle.','x':'El taxi lleva un xilófono.','y':'Yola usa un yoyo.','z':'El zorro usa un zapato.'}
fn=lambda x:x.replace('ñ','ny')
clips=dict(d['CLIPS']);clips.update(json.load(open('data/clips_extra.json')))
out={'LET':d['LET'],'NAMES':d['NAMES'],'ANCH':d['ANCH'],'SENT':{k:[v] for k,v in ONE.items()},'HW':d['HW'],'CLIPS':clips,'SYL':syl,
 'SIMG':json.load(open('data/simg.json')),'WIMG':json.load(open('data/wimg.json')),'AIMG':json.load(open('data/anch.json'))}
t=open('template.html',encoding='utf8').read()
open('../index.html','w',encoding='utf8').write(t.replace('__DATA__',json.dumps(out,ensure_ascii=False,separators=(',',':'))))
wmiss=sorted(w.replace('-','') for ws in syl.values() for w in ws if fn(w.replace('-','')) not in clips)
json.dump({'sent':ONE,'words':sorted({w.replace('-','') for ws in syl.values() for w in ws}),'wordsNoClip':wmiss},open('data/lists.json','w'),ensure_ascii=False)
print('index.html written')
