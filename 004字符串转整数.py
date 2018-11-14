"""
题目：
    实现 atoi，将字符串转为整数。
    ascii to integer
"""
# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         # 字符串不为空/第一个字符不为数字/-/+
#         str = str.strip()  # 去除两端空格
#         if str == '':   #为空
#             return 0
#         if str[0] != '-' and str[0] != '+' and not str[0].isdigit():# isdigit() 方法检测字符串是否只由数字组成
#             return 0    # 第一个字符不为数字/-/+
#         import re#re模块提供了正则表达式相关操作
#         # 确保字符串内包含数字/+/-
#         pattern = re.compile("[-+0-9]+")#将一个字符串编译为字节代码
#         judge = pattern.findall(str)#获取非重复的匹配列表
#         # 例如：" ","-","+"
#         if not judge or judge[0] == '+' or judge[0] == '-':
#               return 0
#         # 例如："++","--","-+/+-","-2-","2-","--2"
#         if len(judge[0]) >=  2:
#             # 确保字符串内包含数字
#             pattern0 = re.compile("[0-9]+")
#             test01 = pattern0.findall(judge[0])
#             if not test01:
#                 return 0  # 只有+/-
#             if not judge[0][1:2].isdigit():
#                 return 0   #去除  ++/-- 属于第一个字符不为数字情况
#             if judge[0][0] == '-' or judge[0][0] == '+':
#                 judge[0] = judge[0][0] + test01[0]   # 第一个字符为 +/- 结果为符号+数字
#             else:  # 只有数字，无符号位
#                 judge[0] = test01[0]
#         interim_target = float(judge[0])  # 转换成float判断范围
#         if interim_target < -2147483648:
#             return -2147483648
#         if interim_target > 2147483647:
#             return 2147483647
#         target = int(judge[0])  # 范围内，转换成int 返回
#         return target


#解法2
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 定义边界
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        # 去空格
        str_new = str.strip()

        # 定义最终结果字符
        saved_s = ''
        # 字符为空或开头直接为非字符
        if len(str_new)==0 or str_new[0].isdigit()==False and str_new[0]!='-' and str_new[0]!='+':
            return 0
        # 遍历
        for i in range(len(str_new)):
            # 首位有+-号时,让+-号存储到最终结果字符里面
            if str_new[i] == '+' or str_new[i] == '-' or str_new[i].isdigit():
                saved_s+=str_new[i]
                # 判断下一个是否为数字
                if i + 1 < len(str_new) and str_new[i + 1].isdigit() == False:
                    break
        # 最终结果字符只有+-,直接返回0
        if saved_s=='+'or saved_s=='-':
            return 0
        # 获取数字结果
        number = int(saved_s)
        # 判断是否越界
        if number>INT_MAX:
            return INT_MAX
        elif number<INT_MIN:
            return INT_MIN
        else:
            return number
s = Solution()
a = s.myAtoi('-5')
print(a)

