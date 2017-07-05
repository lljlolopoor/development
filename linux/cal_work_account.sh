#!/bin/bash

# 统计test.txt每行的单词出现的频率，按照词频进行降序排序，取前2
cat test1.txt | sort | uniq -c | sort -k1 -r | head -n 2
# 将文件中的用逗号或空格分隔的单词隔行，便于之后统计词频
# tr, translate, 主要是-d删除，-s压缩重复字符，例tr -s [a-z]
cat test2.txt | tr ', ' '\n' | sort | uniq -c | sort -k1 -r | head -n 2
