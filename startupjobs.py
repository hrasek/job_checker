import requests

def get_current(key_list) -> list:
    link = "https://www.startupjobs.cz/api/offers?shift[]=full-time&seniority[]=junior&area[]=vyvoj&location[]=ChIJEVE_wDqUEkcRsLEUZg-vAAQ&salary[]=1&salaryRange[]=%7B%22value%22:%2250000%22,%22currency%22:%22CZK%22,%22measure%22:%22monthly%22%7D&page=1"
    
    i=1
    jobs_list = []
    while True:
        try:
            link = link[0:-1] + str(i)
            r = requests.get(link)
            a = r.json()
            result = a['resultSet']
            for item in result:
                row = []
                for key in key_list:
                    row.append(item[key])
                jobs_list.append(row)
            i+=1
        except:
            break
    return jobs_list