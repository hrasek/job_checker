def place(jobs_list, key_list) -> list:
    locations = key_list.index('locations')
    remote =  key_list.index('isRemote')
    filtered_list = []
    for job in jobs_list:
        if 'Brno' in job[locations] or job[remote] == True:
            filtered_list.append(job) 
    return filtered_list

def shift(jobs_list, key_list) -> list:
    shifts = key_list.index('shifts')
    filtered_list = []
    for job in jobs_list:
        if 'Full-time' in job[shifts]:
            filtered_list.append(job)
    return filtered_list

def seniority(jobs_list, key_list) -> list:
    seniorities = key_list.index('seniorities')
    filtered_list = []
    for job in jobs_list:
        if 'junior' in job[seniorities]:
            filtered_list.append(job)
    return filtered_list    