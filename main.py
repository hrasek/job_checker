import startupjobs
import filters
key_list = ['name', 'company', 'locations','shifts', 'seniorities', 'isRemote']
job_list = startupjobs.get_current(key_list)
job_list = filters.place(job_list, key_list)
job_list = filters.shift(job_list, key_list)
job_list = filters.seniority(job_list, key_list)
print(job_list)