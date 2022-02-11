from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import time


dataset = pd.DataFrame(columns=['Level', 'Stance', 'Claim', 'Votes', 'Comments', 'Depth'])
claim_already_visited = {}


def try_click(elem):
    '''
    Try to click a webdriver element. Handle the following exceptions:
    - if the popup window shows
    - if a claim from guide-map obscure the button for the menu
    :param elem:
    '''
    attempts = 0
    global actions
    while attempts < 3:
        try:
            elem.click()
            break
        except ElementClickInterceptedException:
            print('EXCEPTION')
            try:
                wd.find_element_by_class_name('pop-up-template__close').click()
                print('popup')
                # break
            except Exception:
                print('EXCEPTION2')
            # Move mouse to another location to avoid the text shown by hovering mouse on branch claim
            actions.move_to_element(wd.find_element_by_class_name('icon--kialo-logo')).perform()
            time.sleep(2)
            attempts += 1


def get_claim_votes(stance, level, pros_map, cons_map, depth):
    '''
    From the actual HTML page, recover some information about the claim actually selected, and search all its children
    :param stance:
    :param level:
    :param pros_map:
    :param cons_map:
    :param depth:
    '''
    try:
        claim = wd.find_element_by_class_name('selected-claim').find_element_by_class_name('claim-text__content').text
    except Exception as e:
        claim = str('Kialo discurssion: ') + wd.find_element_by_class_name('selected-claim').text
    if claim in claim_already_visited:
        return
    else:
        claim_already_visited[claim] = True
    print(claim)

    claim_container = wd.find_element_by_class_name('selected-claim-container')
    time.sleep(0.2)
    WebDriverWait(claim_container, 2000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'claim-controls__control-item--menu-button'))
    )

    comments = claim_container.find_element_by_class_name('comments-indicator').text

    button = claim_container.find_element_by_class_name('claim-controls__control-item--menu-button')
    try_click(button)
    try:
        WebDriverWait(wd, 200).until(EC.visibility_of_element_located((By.CLASS_NAME, 'context-menu__item-list')))
    except:
        claim_container.find_element_by_class_name('claim-header__impact-container').click()
        time.sleep(1)
        button.click()
    context_menu = wd.find_element_by_class_name('context-menu').find_elements_by_class_name('context-menu-item__text')

    for opt in context_menu:
        if opt.text == 'Voting Stats':
            try_click(opt)
            break

    histogram = wd.find_elements_by_class_name('voters-histogram__voters-bar-container')
    votes = []
    for count in histogram:
        votes.append(count.find_element_by_class_name('icon__counter').text)

    global dataset
    dataset = dataset.append({'Level': level, 'Stance': stance, 'Claim': claim, 'Votes': votes, 'Comments': comments, 'Depth': depth},
                             ignore_index=True)

    new_total_pros_map = wd.find_elements_by_class_name('mini-map-claim--pro')
    new_total_cons_map = wd.find_elements_by_class_name('mini-map-claim--con')
    sub_pros_map = list(set(new_total_pros_map) - set(pros_map))
    sub_cons_map = list(set(new_total_cons_map) - set(cons_map))

    index_level = 1
    for pro in sub_pros_map:
        try_click(pro.find_element_by_tag_name('rect'))
        get_claim_votes('pro', level + '.' + str(index_level), new_total_pros_map, new_total_cons_map, depth + 1)
        index_level += 1
        
    for con in sub_cons_map:
        try_click(con.find_element_by_tag_name('rect'))
        get_claim_votes('con', level + '.' + str(index_level), new_total_pros_map, new_total_cons_map, depth + 1)
        index_level += 1


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--disable-notifications')
firefox_options.add_argument('--disable-popup-blocking')
wd = webdriver.Firefox(options=firefox_options)
actions = ActionChains(wd)

'''
SELECTION OF THE DISCUSSION
'''
# wd.get("https://www.kialo.com/pro-life-vs-pro-choice-should-abortion-be-legal-5637?closeSidebar=notifications.activity")
# wd.get('https://www.kialo.com/should-conscientious-objection-to-abortion-be-banned-2851')
# wd.get('https://www.kialo.com/should-there-be-a-universal-basic-income-ubi-1634?closeSidebar=notifications.activity')
# wd.get('https://www.kialo.com/the-existence-of-god-2629')
# wd.get('https://www.kialo.com/high-speed-rail-network-europe-55592')

# RELIGION
#wd.get('https://www.kialo.com/people-should-not-follow-any-specific-religion-3371.1261?path=3371.0~3371.1261')
#wd.get('https://www.kialo.com/has-religion-been-a-good-thing-for-humanity-8539')
#wd.get('https://www.kialo.com/the-existence-of-god-2629')
wd.get('https://www.kialo.com/god-exists-3491')

# Some debates show two pop-ups before load the full debate page. So if new_to_kialo is True, those pop-ups are closed
new_to_kialo = True
if new_to_kialo:
    # Close "new to Kialo" dialog
    time.sleep(4)
    WebDriverWait(wd, 200).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pop-up-template__inner-modal-wrapper'))
    )
    wd.find_element_by_class_name('pop-up-template__inner-modal-wrapper').find_element_by_class_name('pop-up-template__close').click()

    # Close discussion dialog
    time.sleep(4)
    WebDriverWait(wd, 200).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pop-up-template__body'))
    )
    wd.find_element_by_class_name('pop-up-template__body').find_element_by_class_name('discussion-info-dialog__close').click()

# Close cookies dialog
time.sleep(5)
WebDriverWait(wd, 2000).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'toast-template__close-icon'))
)
wd.find_element_by_class_name('toast-template__close-icon').click()


main_claim = wd.find_element_by_class_name('selected-claim').find_element_by_class_name('claim-text__content').text
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

dataset = dataset.append({'Level': '1', 'Stance': 'None', 'Claim': main_claim, 'Votes': votes, 'Depth': 0}, ignore_index=True)

pros_map = wd.find_elements_by_class_name('mini-map-claim--pro')
cons_map = wd.find_elements_by_class_name('mini-map-claim--con')

index_level = 1
for pro_map in pros_map:
    pro_map.find_element_by_tag_name('rect').click()
    get_claim_votes('pro', '1.{}'.format(index_level), pros_map, cons_map, 1)
    index_level += 1

for con_map in cons_map:
    con_map.find_element_by_tag_name('rect').click()
    get_claim_votes('con', '1.{}'.format(index_level), pros_map, cons_map, 1)
    index_level += 1

dataset.to_csv('output.csv')
# dataset.to_excel('output.xlsx')
print(dataset.iloc[:-1])

wd.close()
