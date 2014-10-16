# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs, csv, datetime, json, sys, urllib
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen
try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

def count_packages(package_names):
    package_list = []
    for name in package_names:
        url = 'https://pypi.python.org/pypi/%s/json' % name
        reader = codecs.getreader("utf-8")
        package_data =  json.load(reader(urlopen(url)))
        downloads =  package_data['info']['downloads']
        print(name, ':', downloads['last_month'], 'downloads last_month')
        all_time = 0
        package_releases = package_data['releases']
        num_releases = len(package_releases)
        first_upload = datetime.datetime.now().isoformat()
        for version, release in package_releases.items():
            for downloadable in release:
                all_time += downloadable['downloads']
                upload_time = downloadable['upload_time']
                first_upload = min(first_upload, upload_time)
        package_list.append((downloads['last_month'],
                            downloads['last_week'],
                            downloads['last_day'],
                            all_time,
                            num_releases,
                            first_upload,
                            name))
    package_list.sort(reverse=True)
    print('================================')
    return package_list

def save_csv(package_list, name):
    with open('%s.csv' % name, 'w') as csv_out_file:
        writer =  csv.writer(csv_out_file)
        writer.writerow(['last month', 'last week', 'last day', 'all',
                    'num_releases', 'first_upload', 'name'])
        for p in package_list:
            print(p[0], p[3]//p[4], p[6])
            writer.writerow(p)

def count_user(username, role=None):
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    user_packages = client.user_packages(username)
    if role:
         package_names = [n[1] for n in user_packages
                            if n[0] == role]
    else:
        package_names = [n[1] for n in user_packages]
    package_names = list(set(package_names))
    package_list = count_packages(package_names)
    return package_list

def count_search(**kwargs):
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    packages = client.search(kwargs)
    package_names = [p['name'] for p in packages]
    package_list = count_packages(package_names)
    return package_list



if __name__ == '__main__':
    kwargs = dict(x.split('=', 1) for x in sys.argv[1:])
    package_list = count_search(**kwargs)
    save_csv(package_list, list(kwargs.values())[0])

