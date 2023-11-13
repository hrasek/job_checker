import startupjobs
import filters

job_list = startupjobs.get_current()
job_list = filters.place(job_list)
job_list = filters.shift(job_list)
job_list = filters.seniority(job_list)
print(job_list)
print(len(job_list))