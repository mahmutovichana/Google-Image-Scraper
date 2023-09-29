# Google Image Scraper

## Description
This Python script allows you to scrape images from Google Images based on a specified search query and save them to your local machine. It utilizes Selenium and the Edge web browser to automate the image retrieval process.

**Purpose:** The primary goal of this project is to create a dataset for training machine learning and artificial intelligence models in an automated manner.

## Usage

Clone this repository to your local machine:
```bash
git clone https://github.com/mahmutovichana/Google-Image-Scraper.git
```
Navigate to the project folder:
``` bash
cd Google-Image-Scraper
```
Install the required Python packages:
``` bash
pip install -r requirements.txt
```
Update the query variable in the googleImageScraper.py file with your desired search query.

Run the script:
``` python
python googleImageScraper.py
```

Images matching your query will be downloaded and saved to a folder on your desktop.

Dependencies:
- Python 3.x
- Selenium
- Pillow (PIL)
- Microsoft WebDriver (Ensure it's compatible with your Edge browser version)
