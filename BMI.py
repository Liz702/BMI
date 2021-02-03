weight = input('请输入体重（公斤）: ')
height = input('请输入身高（公尺）: ')
weight = float(weight)
height = float(height)
bmi = weight / (height * height)
print('您的BMI为:', bmi)
if bmi < 18.5:
    print('您体重过轻')
elif bmi >= 18.5 and bmi < 24:
    print('您的BMI正常')
elif bmi >= 24 and bmi < 27:
    print('您体重过重')
elif bmi >= 27 and bmi < 30:
    print('您是轻度肥胖')
elif bmi >= 30 and bmi < 35:
    print('您是中度肥胖')
else:
    print('您是重度肥胖')