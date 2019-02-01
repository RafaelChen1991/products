# 讀取檔案
products = []
with open('products.csv', 'r', encoding='UTF-8') as f:
	for line in f:
		if '商品, 價格' in line:
			continue #continue 不處理,跳到下一迴
		name, price = line.strip().split(',') # split 切割完的結果是清單
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)
print(products[0][0])

#印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])

##字串可以做+跟*
##寫入檔案
with open('products.csv', 'w', encoding='UTF-8') as f: # open只是打開而已
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+str(p[1])+'\n') # 這行才是真正的寫入


# csv 檔通常以逗點','做為區隔。
# \n為換行