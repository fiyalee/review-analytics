data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)  
		count += 1  #每讀一千筆一次
		if count % 1000 == 0:
			print(len(data))
			# % count 跟1000求餘數為0(1000的倍數),則.. 
print(len(data))  #每一次只讀取一行

print(data[0])
print('----------------------')
print(data[1])