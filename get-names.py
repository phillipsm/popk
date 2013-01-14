import lxml.html as lh
import urllib2
import json

#########
# Get the top 100 female names and the top 100
# male names from the SSA. Print them in JSON format
#########

def zigzag(seq):
    # Thanks, http://stackoverflow.com/a/4696161
    return seq[::2], seq[1::2]

url='http://www.ssa.gov/oact/babynames/decades/century.html'
doc=lh.parse(urllib2.urlopen(url))

names = []
for elt in doc.iter('td'):
    if 'center' in elt.values():
        names.append(elt.text)


male, female = zigzag(names)

print json.dumps({"female": female, "male": male}, sort_keys=False, indent=4, separators=(',', ': '))
        

