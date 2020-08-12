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
print('檔案讀取完了，總共有',len(deta),'筆資料')

sum_lem = 0
for d in deta: #把deta裡面的每一筆資料命名為d
    sum_lem += len(d)

print('留言的平均長度是',sum_lem/ len(deta))
