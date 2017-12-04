#! /bin/bash

import csv
import vm_table
import gzip
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


vm_to_cpu, max_cpu_count, min_cpu_count, cpu_cnt  = vm_table.map_vm_to_cpu('data/vmtable.csv.gz')
print("Number of VMS: "+ str(len(vm_to_cpu.items())))
print("Minimum CPU Count: "+ str(min_cpu_count) + ", Maximum CPU Count: "+ str(max_cpu_count));

num_bins = 5
n, bins, patches = plt.hist(cpu_cnt, num_bins, facecolor='blue', alpha=0.5)
plt.show()
pp = PdfPages('cpucount-hist.pdf')
pp.savefig(plt.figure())
# 1. read one cpu file 
# 2. scale the usage with sigma(max_util*cpu_count)/sigma(cpu_count)
with gzip.open('data/vm_cpu_readings-file-1-of-125.csv.gz', "r") as csvDataFile:
    ts_cpu_util = [0 for x in range(100)]
    vm_cpu = csv.reader(csvDataFile)
    ts = int(next(vm_cpu)[0]);
    csvDataFile.seek(0)
    sigma_max_util = 0;
    total_cpus = 0;
    for vm in vm_cpu:
        if not int(vm[0]) == ts:
            ts_cpu_util[ts/300] = sigma_max_util/total_cpus;
            sigma_max_util = 0;
            total_cpus = 0;
            ts = int(vm[0]);                                                                                                                                                                                                                                        
        n_cpu = vm_to_cpu[vm[1]][0];
        sigma_max_util += (float(n_cpu)*float(vm[3]));
        total_cpus += n_cpu;
    
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(ts_cpu_util, 'r--', [max_cpu_count*100]*100, 's');
    
    ax2.plot(ts_cpu_util);
    plt.show();
    
    sigma_max_util = 0;
    