import pandas as pd
import datetime
def merge(x,y):
    x = pd.merge(x, y, on="scopus_author_id", how="left")
    return x

def split(x):
    str_contributor_scopus_author_ids = []  ##str
    for i in x:
        i = str(i)
        str_contributor_scopus_author_ids.append(i)
    a = []
    for i in str_contributor_scopus_author_ids:
        i = i.replace("|||", ",")
        a.append(i)
    b = []
    for i in a:
        i = i.replace("0|", "0")
        b.append(i)

    split_contributor_scopus_author_ids = []
    for i in b:
        split = i.split(",")
        split_contributor_scopus_author_ids.append(split)
    return split_contributor_scopus_author_ids

def string(x):
    new_medicine_publications_scopus_author_id = []
    for i in x:
        i = str(i)
        new_medicine_publications_scopus_author_id.append(i)
    return new_medicine_publications_scopus_author_id

def first_last_other(x,y):
    first_last_other = []
    count = -1
    for i in x:
        count += 1
        if i == y[count][0]:
            first_last_other.append("first")
        elif i == y[count][-1]:
            first_last_other.append('last')
        else:
            first_last_other.append('other')
    return first_last_other

def date_str(x):

    str_cover_date = []
    x = x.dt.date
    for i in x:
        j = str(i)
        j = j.strip()[0:4]
        str_cover_date.append(j)
    return(str_cover_date)




