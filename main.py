# '''
# Created on May 20, 2015
# 
# @author: Oli
# '''
# import sys
# import os
# import numpy as np
# import csv
# import pandas as pd
# # import str
# 
# 
# 
# 
# sys.path.append('/Users/Oli/work/python/minions')
# 
# 
# 
# 
# from log_file_setup import log_files
# # from analysis_modules import data
# from log_file_setup import Tee
# import matplotlib.pyplot as plt
# from gen_class import gen
# from data_import import imp
# from plotter_class import plotter
# from ana_data import ana_data
# from ana_res import ana_res
# 
# a = ana_data()
# ar = ana_res()
# g = gen()
# l = log_files()
# i = imp() 
# p = plotter()
# # d = data()
# # c = csv_list()
# 
# # Main path for sub folder 
# cwd = '/Users/Oli/work/dBLM_readout/LHC_data_analysis_scope'
# 
# # Path for test enviroment 
# test_env='/Users/Oli/work/dBLM_readout/LHC_data_analysis_scope_test_env'
# 
# # uses test enviroment as current working directory
# # cwd = test_env
# 
# # Subfolders with data, plots and analysis results
# data_fold = 'data'
# plot_fold = 'plots' 
# ana_res_fold = 'ana_res' 
# 
# # Path to data sets 
# data_path  = '/Users/Oli/work/dBLM_readout/IP2/data/data'
# # Path for test enviroment data
# data_test_env  = '/Users/Oli/work/dBLM_readout/IP2/data_test_env/data'
# # data_path  = data_test_env
# # data_path = os.path.join(cwd,data_fold)
# 
# 
# pflag=1
# 
# ana_file_save_interval = 5
# # data_path = os.path.join(cwd,data_fold)
# plot_path = os.path.join(cwd,plot_fold)
# ana_res_path = os.path.join(cwd,ana_res_fold) 
# 
# 
# l.log_file_set(cwd,'log',pflag)
#   
# f = open(l.log_path(),'a')
# original = sys.stdout
# sys.stdout = Tee(sys.stdout, f)
# 
# 
# 
# 
# 
# g.printer(data_path,pflag)
# 
# i.path(data_path,pflag)
# i.path_check(pflag)
# i.data_list_creator('.txt',pflag)
# p.set_save_path(plot_path,pflag)
# ar.infrastruc(ana_res_path,pflag)
# 
# 
# header=[['time_stamp','year','month','day','hour','minute','second','time sec','time zero',
#          'delta time zero','beam','ip','loc','dcum','type','daq_name','channel','mode','beamstatus',
#          't total','t start','t end','t delta','offset','offset_corr','noise','sig 10 pt','sig 10 t','sig 50 pt','sig 50 t','run','analysed',
#          'file_name','file_name_path']]
# 
# scope_conf = [['daq_name'        ,'ip'   ,'beam' ,'loc'  ,'dcum'     ,'type','channel','name'],
#              ['cfo-ua23-bhascp_C1' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','1','cfo-ua23-bhascp'],
#              ['cfo-ua23-bhascp_C2' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','2','cfo-ua23-bhascp'],
#              ['cfo-ua23-bhascp_C3' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','3','cfo-ua23-bhascp'],
#              ['cfo-ua23-bhascp_C4' ,'2'    ,'1'    ,'1'    ,'3254'  ,'CIVIDEC','4','cfo-ua23-bhascp'],
#              ['cfo-us65-bhascp_C1' ,'6'    ,'1'    ,'2'    ,'16505.55'  ,'CIVIDEC','1','cfo-us65-bhascp'],
#              ['cfo-us65-bhascp_C2' ,'6'    ,'1'    ,'2'    ,'16505.55'  ,'CIVIDEC','2','cfo-us65-bhascp'],
#              ['cfo-us65-bhascp_C3' ,'6'    ,'2'    ,'2'    ,'16817.86'  ,'CIVIDEC','3','cfo-us65-bhascp'],
#              ['cfo-us65-bhascp_C4' ,'6'    ,'2'    ,'2'    ,'16817.86'  ,'CIVIDEC','4','cfo-us65-bhascp'],
#              ['cfo-ua87-bhascp_C1' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','1','cfo-ua87-bhascp'],
#              ['cfo-ua87-bhascp_C2' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','2','cfo-ua87-bhascp'],
#              ['cfo-ua87-bhascp_C3' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','3','cfo-ua87-bhascp'],
#              ['cfo-ua87-bhascp_C4' ,'8'    ,'2'    ,'2'    ,'23392.63'  ,'CIVIDEC','4','cfo-ua87-bhascp']
#              ]
#  
# ar.header_set(header,pflag)
# # print ar.haeder
# print i.data_list
# ar.int_data_sets = ar.file_setup(ana_res_path,'int_data_sets.csv',pflag)
# # print ar.file_setup(ana_res_path,'ana_file.csv',pflag)
# ar.ana_file =  ar.file_setup(ana_res_path,'ana_file.csv',pflag)
# ar.ana_file_updater(i.data_list,pflag)
# ar.ana_file_saver(1,pflag)# print ar.ana_file
# # print ar.int_data_sets
# print ar.ana_file
# # sys.exit('stop')
# # ar.ana_file_check(0,pflag)
# # ar.ana_file_loader(pflag)
# # ar.ana_file_writer(i.data_list,pflag)
# # ar.ana_file_saver(1,pflag)
# 
# # sys.exit('stop')
# max_it = len(ar.ana_file)
# force_flag = 0
# # max_it = 2
# # print ar.ana_file[0]
# 
# a.header(ar.ana_file[0],pflag)
# 
# 
# # sys.exit('stop')
# for k in range(1,max_it):
# # for k in range(len(i.data_list)):
#     g.loop_info(k,i.len_data_list,pflag)
#     print ar.ana_file[k]
#     line = ar.ana_file[k]
#     ana_flag = a.tba_check(line,force_flag,pflag)
#     g.printer(ana_flag,pflag)
#     if ana_flag == 1:
#         g.tprinter('start analysis',pflag)
#         a.name_info_scope(line,scope_conf,pflag)
#         a.time_cor(line,pflag)
#          
# # #         break
#         a.data_loader(line,pflag)
#         
#         a.data_check(pflag)
#         a.time_info(line,a.data,pflag)
#         a.offset_corr(line,a.data,pflag)
#         a.noise_finder(line,a.data,pflag)
#         a.sig_above(line,a.data,10,pflag)
#         a.sig_above(line,a.data,50,pflag)
#         
# #         p.simple_plotter(line,a.data,a.header,1,pflag)
#         p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-6,1e-6,1,pflag)
#         p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-7,5e-7,1,pflag)
#         p.simple_plotter_zoom(line,a.data,a.header,a.time_stamp_string,-1e-6,100e-6,1,pflag)
# #         a.bin_time_cor(pflag)
# #         a.c_counter(line,pflag)
# #         a.set_t_zero(line,pflag)
# #         a.time_sec(line,pflag)
# #         a.delta_time_zero(line,pflag)
# #         a.dc_counter(line,pflag)
# #         a.dt_counter(line,pflag)
#         
# #         name ='test.pdf'
# #         hp.shist(a.data,1,plot_path,a.time_stamp+'_'+a.daq_name,pflag)
# 
# #         a.t_delta(line,a.data,pflag)
# #         a.offset_corr(line,a.data,pflag)
# #         a.noise_finder(line,a.data,pflag)
# #         a.max_finder(line,a.data,pflag)
#     else:
#         pass
#     
#     
#     a.analysed(ar.ana_file[k],pflag)
# 
# # ar.int_data_cond(line,'sig 50 pt',1,1,pflag)
# # ar.file_saver(ana_res_path,'int_data_sets.csv',pflag) 
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
# 
# 
# 
# 
# 
# 
# # plot_path = os.path.join(cwd,plot_fold)
# # ana_res_path = os.path.join(cwd,ana_res_fold) 
# # 
# # 
# # l.log_file_set(cwd,'log')
# #   
# # f = open(l.log_path(),'a')
# # original = sys.stdout
# # sys.stdout = Tee(sys.stdout, f)
# # 
# # 
# # pflag=1
# # ana_file_save_interval = 5
# # 
# # 
# # g.printer(data_path,pflag)
# # 
# # i.path(data_path,pflag)
# # i.path_check(pflag)
# # 
# # i.data_list_creator('.txt',pflag)
# # p.set_save_path(plot_path,pflag)
# # ar.infrastruc(ana_res_path,pflag)
# # ar.ana_file_check(pflag)
# # ar.ana_file_loader(pflag)
# # ar.ana_file_writer(i.data_list,pflag)
# # ar.ana_file_saver(1,pflag)
# # 
# # # sys.exit('stop')
# # max_it = len(ar.ana_file)
# # print ar.ana_file[0]
# # 
# # a.header(ar.ana_file[0],pflag)
# # # sys.exit('stop')
# # for k in range(1,max_it):
# # # for k in range(len(i.data_list)):
# #     g.loop_info(k,i.len_data_list,pflag)
# #     print ar.ana_file[k]
# #     line = ar.ana_file[k]
# #     ana_flag = a.tba_check(line,1,pflag)
# #     if ana_flag == 1:
# #         g.tprinter('start analysis',pflag)
# #         a.name_info(line,pflag)
# #         a.data_loader(line,pflag)
# #         a.data_check(a.data,pflag)
# #         a.t_delta(line,a.data,pflag)
# #         a.offset_corr(line,a.data,pflag)
# #         a.noise_finder(line,a.data,pflag)
# #         a.max_finder(line,a.data,pflag)
# #     else:
# #         pass
# #     
# #     
# #     a.analysed(ar.ana_file[k],pflag)
# #  
# # ar.ana_file_saver(1,pflag)   
# #     
# # # for i in ar.ana_file:
# # #     print i    
# # #     i.data_importer(i.data_list[k][0],pflag)
# # #     p.set_save_path(plot_path,pflag)
# # # #     for q in range(10):
# # # #         print i.data[q,3:]
# # #     p.simple_plotter(i.data[:,3:],i.data_list[k][1],0,pflag)
# # #     max_y_index=a.max_find(i.data[:,3:],1,pflag)
# # #     p.zoom_plotter(i.data[:,3:],i.data_list[k][1],max_y_index,1000,0,pflag)
# # #     print a.trig_finder(i.data[:,3:],1,2,pflag)




'''
Created on Jun 11, 2015

@author: Oli
'''
'''
Created on Jun 11, 2015

@author: Oli
'''
import sys
import os
import numpy as np
import csv
import pandas as pd
# import str




# includes the minion files into python path
sys.path.append('/Users/Oli/work/python/minions')
# sys.path.append('/Users/Oli/work/Timber/Timber_python_MFitterer/rdmstores/')
# sys.path.append('/Users/Oli/work/Timber/Timber_python_MFitterer/')


# loads functions from other scripts
from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data
from ana_res import ana_res
from plotter import *

# from rdmstores import * 

a = ana_data()
ar = ana_res()
g = gen()
l = log_files()
imp = imp() 
p = plotter()
hp = histplot()

print sys.argv 

# if len(sys.argv)!=3:
#     sys.exit('not correct number of arguments')
# else:
#     pass

#plot flag
# if set to one, g. functions will generate output on the console and log file
# pflag= int(sys.argv[1])
pflag= 1
# force flag
# forces the script to reanalyse the data sets
# force_flag = int(sys.argv[2])
force_flag = 1
fflag = 1
# save interval for the ana_file
ana_file_save_interval = 5

g.printer('pflag set to 1',pflag)

# working directory with the main script 
# and the result folders
# cwd = '/Users/Oli/work/python/LHC_data_analysis_scope/test_env'
cwd = '/Users/Oli/work/python/LHC_data_analysis_scope/20150727_1'

# result folders
data_fold = 'data'
plot_fold = 'plots' 
ana_res_fold = 'ana_res' 

# path to data sets
# data_path  = '/Users/Oli/work/dBLM_readout/IP4/ROSYAX106E20028/'
# data_path  = '/Users/Oli/work/dBLM_readout/IP2/data/test_env/'
# data_path  = '/Users/Oli/work/dBLM_readout/IP2/data/20150724_data_sets/'
data_path  = '/Users/Oli/work/dBLM_readout/IP2/data/20150727_data_sets/'

# data_path  = '/Users/Oli/work/dBLM_readout/IP4/ROSYAX106E20028/20150713_hist_test'
# data_path = os.path.join(cwd,data_fold)

# list of rosy devices
daq_list = ['waverunner1']
rosy_file_info_list = [0]*len(daq_list) 

data_path_list = []
cwd_list = []
for i in daq_list:
    data_path_list.append(os.path.join(os.path.join(data_path,i),'data'))
    cwd_list.append(os.path.join(cwd,i))

# header list 
# conatins the column names in the ana_file
header=[['time_stamp','daq_name','mode','ip','loc','dcum','type','beam','year','month','day','hour','minute','second','sec','time stamp',
         'offset_corr','offset','ns convert','moving average','num pts moving average','noise','run','analysed',
         'file_name','file_name_path']]

# info about rosy devices
daq_conf = [['daq_name'        ,'ip'   ,'beam' ,'loc'  ,'dcum'     ,'type'],
             ['cfo-ua23-bhascp'     ,'2'    ,'1'    ,'1'    ,'9929.46'  ,'CIVIDEC' ],
             ['cfo-ua56-bhascp'    ,'1'    ,'2'    ,'9936.93'  ,'CIVIDEC' ],
             ['cfo-ua78-bhascp' ,'4'    ,'2'    ,'2'    ,'10057.23'  ,'CIVIDEC' ],
            ]





# start of the main loop 
# runs through the rosy list

for i in range(len(daq_list)):
    # sets variables to 0
    data_path = 0
    daq = 0
    cwd = 0
    
    # current rosy device
    daq = daq_list[i]
    
    # current working path
    cwd = cwd_list[i]
    
    # current data path
    data_path = data_path_list[i]
    plot_path = os.path.join(cwd,plot_fold)
    ana_res_path = os.path.join(cwd,ana_res_fold) 
    
#     ar = ana_res()

    # output of the device and paths
    g.tprinter('DAQ: '+daq,pflag)
    g.printer('cwd: '+cwd,pflag)
    g.printer('data path: '+data_path,pflag)
    
    
    # Check if can be deleted
#     ar.ana_file = []
#     ar.data_list = []

    # creates the device directory
    ar.rosy_dir_creator(cwd,pflag)
    
    # sets up the log file 
    l.log_file_set(cwd,'log',pflag)  
    f = open(l.log_path(),'a')
    original = sys.stdout
    sys.stdout = Tee(sys.stdout, f)
    

    
#     imp.path_data(data_path,pflag)
#     
#     imp.path_check(pflag)
    
    # sets the plot path
    p.set_save_path(plot_path,pflag)
    # creates the infrastructure
    # folder and tests writing permission 
    ar.infrastruc(ana_res_path,pflag)
    
    # sets the anafile name 
    # combination of the device and the ana_file indicator
    ar.ana_file_name_set(daq,pflag)
    
    # sets the header
    ar.header_set(header,pflag)
    
    # sets data path
    ar.data_path_set(data_path,pflag)
    
    # checks for ana_file
    ar.check_for_ana_file(ana_res_path,fflag,pflag)
    
    # creates a list of .csv files in the current cwd directory
    ar.data_list_creator('txt',pflag)
    
    # updates the ana_file by adding only new files from data_list to the ana_file
    ar.ana_file_updater(pflag)
    
    # saves the ana_file
    ar.ana_file_saver(1,pflag)
    
    

    # the namber of max iterations of the analysis loop
    max_it = len(ar.ana_file)
    

    # sets header    
    a.header_set(ar.ana_file[0],pflag)
    
    
    # sys.exit('stop')
    # counters for analysed and already analysed files
    ana_counter = 0
    already_ana_counter = 0
    
#     g.printer('Length ana_file: '+str(len(ar.ana_file)),pflag)

#     sys.exit()
    # analysis loop
    k = 1
    for k in range(1,max_it):
        
        skip=0
    
        # for k in range(len(i.data_list)):
        # info about  the analysis run
        g.loop_info(k,len(ar.ana_file)-1,pflag)
            
#         print ar.ana_file[k]
        # current line of the ana_file
        line = ar.ana_file[k]
        
        if not line[-2].endswith('C1_14142_data.txt'):
            skip = 1
            g.printer('line will be skipped',pflag)
        else:
            g.printer('file will be analysied',pflag)
            
        if skip != 1:       
            # if force flag == 1, reanalysis
            ana_flag = a.tba_check(line,force_flag,pflag)
                
            # if ana_flag == 1, continue analysis
            if ana_flag == 1:
                g.tprinter('start analysis',pflag)
                
                # extracts name infos
                a.name_info_hist(line,daq_conf,pflag)
    #             
    #             # converts the time stamp into readable time information
                a.time_cor_scope(line,pflag)
        #             
    #             # loads the data  
                a.data_loader(line,pflag)
    #             
    #             # checks if data is ok
                a.data_check(pflag)
                
                a.ns_convert(line,pflag)
                # offset correction
                a.offset_corr(line,a.data,pflag)
                
                # moving average
                a.moving_average(line,5)
                    
    #             print a.data[1,1]
                
                    
    #             # converts bins into time 
    #             a.bin_time_cor(pflag)
                # noise calc
                a.noise_finder(line,a.data,pflag) 
                    
                # creating plots
                save_flag = 1
                p.plotter_overview(line,a.data,a.header,save_flag,pflag)
                
#                 p.simple_plotter_zoom(line,a.data,a.header,-1000,3000,save_flag,pflag)
#                 p.simple_plotter_zoom(line,a.data,a.header,-100,400,save_flag,pflag)
#                 p.simple_plotter_zoom(line,a.data,a.header,-1000,10000,save_flag,pflag)
                p.simple_plotter_zoom(line,a.data,a.header,3000,6000,save_flag,pflag)
#                 p.simple_plotter_zoom(line,a.data,a.header,3500,4500,save_flag,pflag)
                p.simple_plotter_zoom(line,a.data,a.header,3750,4250,save_flag,pflag)
#                 p.simple_plotter_zoom(line,a.data,a.header,92000,95000,save_flag,pflag)
    #             p.simple_plotter_zoom(line,a.data,a.header,-1e7,1e6,1,pflag)
    #             # total number of counts in histogram
    #             a.c_counter(line,pflag)
    #             
    #             # plots the histogram data 
    #             p.hist_plotter(line,a.data,header,1,pflag)
    #             
    #             # sets the time_zero, if file ends with ST or its the first data
    #             a.set_t_zero(k,line,pflag)
    #             
    #             # sets time in seconds 
    #             a.set_t(line,pflag)
    #     
    #             # gives the delta of counts to previous hist 
    #             a.dc_counter(line,pflag)
        
                    
        
                ana_counter += 1
            else:
                already_ana_counter += 1
                
                # sets the file to analysed
                a.analysed(ar.ana_file[k],pflag)
        else:
            pass    
            
        # saves the ana_file at the end of analysis run
        ar.ana_file_saver(1,pflag)   
    
    # summary of run
    g.printer('Data sets from: '+str(daq_list[i]),pflag)
    g.printer(str(k)+' files found',pflag)
    g.printer(str(ana_counter)+' files analysed',pflag)
    g.printer(str(already_ana_counter)+' files already analysed',pflag)
    
    # info list contains device and counter information
    rosy_file_info = [daq_list[i],k,ana_counter,already_ana_counter]
    rosy_file_info_list[i]=rosy_file_info 
    
    g.printer('Analysis completed for '+str(daq_list[i]),pflag)

# gives final overview of the analysis    
for i in rosy_file_info_list:
    g.printer('For: '+i[0],pflag)
    g.printer(str(i[1])+' files found',pflag)
    g.printer(str(i[2])+' analysed',pflag)
    g.printer(str(i[3])+' were already analysed',pflag)      
    
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







