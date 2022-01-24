from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_claim_votes(stance, level):
    claim = wd.find_element_by_class_name('selected-claim').find_element_by_class_name('claim-text__content').text
    claim_container = wd.find_element_by_class_name('selected-claim-container')
    time.sleep(1)
    WebDriverWait(claim_container, 2000).until(
        # EC.presence_of_element_located((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
        EC.element_to_be_clickable((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
        # EC.visibility_of_element_located((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
    )

    claim_container.find_element_by_class_name('claim-controls__control-item--menu-button').click()
    context_menu = wd.find_element_by_class_name('context-menu').find_elements_by_class_name('context-menu-item__text')

    for opt in context_menu:
        if opt.text == 'Voting Stats':
            opt.click()
            break

    histogram = wd.find_elements_by_class_name('voters-histogram__voters-bar-container')
    votes = []
    for count in histogram:
        votes.append(count.find_element_by_class_name('icon__counter').text)

    return [level, stance, claim, votes]


firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Firefox(options=firefox_options)
actions = ActionChains(wd)

wd.get("https://www.kialo.com/pro-life-vs-pro-choice-should-abortion-be-legal-5637?closeSidebar=notifications.activity")

main_claim = wd.find_element_by_class_name('selected-claim').text
WebDriverWait(wd, 2000).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
)
button = wd.find_element_by_class_name('claim-controls__control-item--menu-button').click()
context_menu = wd.find_element_by_class_name('context-menu').find_elements_by_class_name('context-menu-item__text')

for el in context_menu:
    if el.text == 'Voting Stats':
        el.click()
        break

histogram = wd.find_elements_by_class_name('voters-histogram__voters-bar-container')
votes = []
for count in histogram:
    votes.append(count.find_element_by_class_name('icon__counter').text)

print(str(main_claim) + str(votes))


pros_map = wd.find_elements_by_class_name('mini-map-claim--pro')
cons_map = wd.find_elements_by_class_name('mini-map-claim--con')
# print(len(pros_map))
# print(len(cons_map))

index_level = 0
for pro_map in pros_map:
    pro_map.find_element_by_tag_name('rect').click()
    res = get_claim_votes('pro', '1.{}'.format(index_level+1))
    print(res)
    index_level += 1

for con_map in cons_map:
    con_map.find_element_by_tag_name('rect').click()
    res = get_claim_votes('con', '1.{}'.format(index_level+1))
    print(res)
    index_level += 1
'''
pro_map[0].find_element_by_tag_name('rect').click()
pro_map2 = wd.find_elements_by_class_name('mini-map-claim--pro')
con_map2 = wd.find_elements_by_class_name('mini-map-claim--con')
print(len(set(pro_map2) - set(pro_map)))
print(len(con_map))
claim = wd.find_element_by_class_name('selected-claim').text
print(claim)
'''
'''
# el = WebDriverWait(wd, 2000).until(EC.invisibility_of_element((By.CLASS_NAME, 'pre-rendered')))
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

hoverable-tooltip-component icon-button claim-controls__control-item claim-controls__control-item--menu-button icon-hover-and-active-trigger
hoverable-tooltip-component icon-button claim-controls__control-item claim-controls__control-item--menu-button icon-hover-and-active-trigger
'''
wd.close()
