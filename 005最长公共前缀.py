"""
题目：
最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    Longest Common Prefix
"""
class Solution:
    def longestCommonPrefix(self,strs):
        len0  = len(strs)
        if len0 == 0:#判断strs是否为空
            return ''
        list_len = []#初始化存放每个子串的长度
        # 找出最短的字符串长度min_len
        for i in range(len0):
            list_len.append(len(strs[i]))
        list_len.sort()#升序排序
        # 取出最短的子串com_str
        # 我这里是直接取第一个子串的前min_len
        com_str = strs[0][0:list_len[0]]#直接取第一个子串的前min_len
        b0 = com_str
        for s in strs:#遍历strs子元素
            for i in range(list_len[0]):#比较子元素与com_str，找出最长公共前缀
                if s[i] != com_str[i]:# 判断到有不等的地方
                    a0 = s[0:i]
                    if len(b0) >= len(a0):# 上一个最长公共前缀是否比现在长
                        b0 = a0
        return  b0


s = Solution()
a = s.longestCommonPrefix(["flower","flow","flight"])
print(a)

# 大牛方法
"""
通过zip(*strs)将上述list分解为下面的元组，然后通过for循环，迭代取值，取出每个元组，
并通过set将每个元组进行合并，我们知道set中不会出现相同的数，也就是三个字符直接合并后为1个，则表示为相同字符，否则不相同，直接退出循环即可。
strs=["flower","flow","flight"]
通过zip可分解为：
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
...............
"""
class Solution:
    def longestCommonPrefix(self, strs):
        res = ''#初始化最长公共前缀
        if len(strs) == 0:
            return ''
        # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
        for each in zip(*strs):#对每个子元素的每个字母进行遍历
            # 利用集合创建一个无序不重复元素集
            if len(set(each)) == 1:#若每个子元素的该字母为公共字母，则取集合后长度为1，则将该字母添加到res中
                res += each[0]
            else:
                return res
        return res

s = Solution()
a = s.longestCommonPrefix(["flower","flow","flight"])
print(a)
