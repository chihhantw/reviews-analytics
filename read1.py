data = []
count = 0 
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成了，總共有', len(data), '筆資料')

sum_len = 0 
for d in data:
#將data中的資料一筆一筆讀取，並取名為d
	sum_len = sum_len + len(d)
	#加總所有留言中的長度
print('留言的平均長度為', sum_len/len(data))

#篩選概念
new = []
for d in data:
#d是字串，deta是清單
    if len(d) < 100:
    	new.append(d)
    #如果留言長度小於100，就加入新清單中
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

