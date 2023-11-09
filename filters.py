from typing import Any

def place(jobs_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered_list: list[dict[str, Any]] = []
    for job in jobs_list:
        if 'Brno' in job['locations'] or job['isRemote'] == True:
            filtered_list.append(job) 
    return filtered_list

def shift(jobs_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered_list: list[dict[str, Any]] = []
    for job in jobs_list:
        if 'Full-time' in job['shifts']:
            filtered_list.append(job)
    return filtered_list

def seniority(jobs_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered_list: list[dict[str, Any]] = []
    for job in jobs_list:
        if 'junior' in job['seniorities']:
            filtered_list.append(job)
    return filtered_list    