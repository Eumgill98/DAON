from django.http import HttpResponse
from django.shortcuts import render


import pandas as pd
import os
import platform
import datetime

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent




def home(request):


    return render(request, 'map/home.html')


def main(request):
    db, ori_db =  read_category()



    return render(request, 'map/main.html', db)

def recomand(requset):
    db = {}
    ori_data, html_code =read_data()

    db['dataframe'] = html_code
    db['ori_data'] = ori_data


    return  render(requset, 'map/recomand.html', db)

def make(requset):

    return render(requset, 'map/make.html')


##불러오기 기능

def read_data():
    data = pd.read_csv('C:/github/ICT/ict_project/daon/daon/data/db.csv', encoding='ms949')
    df=pd.DataFrame()
    df['사업명']=data['사업명']
    df['지역']=data['지자체']
    html_DataFrame = df.to_html(justify='center', index=False, classes="table")
    return(data, html_DataFrame)

def read_category():
    index_1 = [3,27,14]
    index_2 = [10, 11]
    index_3 = [7, 15, 23]
    index_4 = [14, 16, 19]
    index_5 = [16, 20,21]
    num = [1,2,3]

    df_index = ['사업명', '지자체', '해시태그', 'URL']

    db = {}
    df, _ = read_data()
    ori_db = pd.DataFrame()
    for i in range(len(df_index)):
        ori_db[df_index[i]] = df[df_index[i]]

    for i in range(3):
        db[f'latest_{num[i]}'] = ori_db.loc[index_1[i]][df_index[0]]
        db[f'city_{num[i]}'] = ori_db.loc[index_1[i]][df_index[1]]
        db[f'hash_{num[i]}_1'] = ori_db.loc[index_1[i]][df_index[2]]
        db[f'link_{num[i]}'] = ori_db.loc[index_1[i]][df_index[3]]

    for i in range(2):
        db[f'baby_{num[i]}'] = ori_db.loc[index_2[i]][df_index[0]]
        db[f'b_city_{num[i]}'] = ori_db.loc[index_2[i]][df_index[1]]
        db[f'b_hash_{num[i]}_1'] = ori_db.loc[index_2[i]][df_index[2]]
        db[f'b_link_{num[i]}'] = ori_db.loc[index_2[i]][df_index[3]]

    for i in range(3):
        db[f'for_you_{num[i]}'] = ori_db.loc[index_3[i]][df_index[0]]
        db[f'f_city_{num[i]}'] = ori_db.loc[index_3[i]][df_index[1]]
        db[f'f_hash_{num[i]}'] = ori_db.loc[index_3[i]][df_index[2]]
        db[f'f_link_{num[i]}'] = ori_db.loc[index_3[i]][df_index[3]]

    for i in range(3):
        db[f'real_time_{num[i]}'] = ori_db.loc[index_4[i]][df_index[0]]
        db[f'r_city_{num[i]}'] = ori_db.loc[index_4[i]][df_index[1]]
        db[f'r_hash_{num[i]}'] = ori_db.loc[index_4[i]][df_index[2]]
        db[f'r_link_{num[i]}'] = ori_db.loc[index_4[i]][df_index[3]]

    for i in range(3):
        db[f'younger_{num[i]}'] = ori_db.loc[index_5[i]][df_index[0]]
        db[f'y_city_{num[i]}'] = ori_db.loc[index_5[i]][df_index[1]]
        db[f'y_hash_{num[i]}'] = ori_db.loc[index_5[i]][df_index[2]]
        db[f'y_link_{num[i]}'] = ori_db.loc[index_5[i]][df_index[3]]

    return db, ori_db
