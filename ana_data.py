'''
Created on May 21, 2015

@author: Oli
'''
import sys
import os
import numpy as np
# import str









from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from list_class import lists

l = lists()
g = gen()
# l = log_files()
i = imp() 
p = plotter()


class ana_data():
    
    def header(self,header,pflag):
        self.header = header
        self.pass_flag = 0
        print self.header
        
    def tba_check(self,line,fflag,pflag):
        g.tprinter('Running tba_check',pflag)
        if line[l.find_val('analysed',self.header,0)] == str(1):
            g.printer('file is analysed',pflag)
            if fflag == 1:
                g.printer('Forced analysis',pflag)
                return 1
            else:
                return 0
        else:
            g.printer('file needs to be analysed',pflag)
            return 1
    
    def name_info(self,line,pflag):
        g.tprinter('Running name_info',pflag)
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.daq_name = self.fname_list[1]
        self.time_stamp = self.fname_list[0]
        self.channel = self.fname_list[2]
        self.meas_nr = self.fname_list[3] 
        
        g.printer('time stamp: '+str(self.time_stamp),pflag)
        g.printer('meas nr: '+str(self.meas_nr),pflag)
        g.printer('daq name: '+str(self.daq_name),pflag)
        g.printer('channel: '+str(self.channel),pflag)
        
        line[l.find_val('time_stamp',self.header,0)] = self.time_stamp
        line[l.find_val('meas_nr',self.header,0)] = self.meas_nr
        line[l.find_val('daq_name',self.header,0)] = self.daq_name
        line[l.find_val('channel',self.header,0)] = self.channel
#         print self.fname_list    
        
        
    def data_loader(self,line,pflag):
        g.tprinter('Running data_loader',pflag)
        if self.pass_flag ==0:
            dp = line[l.find_val('file_name_path',self.header,0)]
            try:
                self.data = np.loadtxt(dp,delimiter=',')
                g.printer('Data loaded',pflag)
            except:
                g.printer('No data loaded',pflag)
                self.pass_flag = 1
        else:
            g.printer('pass_flag = 1, skip',pflag)
            pass
    
    def data_check(self,data,pflag):
        g.tprinter('Running data_check',pflag)
        if self.pass_flag == 0:
            try:
                self.data[0]
                print len(self.data[0])
                if len(self.data[0]) == 2:                
                    self.pass_flag = 0
                    g.printer('data ok',pflag)
                else:
                    g.printer('data not ok')
                    self.pass_flag = 1
            except:
                self.pass_flag = 1
                g.printer('data not ok',pflag)
            
        else:
            g.printer('pass_flag = 1, skip',pflag)
            pass
        
        
    def t_delta(self,line,data,pflag):
        g.tprinter('Running t_delta',pflag)
        if self.pass_flag == 0:
            print self.data[1,0]-self.data[0,0]
            line[l.find_val('t_delta',self.header,0)] = self.data[1,0]-self.data[0,0]
            line[l.find_val('t_length',self.header,0)] = (self.data[1,0]-self.data[0,0])*len(self.data)
            
        else:
            g.printer('pass_flag = 1, skip')
            pass
        
    def offset_corr(self,line,data,pflag):
        g.tprinter('Running offset_corr',pflag)
        if self.pass_flag ==0:
            len_data = int(round(len(self.data)*.05))-1
#             print len_data
                          
            self.offset = np.mean(self.data[-len_data:,1])
            g.printer('Offset: '+str(self.offset),pflag)
            for i in self.data:
                i[1]=i[1]-self.offset
                
              
            line[l.find_val('offset',self.header,0)] =self.offset
            line[l.find_val('offset_corr',self.header,0)] =1
            offset = np.mean(self.data[-len_data:,1])
            g.printer('New offset: '+str(offset),pflag)  
            
        else:
            g.printer('pass_flag = 1, skip')
            pass
            
    
    def noise_finder(self,line,data,pflag):
        g.tprinter('Running noise_finder',pflag)
        if self.pass_flag==0:
            len_data = int(round(len(self.data)*.05))-1
            noise_min=np.min(self.data[:len_data,1])
            noise_max=np.max(self.data[:len_data,1])
            g.printer('noise min: '+str(noise_min),pflag)
            g.printer('noise max: '+str(noise_max),pflag)
            self.noise = np.max(self.data[:len_data,1])-np.min(self.data[:len_data,1])
            g.printer('noise level: '+str(self.noise),pflag)
            line[l.find_val('noise',self.header,0)] =self.noise
        else:
            g.printer('pass_flag = 1, skip')
            pass 
    
    
    def max_finder(self,line,data,pflag):
        g.tprinter('Running max_finder',pflag)
        if self.pass_flag ==0:
            self.max_list=[]
            
            
            pass
        
        
        else:
            g.printer('pass_flag =1, skip')
            pass    
        
                
    def analysed(self,line,pflag):
        g.tprinter('Setting line to analysed',pflag)
        line[l.find_val('analysed',self.header,0)] = 1
        
        
    def max_find(self,data,n,pflag):
        maxind = np.argmax(data,)
        return maxind
        
        
    def trig_finder(self,data,nup,ndow,pflag):
        g.tprinter('Running trig_finder',pflag)
        trig = np.argwhere(data[0:,0] == 0)
        return trig
        
        