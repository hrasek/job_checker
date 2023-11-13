import requests
from typing import Any

def get_current() -> list[dict[str, Any]]:
    link = "https://www.startupjobs.cz/api/offers?shift[]=full-time&seniority[]=junior&area[]=vyvoj&location[]=ChIJEVE_wDqUEkcRsLEUZg-vAAQ&salary[]=1&salaryRange[]=%7B%22value%22:%2250000%22,%22currency%22:%22CZK%22,%22measure%22:%22monthly%22%7D&page=1"
    i=1
    jobs_list: list[dict[str, Any]] = []
    while True:
        try:
            link = link[0:-1] + str(i)
            response = requests.get(link)
            response_dict = response.json()
            results: list[dict[str, Any]] = response_dict['resultSet']
            jobs_list.append(results)
            i+=1
        except:
            break
    return jobs_list