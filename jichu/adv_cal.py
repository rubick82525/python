#coding=gbk
import sys
import csv

class Config(object):
	
	def __init__(self):
		self.config=self._read_config()
		
	def _read_config(self):
		config={}
		filename='c:/shiyanlou/test1.cfg'		
		with open(filename) as file:
			for line in file:
				line_str=str(line.strip().rstrip())
				zhonglei=line_str.split("=")[0].strip()
				shuilv=line_str.split("=")[1].strip()
				config[zhonglei]=shuilv
		return config
			
	def _get_config(self,zhonglei):
		return self.config[zhonglei]
	
	def get_lower(self):
		return self.config['JiShuL']
	
	def get_higher(self):
		return self.config['JiShuH']
		
	def total_rate(self):
		return sum([
			float(self.config['YangLao']),
			float(self.config['YiLiao']),
			float(self.config['ShiYe']),
			float(self.config['GongShang']),
			float(self.config['ShengYu']),
			float(self.config['GongJiJin'])
		])

config=Config()
class UserData(object):

	def __init__(self):
		self.userdata = self._read_users_data()
		
	def _read_users_data(self):
		userdata=[]
		filename='c:/shiyanlou/user.csv'
		
		with open(filename) as file:
			for line in file:
				line_str=str(line.strip().rstrip())
				name=line_str.split(",")[0].strip()
				i_sal=line_str.split(",")[1].strip()
				yuangong=[name,i_sal]
				userdata.append(yuangong)
		return userdata
	def __iter__(self):
		return iter(self.userdata)	
			
class IncomeTaxCalculator(object):
	
	def __init__(self,userdata):
		self.userdata=userdata
	
	@staticmethod
	def calc_for_insurance(i_sal):
		if int(i_sal)<float(config.get_lower()):
			return float(config.get_lower())*float(config.total_rate())
				
		if int(i_sal)>int(16446.00):
			return float(config.get_higher())*float(config.total_rate())
		
		return int(i_sal)*float(config.total_rate())	
	
	@classmethod				
	def calc_for_all_userdata(cls,i_sal):
		ins_money=cls.calc_for_insurance(i_sal)
		a=int(i_sal)-int(ins_money)
		if a<=3500:
			return '00'
		else:
			b=a-3500
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
			tax=b*c-d
			remain=int(i_sal)-int(ins_money)-(b*c-d)
			return tax,remain
	
	def return_result(self):
		result=[]
		for num,income in self.userdata:
			data=[num,income]
			tax= self.calc_for_all_userdata(income)[0]
			remain= self.calc_for_all_userdata(income)[1]
			data+=[self.calc_for_insurance(income),tax,remain]
			print(data)
			result.append(data)
		return result
		print(result)
	def export(self,file_type='csv'):
		result = self.return_result()
		with open('c:/shiyanlou/gongzi.cvs', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(result)
			
if __name__ == '__main__':
	shili=UserData()
	infor_yuangong=shili._read_users_data()
	jisuan=IncomeTaxCalculator(infor_yuangong)
	jisuan.export()
