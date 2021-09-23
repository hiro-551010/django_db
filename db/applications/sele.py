from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Chromeを起動する関数
def set_driver(headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()
    

    # ヘッドレスモード（画面非表示モード）の設定
    if headless_flg == True:
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与


    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(ChromeDriverManager().install(), options=options)

# main処理
def main():
    # driverを起動
    driver = set_driver(True)
    driver.get('https://google.com')
    # Webサイトを開く
    driver.get("https://www.twitch.tv/")

