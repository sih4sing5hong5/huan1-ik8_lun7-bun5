import json

輸入檔 = open('踏頭話.json', encoding='utf-8')
原始的json陣列 = json.load(輸入檔)


# 目前版本:
#  [ [{"詞1連字音", "詞1詞組綜合標音"}],  [詞二], ..., [詞N]]
 
# print(原始的json陣列[3][0]['詞組綜合標音'])
頭前是換行 = False
for 一組詞的連字與詞組 in 原始的json陣列:
	原始詞組音標 = 一組詞的連字與詞組[0]['詞組綜合標音']
	
	for 一個字的音標資料 in 原始詞組音標:
		字 =  一個字的音標資料['型體']
		if(字 == '\n' and 頭前是換行 == False):
			頭前是換行 = True
		elif(字 == '\n' and 頭前是換行 == True):
			print()
			頭前是換行 = False	
		else:
			注音符號 = 一個字的音標資料['吳守禮方音']
			羅馬拼音 = 一個字的音標資料['臺羅閏號調']
			print("\\tsoo{{{0}}}{{{1}}}{{{2}}}".format(字, 注音符號, 羅馬拼音).replace("None", ""))
			頭前是換行 = False	
		