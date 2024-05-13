from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os, random, time, shutil
from selenium.webdriver.chrome.options import Options
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import asyncio
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import random
from openpyxl import Workbook
import requests,sys
from colorama import Fore, Style

chromium_binary_path = 'C:\\Program Files\\Chromium\\Application\\chrome.exe'  # Đường dẫn tới trình duyệt Chromium
chromium_driver_path = 'C:\\chromedriver\\chromedriver.exe'  # Đường dẫn tới Chromium WebDriver



baihat_list = [
    'SomeoneYouLoved(Cover) - 十八闲客', 'Broken Angel - DIDIT PRASETIYO','Austin - Dasha', 'Perfect - Ed Sheeran', 'Let Me Down Slowly - Alec Benjamin',
    'Instrumen Sholawat Sedih - Yuda pratama', 'Someone You Loved - Someone You Loved'
]

original_sound_value = 0  # Giá trị cho Original sound
added_sound_value = 10  # Giá trị cho Added sound
class Color:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def green(text): return Color.GREEN + text + Color.RESET
def cyan(text): return Color.CYAN + text + Color.RESET
def red(text): return Color.RED + text + Color.RESET
def bold(text): return Color.BOLD + text + Color.RESET
profile_start = int(input(red('Nhập Profile bắt đầu:')))
profile_stop = int(input(red('Nhập Profile kết thúc:')))

def click_may_congty():
    # Open VPN
    x = 1766
    y = 63
    pyautogui.click(x, y)
    time.sleep(5)
    # Start VPN
    x1 = 1632
    y1 = 265
    pyautogui.click(x1, y1)
    time.sleep(5)
    # Start VPN
    x2 = 1560
    y2 = 24
    pyautogui.click(x2, y2)
def click_may_hl():
    # Open VPN
    x = 3687
    y = 60
    pyautogui.click(x, y)
    time.sleep(5)
    # Start VPN
    x1 = 3557
    y1 = 256
    pyautogui.click(x1, y1)
    time.sleep(5)
    # Start VPN
    x2 = 3493
    y2 = 26
    pyautogui.click(x2, y2)
def click_may_home():
    # Open VPN
    x = 1740
    y = 63
    pyautogui.click(x, y)
    time.sleep(5)
    # Start VPN
    x1 = 1603
    y1 = 265
    pyautogui.click(x1, y1)
    time.sleep(5)
    # Start VPN
    x2 = 1320
    y2 = 25
    pyautogui.click(x2, y2)
for i in range(profile_start, profile_stop + 1):
    time.sleep(5)
    service = Service(executable_path=chromium_driver_path)
    options = webdriver.ChromeOptions() 
    options.binary_location = chromium_binary_path
    options.add_argument('--disable-features=AutoUpdate')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--flag-switches-begin')
    options.add_argument('--flag-switches-end')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--disable-extensions')
    options.add_argument("--lang=en")
    baihat = random.choice(baihat_list)
    print(red("""
CẢNH BÁO !
VUI LÒNG KHÔNG TÁC ĐỘNG TỚI TRÌNH DUYỆT ĐỂ TRÁNH XẢY RA LỖI KHÔNG MONG MUỐN
MỌI CHI TIẾT VUI LÒNG LIÊN HỆ : 0938.882.465
DISCORD/ZALO/TELEGRAM : Python02468
              """))
    folder_path_video = f'Profile{i}/Output Video'
    # Đường dẫn tới thư mục chứa cookies
    cookies_dir = 'Cookies'
    # Kiểm tra xem thư mục đã tồn tại chưa, nếu không, tạo thư mục
    if not os.path.exists(cookies_dir):
        os.makedirs(cookies_dir)
    folder_path_video_remove = f'Profile{i}/Output Video/remove'
    script_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(script_path)
    current_directory_video = os.path.join(current_directory, folder_path_video)
    current_directory_video_remove = os.path.join(current_directory, folder_path_video_remove)
    mp4_files = [filename for filename in os.listdir(current_directory_video) if filename.endswith(".mp4")]
    file_mp4 = random.choice(mp4_files)
    user_name = os.getlogin()
    profile_name = f'Profile {i}'
    user_data_dir = f'C:\\Users\\{user_name}\\AppData\\Local\\Chromium\\User Data\\'
    options.add_argument(f'user-data-dir={user_data_dir}')
    options.add_argument(f'profile-directory={profile_name}')
    options.add_argument(f'--profile-directory={profile_name}')
    # options.add_argument("window-size=800,600")
    print(green(f'-----> Đang mở Profile {i}'))

    # Đường dẫn tới file cookie.txt
    
    cookie_file_path = f'{cookies_dir}/cookies{i}.txt'

    # Đọc file cookie.txt
    cookies = []
    with open(cookie_file_path, 'r') as file:
        for line in file:
            if not line.startswith('#') and len(line) > 10:  # Loại bỏ các dòng comment và dòng trống
                elements = line.strip().split('\t')
                cookie = {'name': elements[5], 'value': elements[6], 'domain': elements[0], 'path': elements[2], 'secure': elements[3] == 'TRUE'}
                cookies.append(cookie)

    # # Khởi tạo WebDriver (ví dụ sử dụng Chrome)
    # driver = webdriver.Chrome()
    # Khởi tạo trình duyệt Chrome với profile đã chỉ định
    # service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service = service,options=options)
    # time.sleep(1000)
    # driver.get('https://chromewebstore.google.com/detail/urban-vpn-proxy/eppiocemhmnlbhjplcgkofciiegomcon')
    time.sleep(2)
    click_may_home()
    # nút X (rate us) Tọa độ hiện tại của chuột: (1757, 96)
    driver.get('https://www.tiktok.com/creator-center/upload?from=upload')
    # Thêm mỗi cookie vào phiên trình duyệt
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    time.sleep(3)
    driver.get('https://www.tiktok.com/creator-center/upload?from=upload')
    # driver.refresh()
    try:
        wait = WebDriverWait(driver, 500)
        iframe = wait.until(EC.visibility_of_element_located((By.XPATH, "//iframe")))
        driver.switch_to.frame(iframe)
        upload_video_xpath = "//input[@type='file']"
        upload_input = wait.until(EC.presence_of_element_located((By.XPATH, upload_video_xpath)))

        video_path = os.path.join(current_directory_video, file_mp4)
        print(green("-----> Uploading video file"))  # Sử dụng print thông thường, giả định không có định dạng màu)
        upload_input.send_keys(video_path)  # Tải video lên
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(3)
    # upload_confirmation = "//div[@title]"
    # wai_upload_confirmation = WebDriverWait(driver,500).until(EC.presence_of_element_located((By.XPATH, upload_confirmation)))

    # try:
    #     edit_button_xpath = "//div[contains(text(),'Edit video')]"
    #     edit_button = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))
    #     edit_button.click()
    #     print(Fore.GREEN + "-----> Nhấp vào nút 'Edit video'" + Style.RESET_ALL)
    # except Exception as e:
    #     print(f"Đã xảy ra lỗi: {e}")
    # try:
    #     # XPath to target the button with the specific text 'Edit video' within the given class structure
    #     edit_button_xpath = "//div[contains(text(),'Edit video')]"
    #     edit_button = WebDriverWait(driver, 500).until(
    #         EC.element_to_be_clickable((By.XPATH, edit_button_xpath))
    #     )
    #     edit_button.click()
    #     print(Fore.GREEN + "-----> Nhấp vào nút 'Edit video'" + Style.RESET_ALL)
    # except Exception as e:
    #     print(Fore.RED + f"Đã xảy ra lỗi: {e}" + Style.RESET_ALL)
    try:
        # XPath updated to target the button using its class attributes
        edit_button_xpath = "//div[contains(@class, 'edit-video-btn')]//button[contains(@class, 'css-170cvvi')]"
        edit_button = WebDriverWait(driver, 500).until(  # Adjusted timeout to a more reasonable value
            EC.element_to_be_clickable((By.XPATH, edit_button_xpath))
        )
        edit_button.click()
        print(Fore.GREEN + "-----> Nhấp vào nút 'Edit video'" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Đã xảy ra lỗi: {e}" + Style.RESET_ALL)

    time.sleep(1)
    try:
        # Sử dụng WebDriverWait để chờ đợi cho đến khi phần tử input của thanh tìm kiếm sẵn sàng
        search_input_xpath = "//input[contains(@class,'search-bar-input')]"
        wait = WebDriverWait(driver, 500)  # Thời gian chờ tối đa là 300 giây
        search_input = wait.until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))
        
        # Click vào phần tử input để chuẩn bị nhập văn bản
        search_input.click()
        search_input.send_keys(baihat)
        print(Fore.GREEN + "-----> Nhấp vào thanh tìm kiếm" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(1)
    try:
        search_button_xpath = "//div[contains(@class, 'search-bar-button')]//button[contains(@class, 'css-1sz0pc1')]"
        search_button = WebDriverWait(driver, 500) .until(EC.element_to_be_clickable((By.XPATH, search_button_xpath)))
        search_button.click()
        print(Fore.GREEN + "-----> Nhấp vào nút 'Search'" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(1)
    try:
        # Sử dụng WebDriverWait để chờ đợi cho đến khi thẻ kết quả đầu tiên xuất hiện
        first_result_xpath = "//div[contains(@class, 'music-card-container')]"
        wait = WebDriverWait(driver, 500)  # Đặt thời gian chờ tối đa là 30 giây
        first_result = wait.until(EC.element_to_be_clickable((By.XPATH, first_result_xpath)))
        
        # Nhấp vào thẻ kết quả đầu tiên
        first_result.click()

        print(Fore.GREEN + "-----> Nhấp vào thẻ kết quả đầu tiên" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(1)
    try:
        # Sử dụng WebDriverWait để chờ đợi cho đến khi nút "Use" xuất hiện và có thể nhấp được
        use_button_xpath = "//button[contains(@class, 'css-m2fcla')]//div[contains(text(), 'Use')]"
        wait = WebDriverWait(driver, 500)  # Đặt thời gian chờ tối đa là 30 giây
        use_button = wait.until(EC.element_to_be_clickable((By.XPATH, use_button_xpath)))
        
        # Nhấp vào nút "Use"
        use_button.click()

        print(Fore.GREEN + "-----> Nhấp vào nút 'Use'" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

    # time.sleep(1)
    try:
        # Sử dụng WebDriverWait để đảm bảo rằng hình ảnh trong `audioOperation` đã được tải
        wait = WebDriverWait(driver, 500)
        audio_operation_image_xpath = "//div[contains(@class, 'audioOperation')]//img[contains(@class, 'jsx-2730543169')]"
        audio_operation_image = wait.until(EC.element_to_be_clickable((By.XPATH, audio_operation_image_xpath)))
        
        # Nhấp vào hình ảnh
        audio_operation_image.click()

        print(Fore.GREEN + "-----> Nhấp vào hình ảnh để điều chỉnh âm lượng thành công" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

    # time.sleep(10)

    try:
        # Chờ cho đến khi các thanh điều chỉnh âm lượng xuất hiện
        wait = WebDriverWait(driver, 10)  # Thời gian chờ có thể điều chỉnh
        volume_ranges = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".volume-adjust-container .volume-range input[type='range']")))
        # Định nghĩa giá trị mới cho slider, giả sử bạn muốn thiết lập chúng ở giữa
        original_sound_value = 0  # Giả sử bạn muốn đặt giá trị này
        added_sound_value = 50  # Giả sử bạn muốn đặt giá trị này

        # Tính toán vị trí mới dựa trên giá trị bạn muốn đặt, ở đây giả sử chúng ta muốn đặt giữa
        for slider in volume_ranges:
            action = ActionChains(driver)
            action.click_and_hold(slider).move_by_offset((slider.size['width'] * original_sound_value / 100) - slider.size['width'] / 2, 0).release().perform()
            offset_for_added_sound = (volume_ranges[1].size['width'] * added_sound_value / 100) - volume_ranges[1].size['width'] / 2
            action.click_and_hold(volume_ranges[1]).move_by_offset(offset_for_added_sound, 0).release().perform()
        # Click vào nút lưu hoặc phần tử khác nếu cần
        # driver.find_element_by_css_selector("your_save_button_selector").click()

        print(Fore.GREEN + "Đã điều chỉnh âm lượng và cố gắng lưu."+ Style.RESET_ALL)
            
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(3)
    try:
        # Sử dụng WebDriverWait để chờ đợi cho đến khi nút "Save edit" xuất hiện và có thể nhấp được
        save_edit_button_xpath = "//button[contains(@class, 'css-ug6w5y')]//div[contains(text(), 'Save edit')]"
        wait = WebDriverWait(driver, 500)  # Đặt thời gian chờ tối đa là 30 giây
        save_edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, save_edit_button_xpath)))
        
        # Nhấp vào nút "Save edit"
        save_edit_button.click()

        print(Fore.GREEN + "-----> Nhấp vào nút 'Save edit'" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    time.sleep(3)
    try:
        # Sử dụng WebDriverWait để chờ đợi cho đến khi nút "Post" có thể nhấp được
        post_button_xpath = "//div[contains(@class, 'btn-post')]//button[contains(@class, 'css-y1m958')]"
        wait = WebDriverWait(driver, 500)  # Đặt thời gian chờ tối đa là 30 giây
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, post_button_xpath)))
        
        # Nhấp vào nút "Post"
        post_button.click()

        print(Fore.GREEN + "-----> Nhấp vào nút 'Post'" + Style.RESET_ALL)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

    # # time.sleep(10000)
    # post_button_xpath = "//div[contains(@class, 'btn-post')]"
    # post_button = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, post_button_xpath)))
    # post_button.click()
    # print(green('-----> Hoàn Tất Đăng Video'))
    # time.sleep(1)
    try:
        next_button_xpath = "//div[text()='Manage your posts']"
        next_button = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print(Fore.GREEN + "-----> Quản lý bài đăng" + Style.RESET_ALL)
        time.sleep(10)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        
    
    source_path = os.path.join(current_directory_video, file_mp4)
    destination_path = os.path.join(current_directory_video_remove, file_mp4)
    shutil.move(source_path, destination_path)
    print(red(f'-----> Video {file_mp4} đã được di chuyển vào thư mục remove.'))    
    print(green('-----> Chờ 5 giây để tiếp tục upload video tiếp theo!'))
    # time.sleep(1)
    driver.quit()





    
