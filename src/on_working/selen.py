from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import time


dataset = pd.DataFrame(columns=['Level', 'Stance', 'Claim', 'Votes'])


def get_claim_votes(stance, level, pros_map, cons_map):
    claim = wd.find_element_by_class_name('selected-claim').find_element_by_class_name('claim-text__content').text
    claim_container = wd.find_element_by_class_name('selected-claim-container')
    time.sleep(0.2)
    WebDriverWait(claim_container, 2000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
        # EC.visibility_of_element_located((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
    )

    try:
        claim_container.find_element_by_class_name('claim-controls__control-item--menu-button').click()
    except ElementClickInterceptedException as e:
        # print(e)
        print('popup')
        wd.find_element_by_class_name('pop-up-template__close').click()

    context_menu = wd.find_element_by_class_name('context-menu').find_elements_by_class_name('context-menu-item__text')

    for opt in context_menu:
        if opt.text == 'Voting Stats':
            try:
                opt.click()
            except ElementClickInterceptedException as e:
                # print(e)
                print('popup')
                wd.find_element_by_class_name('pop-up-template__close').click()
            break

    histogram = wd.find_elements_by_class_name('voters-histogram__voters-bar-container')
    votes = []
    for count in histogram:
        votes.append(count.find_element_by_class_name('icon__counter').text)

    global dataset
    dataset = dataset.append({'Level': '1.{}'.format(level), 'Stance': stance, 'Claim': claim, 'Votes': votes},
                             ignore_index=True)

    new_total_pros_map = wd.find_elements_by_class_name('mini-map-claim--pro')
    new_total_cons_map = wd.find_elements_by_class_name('mini-map-claim--con')
    sub_pros_map = list(set(new_total_pros_map) - set(pros_map))
    sub_cons_map = list(set(new_total_cons_map) - set(cons_map))

    # sub_pros_map[0].find_element_by_tag_name('rect').click()
    # get_claim_votes('pro', 0, new_total_pros_map, new_total_cons_map)

    for pro in sub_pros_map:
        try:
            pro.find_element_by_tag_name('rect').click()
        except ElementClickInterceptedException as e:
            # print(e)
            print('popup')
            wd.find_element_by_class_name('pop-up-template__close').click()
        get_claim_votes('pro', 0, new_total_pros_map, new_total_cons_map)
        
    for con in sub_cons_map:
        try:
            con.find_element_by_tag_name('rect').click()
        except ElementClickInterceptedException as e:
            # print(e)
            print('popup')
            wd.find_element_by_class_name('pop-up-template__close').click()
        get_claim_votes('con', 0, new_total_pros_map, new_total_cons_map)

    # return [level, stance, claim, votes]


firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--disable-notifications')
firefox_options.add_argument('--disable-popup-blocking')
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

dataset = dataset.append({'Level': '1', 'Stance': 'None', 'Claim': main_claim, 'Votes': votes}, ignore_index=True)

pros_map = wd.find_elements_by_class_name('mini-map-claim--pro')
cons_map = wd.find_elements_by_class_name('mini-map-claim--con')

index_level = 1
for pro_map in pros_map:
    pro_map.find_element_by_tag_name('rect').click()
    get_claim_votes('pro', index_level, pros_map, cons_map)
    # print(res)
    index_level += 1

for con_map in cons_map:
    con_map.find_element_by_tag_name('rect').click()
    get_claim_votes('con', index_level, pros_map, cons_map)
    # print(res)
    index_level += 1

dataset.to_excel('output.xlsx')
print(dataset.iloc[:-1])
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
