import requests


link = "https://www.startupjobs.cz/api/offers?shift[]=full-time&seniority[]=junior&area[]=vyvoj&location[]=ChIJEVE_wDqUEkcRsLEUZg-vAAQ&salary[]=1&salaryRange[]=%7B%22value%22:%2250000%22,%22currency%22:%22CZK%22,%22measure%22:%22monthly%22%7D&page=3"
r = requests.get(link)
a = r.json()
result = a['resultSet']

for item in result:
    print(item['id'], item.keys())
