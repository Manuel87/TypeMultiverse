#Interplolating x Masters

#			1	 2    3    4    5    6    7
#interpol = [0.4, 0.0, 0.0, 0.0, 0.0, 1.0, 5.0] 	#set 1
#interpol = [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0] 	#set 2
interpol = [0.0, 1.8, 0.5, 1.0, -0.3, 0.0, 0.0] 	#set 3

#editing instance
i = Font.instances[0]


interpol_sum = 0
Masters = Font.masters
i.setManualInterpolation_(True)


#calc interpol_sum 
for k in range(0, len(interpol), 1):
	interpol_sum += interpol[k]
 

#apply
for k in range(0, len(interpol), 1):
	#convert values so its sum equals 1.0
    interpol[k] = interpol[k] / interpol_sum
    #apply to instance
    i.instanceInterpolations()[Masters[k].id] = interpol[k]
	
#new distribution 
print i.instanceInterpolations()