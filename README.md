
# Automated Product Screenshots

Automated Product Screenshots is a Python project that utilizes the Selenium library to access a website, perform a search, and capture screenshots of the resulting products. The project incorporates automated scrolling to ensure all products are captured.
## Features

- Automates the process of accessing a website, performing a search, and capturing screenshots of products.
- Uses the Selenium library to interact with the website and perform actions programmatically.
- Implements automated scrolling to capture all products appearing in the search results.
- Allows customization for search keywords and the destination folder to save the captured screenshots.
- Provides a simple and straightforward way to automate the process of capturing product screenshots for further analysis or documentation.
## Installation

1. Clone the repository:

```bash
git clone git@github.com:OcamaAslam/Automated-Product-Screenshots.git
```
2. Navigate to the project directory:
```bash
cd automated-product-screenshots
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Navigate to the project directory:
```bash
cd automated-product-screenshots
```
## Deployment

Set the Chrome driver path in config.py according to your file structure:

```bash
s = Service("{your file path}/Automated Product Screenshots/Chrome Driver/chromedriver.exe")
```


## Usage/Examples
- Modify the config.py file to specify the target website, search keyword, destination folder for saving the screenshots, and any other required configurations.

- Run the main script:
```python
python main.py

```
- The script will automate the process of accessing the website, performing the search, and capturing the product screenshots. The screenshots will be saved in the specified destination folder "/SS".

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ocama-mohamed/)
