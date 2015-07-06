'''
Created on May 20, 2015

@author: Oli
'''
import sys
import os
import numpy as np
import csv
import pandas as pd
# import str




sys.path.append('/Users/Oli/work/python/minions')




from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data
from ana_res import ana_res

a = ana_data()
ar = ana_res()
g = gen()
l = log_files()
i = imp() 
p = plotter()
# d = data()
# c = csv_list()


cwd = '/Users/Oli/work/dBLM_readout/LHC_data_analysis_scope'
test_env='/Users/Oli/work/dBLM_readout/LHC_data_analysis_scope_test_env'
# cwd = test_env
data_fold = 'data'
plot_fold = 'plots' 
ana_res_fold = 'ana_res' 

data_path  = '/Users/Oli/work/dBLM_readout/IP2/data/data'
data_test_env  = '/Users/Oli/work/dBLM_readout/IP2/data_test_env/data'
# data_path  = data_test_env
# data_path = os.path.join(cwd,data_fold)



# data_path = os.path.join(cwd,data_fold)
plot_path = os.path.join(cwd,plot_fold)
ana_res_path = os.path.join(cwd,ana_res_fold) 


l.log_file_set(cwd,'log')
  
f = open(l.log_path(),'a')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)


pflag=1

ana_file_save_interval = 5


g.printer(data_path,pflag)

i.path(data_path,pflag)
i.path_check(pflag)
i.data_list_creator('.txt',pflag)
p.set_save_path(plot_path,pflag)
ar.infrastruc(ana_res_path,pflag)


header=[['time_stamp','year','month','day','hour','minute','second','time sec','time zero',
         'delta time zero','beam','ip','loc','dcum','type','daq_name','channel','mode','beamstatus',
         't total','t start','t end','t delta','offset','offset_corr','noise','sig 10 pt','sig 10 t','sig 50 pt','sig 50 t','run','analysed',
         'file_name','file_name_path']]

scope_conf = [['daq_name'        ,'ip'   ,'beam' ,'loc'  ,'dcum'     ,'type','channel','name'],
             ['cfo-ua23-bhascp_C1' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','1','cfo-ua23-bhascp'],
             ['cfo-ua23-bhascp_C2' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','2','cfo-ua23-bhascp'],
             ['cfo-ua23-bhascp_C3' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','3','cfo-ua23-bhascp'],
             ['cfo-ua23-bhascp_C4' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','4','cfo-ua23-bhascp'],
             ['cfo-us65-bhascp_C1' ,'6'    ,'1'    ,'2'    ,'16505.55'  ,'CIVIDEC','1','cfo-us65-bhascp'],
             ['cfo-us65-bhascp_C2' ,'6'    ,'1'    ,'2'    ,'16505.55'  ,'CIVIDEC','2','cfo-us65-bhascp'],
             ['cfo-us65-bhascp_C3' ,'6'    ,'2'    ,'2'    ,'16817.86'  ,'CIVIDEC','3','cfo-us65-bhascp'],
             ['cfo-us65-bhascp_C4' ,'6'    ,'2'    ,'2'    ,'16817.86'  ,'CIVIDEC','4','cfo-us65-bhascp'],
             ['cfo-ua87-bhascp_C1' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','1','cfo-ua87-bhascp'],
             ['cfo-ua87-bhascp_C2' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','2','cfo-ua87-bhascp'],
             ['cfo-ua87-bhascp_C3' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','3','cfo-ua87-bhascp'],
             ['cfo-ua87-bhascp_C4' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','4','cfo-ua87-bhascp']
             ]
 
ar.header_set(header,pflag)
# print ar.haeder
print i.data_list
ar.int_data_sets = ar.file_setup(ana_res_path,'int_data_sets.csv',pflag)
# print ar.file_setup(ana_res_path,'ana_file.csv',pflag)
ar.ana_file =  ar.file_setup(ana_res_path,'ana_file.csv',pflag)
ar.ana_file_updater(i.data_list,pflag)
ar.ana_file_saver(1,pflag)# print ar.ana_file
# print ar.int_data_sets
print ar.ana_file
# sys.exit('stop')
# ar.ana_file_check(0,pflag)
# ar.ana_file_loader(pflag)
# ar.ana_file_writer(i.data_list,pflag)
# ar.ana_file_saver(1,pflag)

# sys.exit('stop')
max_it = len(ar.ana_file)
force_flag = 0
# max_it = 2
# print ar.ana_file[0]

a.header(ar.ana_file[0],pflag)


# sys.exit('stop')
for k in range(1,max_it):
# for k in range(len(i.data_list)):
    g.loop_info(k,i.len_data_list,pflag)
    print ar.ana_file[k]
    line = ar.ana_file[k]
    ana_flag = a.tba_check(line,force_flag,pflag)
    g.printer(ana_flag,pflag)
    if ana_flag == 1:
        g.tprinter('start analysis',pflag)
        a.name_info_scope(line,scope_conf,pflag)
        a.time_cor(line,pflag)
         
# #         break
        a.data_loader(line,pflag)
        
        a.data_check(pflag)
        a.time_info(line,a.data,pflag)
        a.offset_corr(line,a.data,pflag)
        a.noise_finder(line,a.data,pflag)
        a.sig_above(line,a.data,10,pflag)
        a.sig_above(line,a.data,50,pflag)
        
#         p.simple_plotter(line,a.data,a.header,1,pflag)
        p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-6,1e-6,1,pflag)
        p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-7,5e-7,1,pflag)
        p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-6,100e-6,1,pflag)
#         a.bin_time_cor(pflag)
#         a.c_counter(line,pflag)
#         a.set_t_zero(line,pflag)
#         a.time_sec(line,pflag)
#         a.delta_time_zero(line,pflag)
#         a.dc_counter(line,pflag)
#         a.dt_counter(line,pflag)
        
#         name ='test.pdf'
#         hp.shist(a.data,1,plot_path,a.time_stamp+'_'+a.daq_name,pflag)

#         a.t_delta(line,a.data,pflag)
#         a.offset_corr(line,a.data,pflag)
#         a.noise_finder(line,a.data,pflag)
#         a.max_finder(line,a.data,pflag)
    else:
        pass
    
    
    a.analysed(ar.ana_file[k],pflag)

# ar.int_data_cond(line,'sig 50 pt',1,1,pflag)
# ar.file_saver(ana_res_path,'int_data_sets.csv',pflag) 
ar.ana_file_saver(1,pflag)   
    
# for i in ar.ana_file:
#     print i    
#     i.data_importer(i.data_list[k][0],pflag)
#     p.set_save_path(plot_path,pflag)
# #     for q in range(10):
# #         print i.data[q,3:]
#     p.simple_plotter(i.data[:,3:],i.data_list[k][1],0,pflag)
#     max_y_index=a.max_find(i.data[:,3:],1,pflag)
#     p.zoom_plotter(i.data[:,3:],i.data_list[k][1],max_y_index,1000,0,pflag)
#     print a.trig_finder(i.data[:,3:],1,2,pflag)






# plot_path = os.path.join(cwd,plot_fold)
# ana_res_path = os.path.join(cwd,ana_res_fold) 
# 
# 
# l.log_file_set(cwd,'log')
#   
# f = open(l.log_path(),'a')
# original = sys.stdout
# sys.stdout = Tee(sys.stdout, f)
# 
# 
# pflag=1
# ana_file_save_interval = 5
# 
# 
# g.printer(data_path,pflag)
# 
# i.path(data_path,pflag)
# i.path_check(pflag)
# 
# i.data_list_creator('.txt',pflag)
# p.set_save_path(plot_path,pflag)
# ar.infrastruc(ana_res_path,pflag)
# ar.ana_file_check(pflag)
# ar.ana_file_loader(pflag)
# ar.ana_file_writer(i.data_list,pflag)
# ar.ana_file_saver(1,pflag)
# 
# # sys.exit('stop')
# max_it = len(ar.ana_file)
# print ar.ana_file[0]
# 
# a.header(ar.ana_file[0],pflag)
# # sys.exit('stop')
# for k in range(1,max_it):
# # for k in range(len(i.data_list)):
#     g.loop_info(k,i.len_data_list,pflag)
#     print ar.ana_file[k]
#     line = ar.ana_file[k]
#     ana_flag = a.tba_check(line,1,pflag)
#     if ana_flag == 1:
#         g.tprinter('start analysis',pflag)
#         a.name_info(line,pflag)
#         a.data_loader(line,pflag)
#         a.data_check(a.data,pflag)
#         a.t_delta(line,a.data,pflag)
#         a.offset_corr(line,a.data,pflag)
#         a.noise_finder(line,a.data,pflag)
#         a.max_finder(line,a.data,pflag)
#     else:
#         pass
#     
#     
#     a.analysed(ar.ana_file[k],pflag)
#  
# ar.ana_file_saver(1,pflag)   
#     
# # for i in ar.ana_file:
# #     print i    
# #     i.data_importer(i.data_list[k][0],pflag)
# #     p.set_save_path(plot_path,pflag)
# # #     for q in range(10):
# # #         print i.data[q,3:]
# #     p.simple_plotter(i.data[:,3:],i.data_list[k][1],0,pflag)
# #     max_y_index=a.max_find(i.data[:,3:],1,pflag)
# #     p.zoom_plotter(i.data[:,3:],i.data_list[k][1],max_y_index,1000,0,pflag)
# #     print a.trig_finder(i.data[:,3:],1,2,pflag)











