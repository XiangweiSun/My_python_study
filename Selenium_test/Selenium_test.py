from selenium import webdriver
import time

brower = webdriver.Chrome()

brower.get('http://ilearning.huawei.com/next/home.html#/examinationContent?exam_id=1502&examinationId=1502')



brower.find_element_by_xpath('//*[@id="uid"]').clear()
brower.find_element_by_xpath('//*[@id="uid"]').send_keys('s00169008')

brower.find_element_by_xpath('//*[@id="password"]').clear()
brower.find_element_by_xpath('//*[@id="password"]').send_keys('Sun771983921$')

brower.find_element_by_xpath('//*[@id="page-input-holder"]/input[2]').click()


time.sleep(10)

print(brower.page_source)

brower.find_element_by_xpath('//*[@id="examRightInfo"]/a').click()
time.sleep(10)


brower.find_element_by_xpath('//*[@id="examin_content"]/div[5]/div/div/div[2]/a[2]').click()




# brower.find_element_by_xpath('//*[@id="toDoListId"]/nobr/b[1]').click()//*[@id="page-input-holder"]/input[2]
#
#
# page = brower.page_source
# print(page)
#
# brower.get_screenshot_as_file('123.png')
