import os
import requests
import shutil
import platform

def download_edgedriver():
    try:
        # Determine the OS and architecture to construct the download URL
        system = platform.system().lower()
        architecture = platform.architecture()[0][:2]  # '32' or '64'

        # Define the WebDriver version based on your Edge browser version
        driver_version = 'latest'  # or specify a specific version like '93.0.961.52'

        # Construct the download URL
        driver_url = f'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads'

        # Destination directory for the WebDriver
        webdriver_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Create the destination directory if it doesn't exist
        os.makedirs(webdriver_dir, exist_ok=True)

        # Download the WebDriver executable
        print(f'Downloading Edge WebDriver from: {driver_url}')
        response = requests.get(driver_url, stream=True)
        if response.status_code == 200:
            # Save the downloaded file
            webdriver_exe_path = os.path.join(webdriver_dir, f'msedgedriver_{system}.exe')
            with open(webdriver_exe_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            
            print(f'Downloaded WebDriver to: {webdriver_exe_path}')

            # Clean up: close the response object
            response.close()

            # Move the WebDriver executable to the desired path
            final_webdriver_path = os.path.join(webdriver_dir, 'msedgedriver.exe')
            shutil.move(webdriver_exe_path, final_webdriver_path)

            print(f'Moved WebDriver to: {final_webdriver_path}')

        else:
            print(f'Failed to download WebDriver. Status code: {response.status_code}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    download_edgedriver()
