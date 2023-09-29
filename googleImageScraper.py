import os
import io
import time
import base64  
import requests
from PIL import Image
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Enter query for Google search
query = "plastic"

# Convert the query into URL format
query_url = quote(query)

# Specify the desired folder path on the desktop
folder_name = os.path.join('C:\\Users\\mahmu\\OneDrive\\Desktop', query)

try:
    # Create the folder if it doesn't exist
    os.makedirs(folder_name)
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Initialize the Edge web browser using options and a service
driver = webdriver.Edge(r"C:\Users\mahmu\MicrosoftWebDriver.exe")

# URL for Google Images search
url = f"https://www.google.com/search?q={query_url}&tbm=isch"

# Open the URL in the web browser
driver.get(url)

# Simulate scrolling to load more images
for _ in range(10):  # Adjust the number based on the number of images wanted
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for images to load

try:
    # Find all image elements
    img_elements = driver.find_elements_by_css_selector('img.rg_i')
    print(img_elements)
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Download and save images
for i, img in enumerate(img_elements):
    img_url = img.get_attribute("src")
    if img_url and img_url.startswith('http'):
        img_response = requests.get(img_url)
        img_name = f"{i + 1}.jpg"  
        img_path = os.path.join(folder_name, img_name)

        # Save the image to computer
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    elif img_url and img_url.startswith('data:image/jpeg;base64'):
        # Decode base64 image data and save it
        img_data = img_url.split('base64,')[1]
        img = Image.open(io.BytesIO(base64.b64decode(img_data)))
        img_name = f"{i + 1}.jpg"  
        img_path = os.path.join(folder_name, img_name)
        img.save(img_path)

print(f"Images have been downloaded and saved in the folder: {folder_name}")

# Close the web browser
driver.quit()
