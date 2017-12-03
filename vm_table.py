#! /bin/bash
import csv
import gzip 
import sys
from collections import defaultdict

def map_vm_to_cpu(fname):
    max_cpu_count = 0
    min_cpu_count = 100
    vm_to_cpu = defaultdict(list);
    cpu_pop = []
    if fname.endswith('.csv.gz'):
        with gzip.open(fname, "r") as csvDataFile:
            vm_table = csv.reader(csvDataFile)
            for vm in vm_table:
                n_cpu = int(vm[9])
                vm_to_cpu[vm[0]].append(n_cpu);
                if max_cpu_count < n_cpu:
                    max_cpu_count = n_cpu
                
                if n_cpu < min_cpu_count:
                    min_cpu_count = n_cpu;
                
                cpu_pop.append(n_cpu)
                
            return vm_to_cpu, max_cpu_count, min_cpu_count, cpu_pop;
    
    if fname.endswith('.csv'):
        with open(fname, "r") as csvDataFile:
            vm_table = csv.reader(csvDataFile)
            return vm_to_cpu;
    print ("incorrect file formate: expect csv.gz or csv. file name: " + fname);
    
#def workload_generate(fname):
#    if fname.endswith('.csv.gz'):
#        with gzip.open(fname, "r") as csvDataFile:
#            #open a csv writer
#            vm_table = csv.reader(csvDataFile)
#            for vm in vm_table:
#                         
#    
#    if fname.endswith('.csv'):
#        with open(fname, "r") as csvDataFile:
#            vm_table = csv.reader(csvDataFile)
#            return vm_to_cpu;
#    print ("incorrect file formate: expect csv.gz or csv. file name: " + fname);