import requests
import json
import csv
def get_linkedin_data_api(first_name, last_name):
    access_token = 'AQXS4xLxknpFdIFhhlzRjc6i-FsSVAxjLUzZn1Sv8gGO-hj_045xI6gIezhCRZ--12DNtL-jGbblETV091UnMWYHvt0t-qe9IU4XCn3B8Sa49PgMqXjUYvib9MHHaoP3beuOaamEs2sMXDCJdhmRfb4Dc5yMKdrch5F8IIBfLIPtr6dVil_b2YPYCbc6W7uoC4eq2QuR1q_wiY2m5RogAWz0DdaK0SxdnjFWyD0Iim9Clu9I0-YJ95LdWGn21UTM8uHT8ZtyxMJpV_ruWn3zzd1QrzTIdp1S3Ci9ZjW8YdVrR0FqT35fKEcvZcM5u6xPNwHmTbmhBRh9mGWTL6TPqVDHAjHk0Q'
    url = f'https://api.linkedin.com/v2/people-search?q={first_name} {last_name}&count=10'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
    }
    try:
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        # Extracting data from API response
        user_data = []
        for person in data.get('elements', [])[:5]:
            user_data.append({
                'Name': f"{person.get('firstName')} {person.get('lastName')}",
                'Headline': person.get('headline', ''),
                'Location': person.get('location', {}).get('preferredGeoPlaceName', ''),
                'Public Profile URL': person.get('publicIdentifier', ''),
            })
        return user_data
    except Exception as e:
        print(f"Error: {e}")
        return None
def save_to_csv(data, file_path):
    # Saving data to CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
#Search
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
linkedin_data = get_linkedin_data_api(first_name, last_name)
save_to_csv(linkedin_data, 'Output.csv')
