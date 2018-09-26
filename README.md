# filter-doi-crossref
### Python code to retrieve DOI from searching query on Crossref and save it as a CSV File.

#### Crossref Client
Habanero is used as the Crossref client. <br>
```
from habanero import Crossref
```

#### Procedure
* The query is searched in Crossref works and is filtered specifically for DOI.
```
  Crossref().works(query=query,select='DOI')
```
* These results are obtained by using Deep Paging Cursors as maximum limit in offset is 10K which is much lesser than total results.
```
  Crossref().works(query=query,select='DOI',cursor='*')
```
* DOIs are then collected in a list which is converted to CSV file using CSV writer.<br>
Following function converts a list of dictionaries containing 'DOI' as an index to a CSV file:
```
  def listtocsv(doi,filename):
      import csv
      csvfile = filename
      with open(csvfile, "w") as output:
          writer = csv.writer(output, lineterminator='\n')
          for val in doi:
              writer.writerow([val['DOI']]) 
      return 'Success'
```
