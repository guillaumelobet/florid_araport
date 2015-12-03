# file: main.py

import requests
import re
import json

def search(arg):

# arg contains a dict with a single key:value
# locus is AGI identifier and is mandatory
    
    # Return nothing if client didn't pass in a locus parameter
    if not ('locus' in arg):
       return
    
    # Validate against a regular expression
    locus = arg['locus']
    locus = locus.upper()
    p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
    if not p.search(locus):
        return

    url = 'http://www.phytosystems.ulg.ac.be/florid/details?gene=' + locus + '&type=json'
    r = requests.get(url) 
    
    if r.ok:
        print r.content
        print '---'
    else:
        return 'text/plaintext; charset=ISO-8859-1', 'An error occurred on the remote server'

def list(arg):
    pass
