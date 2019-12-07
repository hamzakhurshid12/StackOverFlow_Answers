import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def work_parser(ip):
    t = ip.find_all('td')
    time.sleep(5)
    print(t[1].text)

def work_print(ip):
    time.sleep(5)
    print(ip)

html = BeautifulSoup(r'<tr class="odd"><td class="country"><img alt="Cn" src="//fs.xicidaili.com/' \
       r'images/flag/cn.png"/></td><td>117.69.153.136</td><td>9999</td></tr>')
ips = html.find_all('tr', class_='odd')

time.sleep(1)

print('### Experiment 1')
print('This experiment presents that work_parser and work_print are correct')

print('---1.1 work_parser execute in order')
for ip in ips:
    work_parser(ip)

print('---1.2 work_print execute in order')
for ip in ips:
    work_print(ip)

print('\n')
print('### Experiment 2')
print('--- This experiment presents that in multithread running, work_print cuns well, but work_parser does not.')

print('---2.1 work_parser execute by thread')
with ThreadPoolExecutor(max_workers=2) as executor:
    for ip in ips:
        executor.submit(work_parser, (ip))

print('---2.2 work_print execute by thread')
with ThreadPoolExecutor(max_workers=2) as executor:
    for ip in ips:
        executor.submit(work_print, (ip))

print('--- Experiment is over')
