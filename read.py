data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)  
		count += 1  #每讀一千筆一次
		if count % 1000 == 0:
			print(len(data))
			# % count 跟1000求餘數為0(1000的倍數),則.. 
print('檔案讀取完，總共有', len(data), '筆資料')  #每一次只讀取一行

sum_len = 0 #目前的總數
for d in data:
	sum_len = sum_len + len(d)
	
print('每筆留言平均長度是', sum_len/len(data))
