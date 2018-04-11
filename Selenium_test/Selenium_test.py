#导入webdriver库
from selenium import webdriver

#导入Beautifulsoup库
from bs4 import BeautifulSoup

#导入时间库，用来做网页加载的延迟
import time

#导入正则表达式库
import re

#获取浏览器对象
brower = webdriver.Chrome()

#考试链接的地址
URL = 'http://ilearning.huawei.com/next/home.html#/examinationContent?exam_id=1502&examinationId=1502'

#获取考试链接的地址
brower.get(URL)

time.sleep(3)

#输入员工账号
brower.find_element_by_xpath('//*[@id="uid"]').clear()
brower.find_element_by_xpath('//*[@id="uid"]').send_keys('s00169008')

#输入员工密码
brower.find_element_by_xpath('//*[@id="password"]').clear()
brower.find_element_by_xpath('//*[@id="password"]').send_keys('Sun771983921$')

#点击按钮
brower.find_element_by_xpath('//*[@id="page-input-holder"]/input[2]').click()

#延迟10秒钟，等待网页加载完毕
time.sleep(10)

#打印出加载JS后的网页源代码，用来获取后续点击的XPATH ID
#print(brower.page_source)

#点击开始考试按钮
brower.find_element_by_xpath('//*[@id="examRightInfo"]/a').click()

#延迟10秒钟，等待网站全部加载完毕
time.sleep(10)

#此处需要手工点击弹出的窗口确定按钮

#点击查看答案按钮
brower.find_element_by_xpath('//*[@id="examin_content"]/div[5]/div/div/div[2]/a[2]').click()

#延迟10秒钟等待网页JS加载
time.sleep(10)

#获取新的网页源代码
#print(brower.page_source)


#获取题目总数
Page = brower.page_source
Re_pattern = re.compile(u'<span class="ng-binding">已答：0/(.*?)</span>')
Page_num = int(re.findall(Re_pattern, Page)[0])


for page in range(1, Page_num + 1):

    time.sleep(3)
    brower.find_element_by_xpath('//*[@id="boxscroll4"]/div[1]/ul[2]/li[' + str(page) + ']').click()
    time.sleep(3)

    html_file = brower.page_source

    soup = BeautifulSoup(html_file,'lxml')

    question = soup.find(attrs={'ng-bind-html': 'checkSubject.subjectTitle'}).string

    print(question)

    answer = soup.find_all(class_='kaoshi-answer')

    answer1 = re.findall('正确答案(.*?)</span>', str(answer))

    print(answer1)



//*[@id="boxscroll4"]/div[1]/ul[2]/li[1]

//*[@id="boxscroll4"]/div[1]/ul[3]/li[1]






# brower.find_element_by_xpath('//*[@id="toDoListId"]/nobr/b[1]').click()//*[@id="page-input-holder"]/input[2]
#
#
# page = brower.page_source
# print(page)
#
# brower.get_screenshot_as_file('123.png')
