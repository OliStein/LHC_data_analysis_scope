'''
Created on Jun 1, 2015

@author: Oli
'''
import os
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import shutil as st
import pickle 
from time import strftime, localtime, time
import time
import glob

sys.path.append('/Users/Oli/work/python/minions')

from csv_list_class import csv_list
from gen_class import gen
from list_class import lists

l = lists()
c = csv_list()
g = gen() 

class ana_res():
    
    
    def infrastruc(self,path,pflag):
        g.tprinter('Running infrastruc',pflag)
        if os.path.exists(path) is not True:
            g.printer('Creating ana_res path',pflag)
            
            os.mkdir(path)
        else:
            g.printer('Ana_res path exists',pflag)
        g.printer('ana_res_path',pflag)
        g.printer(path,pflag)
        self.ana_res_path = path 
    
    def ana_file_check(self,pflag):
        g.tprinter('Running ana_file_check',pflag)
        self.ana_file_name = os.path.join(self.ana_res_path,'ana_file.csv')
        if os.path.isfile(self.ana_file_name) is True:
            g.printer('Found ana_file',pflag)
#             self.ana_file = c.csv_file_loader(self.ana_res_path,'ana_file.csv',pflag) 
        else:
            g.printer('No ana_file found',pflag)
            self.ana_file_creator(1,pflag)
            
    def ana_file_creator(self,flag,pflag):
        g.tprinter('Running ana_file_creator',pflag)
        header=[['time_stamp','meas_nr','daq_name','channel','t_delta','t_length','offset','offset_corr','noise','analysed','file_name','file_name_path']]
        print self.ana_res_path
        c.csv_file_saver(self.ana_res_path,'ana_file.csv',header,flag,pflag)
              

    def ana_file_loader(self,pflag):
        g.tprinter('Runningh ana_file_loader',pflag)
        self.ana_file = c.csv_file_loader(self.ana_res_path,'ana_file.csv',pflag)
        
    def ana_file_saver(self,flag,pflag):
        g.tprinter('Running ana_file_saver',pflag)
        c.csv_file_saver(self.ana_res_path,'ana_file.csv',self.ana_file,flag,pflag)
           
    def ana_file_writer(self,dlist,pflag):
        g.tprinter('Running ana_file_writer',pflag)
        for i in dlist:
            print i[0]
            if str(i[0]) in np.array(self.ana_file):
                g.printer(str(i)+' is in ana_file',pflag)
                pass
            else:
                g.printer(str(i[0])+' is not in ana_file',pflag)
                nline = [0]*len(self.ana_file[0])
                nline[l.find_val('file_name',self.ana_file[0],0)] = i[-1]
                nline[l.find_val('file_name_path',self.ana_file[0],0)] = i[-2]
                self.ana_file.append(nline)
#                 print nline
                
            
                
                
                
           
