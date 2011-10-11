import crunchbase_api as cb_api
import simplejson as json


def add_to_list(comp_name, sf_office):
    f = open('sfcomps.txt', 'a')
    
    row = '%s, %s, %s, %s,\n' % (comp_name, sf_office[0], sf_office[1], sf_office[2])
    print row

    f.write(row)
    f.close()


def exists_on_cb(company):
    print 'Checking to see if %s exists on CB' % company['name']
    if '404' in company['name']:
        return False
    else:
        return True

def has_been_acquired(company):
    print 'Checking if %s has been acquired' % company['name']
    if company['acquisition']:
        return True
    else:
        return False

def is_mobile_company(company):
    print 'Checking if %s is a mobile company' % company['name']
    if company['category_code'] == 'mobile':
        return True
    else:
        return False

def less_then_50_employees(company):
    print 'Checking to see if %s has less than 50 employees' % company['name']
    if company['number_of_employees'] < 51:
        return True
    else:
        return False

def located_in_sf(company):
    print 'Checking for SF locations of %s' % company['name']
    sf_offices = []

    if company['offices']:
        for office in company['offices']:
            if office['city'] == 'San Francisco':
                sf_offices.append(office['address1'])
                sf_offices.append(office['address2'])
                sf_offices.append(office['zip_code'])
            else:
                pass
        return sf_offices
    else:
        return False

# caj = comps as json
def filter_by_sf(caj):
    for comp in caj:
        # check to make sure the company doesn't return a 404 as a name
        company = cb_api.spec_cb_comp_as_json(comp['permalink'])
        if company != None:
            if exists_on_cb(company):
                if is_mobile_company(company) == True:
                    if less_then_50_employees(company) == True:
                        if has_been_acquired(company) == True:
                            pass
                        else:
                            sf_office = located_in_sf(company)
                            if sf_office == False:
                                pass
                            elif sf_office == []:
                                pass
                            else:
                                print sf_office
                                add_to_list(company['name'], sf_office)
                                print '**** %s added ****' % company['name']
                            
            print '----------'

def get_sf_companies():
    print 'Criteria for this script:'
    print 'Mobile company'
    print 'Less than 50 employees'
    print 'Has yet to be acquired'
    print 'Has SF based offices'

    companies = cb_api.cb_comps_as_json()

    f = open('sfcomps.txt', 'a')
    f.close()

    filter_by_sf(companies)

    print 'Done'
