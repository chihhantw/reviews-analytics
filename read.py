#讀取留言

deta = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		deta.append(line)
		count += 1
		if count % 1000 == 0: #如果count是1000的倍數
			# %是用來求餘數 
		    print(len(deta))#每讀取一筆就印出
print(len(deta))


print(deta[0])
print('--------------------------')
print(deta[1])

