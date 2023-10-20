import pandas as pd
import matplotlib.pyplot as plt
import graphics

df = pd.read_csv("C:/Users/alejo/Desktop/pythonProject5/tested.csv")


# print(df)


# self = df.loc[
#          df['published_year'].isna(), 'published_year'] = 0

def fare_passager(a):
    fare_date = a.loc[:, ['Fare']]
    fare_date = fare_date.drop_duplicates(subset=['Fare'])
    print(fare_date)


def passenger_survivor(self):
    pass


def surviving_passagers_chart_sex(a):
    date_survivor = a.loc[:, ['Survived', 'Sex']]
    womens = date_survivor.drop(subset=['sex' 'male'])
    print(womens)


def choose_var_1(a):
    a = a.drop_duplicates(subset=['PassengerId'])
    v = input('put the var 1 among the following'
              '1 PassengerId'
              '2 Survived '
              '3 Pclass '
              '4 Name '
              '5 Sex '
              '6 Age '
              '7 SibSp'
              '8 Parch'
              '9 Ticket'
              '10 Fare'
              '11 Cabin'
              '12 Embarked')
    if v == '1':
        a = a.loc[:, ['PassengerId']]

        return a
    if v == '2':
        a = a.loc[:, ['Survived']]
        return a
    if v == '3':
        a = a.loc[:, ['Pclass']]
        return a
    if v == '4':
        a = a.loc[:, ['Name']]
        return a
    if v == '5':
        a = a.loc[:, ['Sex']]
        return a
    if v == '6':
        a = a.loc[:, ['Age']]
        return a
    if v == '7':
        a = a.loc[:, ['SibSp']]
        return a
    if v == '8':
        a = a.loc[:, ['Parch']]
        return a
    if v == '9':
        a = a.loc[:, ['Ticket']]
        return a
    if v == '10':
        a = a.loc[:, ['Fare']]
        return a
    if v == '11':
        a = a.loc[:, ['Cabin']]
        return a
    if v == '12':
        a = a.loc[:, ['Embarked']]
        return a


def choose_var_2(a):
    a = a.drop_duplicates(subset=['PassengerId'])
    v = input('put the var 2 among the following'
              '1 PassengerId'
              '2 Survived '
              '3 Pclass '
              '4 Name '
              '5 Sex '
              '6 Age '
              '7 SibSp'
              '8 Parch'
              '9 Ticket'
              '10 Fare'
              '11 Cabin'
              '12 Embarked')
    if v == '1':
        a = a.loc[:, ['PassengerId']]
        return a
    if v == '2':
        a = a.loc[:, ['Survived']]
        return a
    if v == '3':
        a = a.loc[:, ['Pclass']]
        return a
    if v == '4':
        a = a.loc[:, ['Name']]
        return a
    if v == '5':
        a = a.loc[:, ['Sex']]
        return a
    if v == '6':
        a = a.loc[:, ['Age']]
        return a
    if v == '7':
        a = a.loc[:, ['SibSp']]
        return a
    if v == '8':
        a = a.loc[:, ['Parch']]
        return a
    if v == '9':
        a = a.loc[:, ['Ticket']]
        return a
    if v == '10':
        a = a.loc[:, ['Fare']]
        return a
    if v == '11':
        a = a.loc[:, ['Cabin']]
        return a
    if v == '12':
        a = a.loc[:, ['Embarked']]
        return a




graphics.graphics_use_for_2_vars(choose_var_1(df),choose_var_2(df))

# 'PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'
