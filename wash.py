"""
wash
Author:我是谁
Date:2021/10/14
"""
import csv
import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
train_label = pd.read_csv('./dataset/train_label.csv')
train_set = pd.read_csv('./dataset/train_set.csv')


# train_set.info()
# da = pd.merge(train_set, train_label, left_on = 'user_id', right_on = 'user_id', how='left', sort = False)
# da.info()
train_set.drop(['X6','X7','X8','X9','X10', 'X11','X12','X13','X14'],axis=1,inplace=True)
#构建新字段：近三月平均语音超套金额X44、近三月平均流量超套金额X45、近三月平均流量饱和度
train_set['X44'] = train_set[['X18','X19','X20']].mean(axis=1)
train_set['X45'] = train_set[['X21','X22','X23']].mean(axis=1)
train_set['X46'] = train_set[['X34','X35','X36']].mean(axis=1)
#删除原字段
train_set.drop(['X18','X19','X20','X21','X22','X23','X34','X35','X36'],axis=1,inplace=True)

train_set.drop(['X24','X25','X26','X27','X28','X29','X30','X31'],axis=1,inplace=True)

# 空值处理
train_set['X3'].fillna(0,inplace=True)
train_set['X38'].fillna(0,inplace=True)
#分组查看各用户类别数量
print(train_set[['user_id','X5']].groupby('X5').count())
#填充缺失值为众数
train_set['X5'].fillna('大众用户',inplace=True)
#根据各字段的数据分布填充缺失值为均值、众数
mean_cols = ['X15','X16','X17','X44','X45','X46']
mode_cols = ['X32','X33']

for col in mean_cols:
    train_set[col].fillna(train_set[col].mean(),inplace=True)

for col in mode_cols:
    train_set[col].fillna(18,inplace=True)
print(train_set.info())
print(train_label.info())
da = pd.merge(train_set, train_label, on='user_id')

da.to_excel('./dataset/datas.xlsx',index=False)