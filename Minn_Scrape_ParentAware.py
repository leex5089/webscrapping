import pandas as pd
import requests
import json

base_url = 'http://parentaware.org/provider/'


def get_data(extension):
    url = base_url + extension + '/'
    
    # get the provider page
    try:
        page = requests.get(url).text
    except:
        try:
            print('Connection timeout -- retrying once')
            print('Extension value is ' + extension) 
            page = requests.get(url).text
        except:
            print('Connection timeout again.  Skipping this value')
            return(null)
    
    lines = page.split('\n')
    
    for line in lines:
        if 'The requested page does not appear to exist.' in line:
            return
    
    # save a copy
    with open('page_archive' + extension + '.html', 'w') as f:
        f.write(page)
    
    # scan the page for the line with the key phrase
    provider_data = ''
    for line in lines:        
        if 'controller.setProvider' in line:
            provider_data = line
            
    # trim the provider data
    provider_data = provider_data.replace('controller.setProvider(', '')
    provider_data = provider_data.replace(');', '')
    provider_data = provider_data.strip()
    
    # translate to a pandas series
    clean_data = pd.Series(json.loads(provider_data))
    
    return clean_data
    
candidate_list = range(0, 40000)
data_list = []

for candidate in candidate_list:
    ext = str(candidate)
    data_list.append(get_data(ext))
    
df = pd.concat(data_list, axis = 1).T
df.to_csv('data_output.csv')
