from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver.exe', options=chrome_options)
'''
firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Firefox(options=firefox_options)
actions = ActionChains(wd)

wd.get("https://www.kialo.com/pro-life-vs-pro-choice-should-abortion-be-legal-5637?closeSidebar=notifications.activity")
# el = WebDriverWait(wd, 2000).until(EC.invisibility_of_element((By.CLASS_NAME, 'pre-rendered')))
claim = wd.find_element_by_class_name('selected-claim').text
WebDriverWait(wd, 2000).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
)
button = wd.find_element_by_class_name('claim-controls__control-item--menu-button').click()
context_menu = wd.find_element_by_class_name('context-menu').find_elements_by_class_name('context-menu-item__text')

for el in context_menu:
    if el.text == 'Voting Stats':
        el.click()
        break

histogram = wd.find_elements_by_class_name('voters-histogram__voters-bar-container')
res = []
for count in histogram:
    res.append(count.find_element_by_class_name('icon__counter').text)

print(str(claim) + str(res))
'''
rects_map = wd.find_elements_by_class_name('mini-map-claim-background')
print(len(rects_map))
rects_map[1].click()
rects_map = wd.find_elements_by_class_name('mini-map-claim-background')
print(len(rects_map))
'''

pro_map = wd.find_elements_by_class_name('mini-map-claim--pro')
con_map = wd.find_elements_by_class_name('mini-map-claim--con')
print(len(pro_map))
print(len(con_map))
pro_map[0].find_element_by_tag_name('rect').click()
pro_map2 = wd.find_elements_by_class_name('mini-map-claim--pro')
con_map2 = wd.find_elements_by_class_name('mini-map-claim--con')
print(len(set(pro_map2) - set(pro_map)))
print(len(con_map))
claim = wd.find_element_by_class_name('selected-claim').text
print(claim)

'''
f = open('page.txt', 'w')
f.write(wd.page_source)
f.close()
'''
'''
el = WebDriverWait(wd, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="scroll-context-20"]/div[4]/div/div[2]/div/main/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[3]/button[1]'))
)
# wd.find_element_by_xpath('//*[@id="scroll-context-20"]/div[4]/div/div[2]/div/main/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[3]/button[1]')

claim_cont = wd.find_element_by_class_name('selected-claim-container')
claim_controls = wd.find_element_by_class_name('claim-header__controls')
wd.switch_to.(claim_controls)
# print(claim_controls.find_elements_by_name('*'))
butt = claim_controls.find_elements_by_tag_name('button')
print(butt)

print(wd.find_element_by_class_name('impact-representation__foreground').get_attribute('style'))

# actions.context_click(claim_cont).perform()

# el = wd.find_element_by_class_name('claim-text__content')
# print(el.text)

hoverable-tooltip-component icon-button claim-controls__control-item claim-controls__control-item--menu-button icon-hover-and-active-trigger
hoverable-tooltip-component icon-button claim-controls__control-item comments-indicator                        icon-hover-and-active-trigger
'''
wd.close()
