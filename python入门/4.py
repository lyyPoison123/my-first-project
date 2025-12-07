"""
题目：编写一个成绩评级程序
90分以上：优秀
80-89分：良好
70-79分：中等
60-69分：及格
60分以下：不及格

要求：
1. 让用户输入成绩（0-100之间的整数）
2. 根据成绩输出评级
3. 如果输入的成绩不在0-100之间，提示"成绩无效"
"""
# 请在这里编写你的代码
score = int(input("请输入您的成绩："))
if score > 100 or score < 0:
    print("成绩无效")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")