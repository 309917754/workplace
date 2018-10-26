from ggplot import *
import pandas as pd

import numpy as np
import os

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df['A'])

# cwd: str=os.getcwd()
# print(cwd)

path1 = U'D:/PythonData/01_heights_weights_genders.csv'
test = pd.read_csv(path1)
print(ggplot(test, aes(x='Height', y='Weight', color='Gender')) + geom_point())  # 加颜色的散点图，以‘Gender分开’
# print(ggplot(test, aes(x='Height', y='Weight', color='Gender')) + geom_point() + geom_smooth())  # 加平滑效果/
ggplot(test, aes(x='Height', y='Weight', color='Gender')) + geom_point() + stat_smooth(method='loess')
ggplot(test, aes(x='Height', y='Weight', color='Gender')) + geom_point() + facet_wrap('Gender', ncol=2)

# 柱形图
# mpg = pd.read_csv("D:\\Users\\zhoumeixu204\\Desktop\\mpg.csv")
#
# ggplot(mpg, aes(x="hwy", y="cty", color='year')) + geom_point(color='steelblue') + scale_x_continuous(
#     breaks=[10, 20, 30])  # 分四段显示 [-co,10][10,20]...
#
# ggplot(mpg, aes(x='hwy', colour='class', fill='True')) + geom_density()
#
# ggplot(mpg, aes('class', fill='year')) + geom_bar()
# ggplot(mpg, aes('class', fill='year')) + geom_bar() + ggtitle("the  hisr")
#
# # 密度曲线
# ggplot(mpg, aes(x='hwy', color='class')) + geom_density()
# ggplot(mpg, aes(x='hwy', colour='class', fill='True')) + geom_density()