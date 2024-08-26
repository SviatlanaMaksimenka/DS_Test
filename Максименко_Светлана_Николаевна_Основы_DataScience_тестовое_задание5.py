# -*- coding: utf-8 -*-
"""
Задача 5:
Существует массив поисковых запросов, например:

search_queries = [“watch new movies”, “coffee near me”,
“how to find the determinant”, “python”, 
“data science jobs in UK”, “courses for data science”, 
“taxi”, “google”, “yandex”,
“bing”,”foreign exchange rates USD/BYN”, 
“Netflix movies watch online free”,
“Statistics courses online from top universities”]

Необходимо реализовать функцию, которая принимает на вход данные
массива поисковых запросов и возвращает распределение
поисковых запросов по количеству слов в каждом из запросов
в процентах.

Результат должен выглядеть следующим образом:
    1 слово : 10% 
    2 слова: 40% 
    4 слова: 45% 
    5 слов: 5%
"""

def func(a):
    wcount = [len(i.split()) for i in a]
    wcount.sort()
    for cnt in set(wcount):
        perc = wcount.count(cnt)/len(wcount)*100
        if cnt == 1:  
            print(f'{cnt} слово: {perc:.0f}%') 
        elif cnt in (2,3,4):  
            print(f'{cnt} слова: {perc:.0f}%') 
        else:  
            print(f'{cnt} слов: {perc:.0f}%')
search_queries = ["watch new movies","coffee near me", "how to find the determinant", "python",
"data science jobs in UK", "courses for data science","taxi", "google", "yandex", "bing",
"foreign exchange rates USD/BYN","Netflix movies watch online free","Statistics courses online from top universities"]
func(search_queries)
