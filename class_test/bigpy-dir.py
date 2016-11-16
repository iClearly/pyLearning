#! /usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
搜索出单个目录下最大的python源代码文件
搜索Windows Python源代码库， 除非指定了dir命令行参数
"""

import os, glob, sys
dirname = r'C:\python3.5\Lib' if len(sys.argv) == 1 else sys.argv[1]
allsize = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsize.append((filesize, filename))

allsize.sort()
print(allsize[:2])
print(allsize[-2:])