#STEP 1: DOWNLOAD SELENIUM ON PIP
#STEP 2: DOWNLOAD CHROME DRIVER






#3 issues you may encounter and how to solve them:
#--System Environment Varibles setup properly and module installed via pip
#--The driver isn't the correct one for your version of firefox/chrome
#--You're using selenium 3. Many issues with opening new tabs and using keys depending on the browser, but Selenium 4 sidesteps those issues. Use the documentation website.

#Help From this Selenium learning Playlist:
#https://www.youtube.com/watch?v=zIrs8FtLnIs

from selenium import webdriver

#ask for search input
search = input("Search Query:")

#ensure the driver version matches your version of chrome
driver=webdriver.Chrome(executable_path=r"C:\Users\JP\Downloads\chromedriver_win32(1)\chromedriver.exe")

#First Window Opens
driver.get('https://www.youtube.com/channel/UCkefXKtInZ9PLsoGRtml2FQ/search?query='+ search)

#open & switch to new tab, then travel to url

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCWIEIMHXyJ62RF4aVmU30og/search?query='+search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g/featured/search?query='+search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCCEq30wPW7HYbisawxNtmPw/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCwTH3RkRCIE35RJ16Nh8V8Q/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCVPjtOVcnKaSRI8IO3KSetA/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UC_M-iWYpQbgo4rK1YfewI5w/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/user/schafer5/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UC68KSmHePPePCjW4v57VPQg/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UChkws8rD7PNNITF17q1wOCw/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCw5aSIOFmapIcmAvEpaAUrQ/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UC3s0BtrBJpwNDaflRSoiieQ/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UC3sccPO4v8YqCTn8sezZGTw/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UC0ArlFuFYMpEewyRBzdLHiw/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/channel/UCxQKHvKbmSzGMvUrVtJYnUA/search?query=' +search)

driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/user/homergfunk/search?query=' +search)
