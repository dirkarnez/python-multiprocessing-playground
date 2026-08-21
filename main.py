# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import multiprocessing
import time
from ctypes import CDLL
libc = CDLL("libc.so.6")

# from ctypes import Structure, byref, windll, wintypes

# class PROCESSOR_NUMBER(Structure):
#     _fields_ = [("Group", wintypes.WORD), ("Number", wintypes.BYTE), ("Reserved", wintypes.BYTE)]
# pn = PROCESSOR_NUMBER()
# windll.kernel32.GetCurrentProcessorNumberEx(byref(pn))
# print(f"Running on Core ID: {pn.Number}")

def heavy_computation(n):
    print(f"Running on Core ID: {libc.sched_getcpu()}")
    # A CPU-bound task that will run on an individual core
    return sum(i * i for i in range(n))
  
def main():
    numbers = [10_000_000, 10_000_000, 10_000_000, 10_000_000]
    
    # 1. Determine how many cores the machine has
    # Typically returns logical processors (including hyperthreading)
    core_count = multiprocessing.cpu_count() 
    print(f"Spawning pool across {core_count} available CPU cores...")

    # 2. Open a worker pool. Leaving it blank defaults to your total core count.
    with multiprocessing.Pool(processes=core_count) as pool:
        # 3. Map the workload. 
        # The pool splits the list and assigns items to separate processes/cores.
        start_time = time.time()
        results = pool.map(heavy_computation, numbers)
        end_time = time.time()
        
    print(f"Results: {results}")
    print(f"Parallel execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()

