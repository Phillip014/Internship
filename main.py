import pandas as pd
from method import split, merge,string,first_last_other,date_str
from data_clean import data_clean
import datetime
medicine_publications=pd.read_excel("./medicine_publications.xlsx")
medicine_scival =pd.read_csv("./medicine_scival.csv")
if __name__ == '__main__':
    merge = merge(medicine_scival,medicine_publications)
    #contributor_scopus_author_ids
    contributor_scopus_author_ids = merge["contributor_scopus_author_ids"]
    contributor_scopus_author_ids = split(contributor_scopus_author_ids)
    print(type(contributor_scopus_author_ids[0][0]))
    print(len(contributor_scopus_author_ids))

    #medicine_publications_scopus_author_id
    medicine_publications_scopus_author_id = merge["scopus_author_id"]
    medicine_publications_scopus_author_id= string(medicine_publications_scopus_author_id)
    print(type(medicine_publications_scopus_author_id[0]))
    print(len(medicine_publications_scopus_author_id))

    #first_last_other
    first_last_other = first_last_other(medicine_publications_scopus_author_id,contributor_scopus_author_ids)
    merge['first_last_other'] = first_last_other

    #date_to_string
    cover_date = merge['cover_date']
    str_cover_date = date_str(cover_date)

    merge['year']=str_cover_date
    sum_author=merge[['scopus_author_id','first_last_other','year']]
    sum_author = pd.DataFrame(sum_author)
    sum_author['first_last_other_year'] = merge['year'] + '_' + merge['first_last_other']
    o = pd.DataFrame(sum_author['first_last_other_year'])
    h = o['first_last_other_year']
    h['first_last_other_year'] = sum_author
    sum_author = sum_author[['scopus_author_id', 'first_last_other_year']]
    sum_author = sum_author[['scopus_author_id', 'first_last_other_year']]
    a = sum_author.groupby(['scopus_author_id', 'first_last_other_year']).size()
    b = sum_author.groupby(['scopus_author_id', 'first_last_other_year']).size().reset_index(name='counts')
    c = b["scopus_author_id"].unique()
    e = []
    for i in c:
        e.append(i)
    e = pd.DataFrame(e)
    e["scopus_author_id"] = e
    d = pd.pivot(b, index='scopus_author_id', columns='first_last_other_year')
    d = d['counts']
    merge = pd.merge(medicine_scival, d, on="scopus_author_id", how="left")
    merge = merge.drop(columns=['NaT_other'])
    merge.to_csv('data.csv', encoding='utf-8')
    medicine_scival = data_clean(medicine_scival)
    merge.to_csv('medicine_scival_test.csv', encoding='utf-8')




