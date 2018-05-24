#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import sys
import importlib #reload를 3.6부터는 이렇게 불러와야한다.(기본내장X로 바뀜)
importlib.reload(sys)



testCSV_path = r"C:\Users\jshan\Desktop\GitProject\FPPG\local_dataset\어종별위탁판매집계\위판장별_어종별_위탁판매_집계_2016년6월_\위판장별 어종별 위탁판매 집계(2016년6월).csv"

dateinfo = pd.read_csv(testCSV_path, encoding="cp949")

print(dateinfo.head(5))



#bs(dateinfo,"lxml")
