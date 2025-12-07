"""
题目：创建一个学生信息字典
要求包含：姓名(name)、年龄(age)、成绩(score)
然后实现以下功能：
1. 打印所有信息
2. 修改成绩为原成绩+5
3. 添加一个新的键值对：班级(class) = "计算机1班"
4. 检查"性别"是否在字典中，如果不存在则添加"gender": "男"
"""
# 请在这里编写你的代码
dic = {
    "name":"zhangsan",
    "age":22,
    "score":88
}
dic["score"]+=5
dic["class"]="计算机一班"
if "性别" not in dic.keys():
    dic["gender"]="男"
print(dic)