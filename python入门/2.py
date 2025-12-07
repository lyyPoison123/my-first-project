"""
题目：完成以下列表操作
1. 创建一个空列表 fruits
2. 添加 "apple", "banana", "orange" 到列表中
3. 在 "banana" 后面插入 "grape"
4. 删除 "apple"
5. 打印列表长度和所有元素
"""
# 请在这里编写你的代码
fruits = ["apple","banana","orange"]
fruits.insert(2,"grape")
fruits.remove("apple")
print(len(fruits))
print(fruits)