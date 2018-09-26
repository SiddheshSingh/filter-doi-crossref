from habanero import Crossref
cr = Crossref()

#Converts list of values to csv
def listtocsv(doi,filename='doi_list.csv'): #doi is a list of dictionary with 'DOI' as an index
    import csv
    csvfile = filename
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in doi:
            writer.writerow([val['DOI']]) 
    return 'Success'

#Filter doi from query
def filter_doi(query,cursor="*"):
    return cr.works(query=query,select='DOI',cursor=cursor,cursor_max=20)

#Filters out items,total results and next-cursor value from result
#Required as the data type of result is any one of list and dictionary
def give_vals(result):
    if type(result)==list:k=result[0]['message']
    else:k=result['message']
    return {'items':k['items'],'total-results':k['total-results'],'next-cursor':k['next-cursor']}

def permutations(n,val):
    counter=0
    while not n==0:
        if n<val:
            counter+=1
            break
        counter+=1
        n-=val
    return counter

#returns list of all dois
def search_all_dois(query):
    fir = give_vals(filter_doi(query))
    dois=fir['items']
    total_results=fir['total-results']
    total_permutations=permutations(total_results,20)
    current_cursor_number=2
    while current_cursor_number<total_permutations: 
        fir=give_vals(filter_doi(query,fir['next-cursor']))
        current_cursor_number+=1
        dois+=fir['items']
    return dois

'''
The function "search_all_dois(query)" inputs a string query and 
returns list of all dois which results in that query in format-
['DOI':unique_doi,'DOI':unique_doi.....].

function "listtocsv(doi,filename='doi_list.csv')" converts list of
doi in format returned by search_all_dois function to csv.
'''