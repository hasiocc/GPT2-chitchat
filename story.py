# -*- coding: UTF-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg
from optparse import OptionParser
content = '''
而在莊園的中心，有一座巨大的豪宅，這座豪宅莊嚴雄偉，金碧輝坎，外表呈歐式風格，裡面則是厚重中國江南古代風味，假山庭園，高樓住宅，更是數不勝數，住在這裡的人，一看便知非富即貴。
　　
'''
seg_list = jieba.cut(content)
print ("Full Mode:", "/ ".join(seg_list))  # 全模式
