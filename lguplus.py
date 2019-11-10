
# coding: utf-8

# In[54]:


from selenium import webdriver
import time, re


# In[55]:


drv = webdriver.PhantomJS()
drv.get("https://www.uplus.co.kr/css/chgi/chgi/RetrieveTvContentsMFamily.hpi")


# In[59]:


drv.find_element_by_id('3').click()
time.sleep(1)
for i in range(101, 110):
    el = drv.find_element_by_id(str(i))
    print('\n', el.text)
    el.click()
    time.sleep(1)
    html = drv.find_element_by_css_selector('table').get_attribute('innerHTML')
    regex = re.compile('<td class="txtC">(\S+)</td>\s*<td class="txtL">(.+)\n')
    for j in regex.findall(html):
        print (j[0], j[1])

