from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

def linkedin_data_browser(first_name, last_name):
    url = f'https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}&origin=GLOBAL_SEARCH_HEADER'
    try:
        # browser Setup 
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)

        # Extracting data from the search results
        user_data = []
        results = driver.find_elements(By.CSS_SELECTOR, '.search-result')
        for result in results[:5]:
            name = result.find_elements(By.CSS_SELECTOR, '.actor-name').text
            headline = result.find_elements(By.CSS_SELECTOR, '.subline-level-1').text
            location = result.find_elements(By.CSS_SELECTOR, '.subline-level-2').text
            public_profile_url = result.find_elements(By.CSS_SELECTOR, 'a.search-result__result-link').get_attribute('href')

            user_data.append({
                'Name': name,
                'Headline': headline,
                'Location': location,
                'Public Profile URL': public_profile_url,
            })

        return user_data

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the browser
        driver.quit()

# Example usage:
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

linkedin_data = linkedin_data_browser(first_name, last_name)
if linkedin_data:
    save_to_csv(linkedin_data, 'linkedin_browser_output.csv')
