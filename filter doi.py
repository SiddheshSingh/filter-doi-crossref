from habanero import Crossref
cr = Crossref()

#Converts list of values to csv
def listtocsv(doi,filename): #doi is a list of dictionary with 'DOI' as an index
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

#Saves ALL dois from search results to csv file
def search_all_dois(query):
    fir = filter_doi(query)['message']
    dois=fir['items']
    curlen=len(dois)
    while curlen==20: 
        fir=filter_doi(query,fir['next-cursor'])['message']
        k=fir['items']
        dois+=k
        curlen=len(k)
    return dois