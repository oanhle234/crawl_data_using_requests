import requests
from lxml import html
import csv

page = requests.get('https://news.ycombinator.com/news')
x = html.fromstring(page.content)

# Print "title of post"
title = x.xpath('//td/a[@class="titlelink"]/text()')
print(title)
for i in title:
    print("title: ", i)

# Print "source from each post"
source = x.xpath('//td/a[@class="titlelink"]/@href')
for i in source:
    print("source: ", i)

# Print "point from each post"
point = x.xpath('//td/span[@class="score"]/text()')
for i in point:
    print("point: ", i)

# Print "name of people create post"
posted_by = x.xpath('//td/a[@class="hnuser"]/text()')
for i in posted_by:
    print("posted by: ", i)

# Print "quantity of comment"
number_of_comments = x.xpath('//td[@class="subtext"]/a[3]/text()')
for i in number_of_comments:
    print("number of comments: ", i)

# Print "posted date"
posted_date = x.xpath('//span[@class="age"]/a/text()')
for i in posted_date:
    print("poste date: ", i)

# Export "csv file"
data = [[title], [source], [point], [posted_by], [number_of_comments], [posted_date]]
with open('test.csv', 'w') as file:
    wr = csv.writer(file)
    wr.writerows(data)
file.close()

