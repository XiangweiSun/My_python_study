from bs4 import BeautifulSoup
import re


path = 'C:/Users/s00169008/Desktop/54321.html'

htmlfile = open(path, 'r', encoding='utf-8')

htmlhandle = htmlfile.read()


soup = BeautifulSoup(htmlhandle,'lxml')

# question = soup.find(attrs = {'ng-bind-html': 'checkSubject.subjectTitle'}).string

answer = soup.find_all(class_='kaoshi-answer')


answer1 = re.findall('正确答案(.*?)</span>', str(answer))
#
print(answer1)



# [@ng-bind-html='checkSubject.subjectTitle']





