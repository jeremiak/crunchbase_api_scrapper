import simplejson as json
import urllib2

def get_all_cb_comps():
    u = urllib2.urlopen('http://api.crunchbase.com/v/1/companies.js')
    
    comps = u.read()

    return comps

def get_spec_cb_comp(comp_name):
    print '-- %s' % comp_name
    u = urllib2.urlopen('http://api.crunchbase.com/v/1/company/%s.js' % comp_name)
    
    comp = u.read()

    return comp

def convert_to_json(url_result):
    j = json.loads(url_result)

    return j

def cb_comps_as_json():
    comps = get_all_cb_comps()
    # comps as json
    caj = convert_to_json(comps)

    return caj

def spec_cb_comp_as_json(comp_name):
    try:
        comp = get_spec_cb_comp(comp_name)
        # comp as json
        caj = convert_to_json(comp)
        return caj
    except:
        print 'Could not find %s' % comp_name
        return None
    
