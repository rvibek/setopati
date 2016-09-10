import lxml.html
import csv
#import requests
from lxml import etree


url = 'http://www.setopati.com/?home=true'

parseURL = etree.HTMLParser(encoding='utf-8')
html =etree.parse(url, parseURL)



f = open('setopati.csv', 'w')
writer = csv.writer(f)

i = 1
while 1:
    twit =    html.xpath('//div[contains(@class, "item fb_twitter")]/ul/li[%d]/h2/text()' % i)
    twitter = html.xpath('//div[contains(@class, "item fb_twitter")]/ul/li[%d]/span/text()' % i)
    media = html.xpath('//div[contains(@class, "item fb_twitter")]/ul/li[%d]/span/@class' % i)

    if not twit:
        break
    else:
        i += 1
       # sheet.append(twit)

        if media[0] == 'fb_title fb_icon':
            media = 'facebook'
        elif media[0] == 'fb_title twit_icon':
            media = 'twitter'
        else:
            media = ''

       	x = ' '.join(twit).encode('utf-8'), ' '.join(twitter).encode('utf-8'), media
        print x
        writer.writerow(x)

f.close()
