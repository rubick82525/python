#coding=gbk
import sys
screws_sla=[]
for arg in sys.argv[1:]:
	arg_str=str(arg)
	new_screw={'num':arg_str.split(":")[0],'sla':arg_str.split(":")[1]}
	screws_sla.append(new_screw)
print(screws_sla)
for screw_sla in screws_sla:
	a=int(screw_sla['sla'])
	try:
		if a<=4191.62:
			e=a*0.835
		else:
			b=a-3500-a*0.165
			if b<=1500:
				c=0.03
				d=0
			elif b<=4500:
				c=0.1
				d=105
			elif b<=9000:
				c=0.2
				d=555
			elif b<=35000:
				c=0.25
				d=1005
			elif b<=55000:
				c=0.3
				d=2755
			elif b<=80000:
				c=0.35
				d=5505
			else:
				c=0.45
				d=13505
			e=a*0.835-(b*c-d)	
		print(str(screw_sla['num'])+':'+str(e))
	except:
		print('wocao')
