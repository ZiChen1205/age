driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit

age = input('請問你幾歲：')
age=int(age)

if driving == '有':
    if age >= 18:
    	print('你通過測試了！')
    else:
    	print('奇怪？你怎麼有開過車XD')

if driving == '沒有':
    if age >= 18:
    	print('你可以考駕照了阿！怎麼還不去考？')
    else:
    	print('很好！再過幾年就可以考駕照了喔！')