import requests
from bs4 import BeautifulSoup

def get_sponsor(link):

	page = requests.get("https://www.govtrack.us/" + link)

	govt = BeautifulSoup(page.text, 'html.parser')

	name = govt.select_one("#maincontent > div > div.h1-multiline > h1")
	about = govt.select_one("#maincontent > div > div.h1-multiline > p")
	description = govt.select_one("#track_panel_base > div > p")
	image = govt.select_one("#content > div.row.group > div.aside.col-sm-4 > div.photo > img", src=True)

	data = []

	data.append(' '.join([str(ele) for ele in name.text.split()]))
	data.append(' '.join([str(ele) for ele in about.text.split()])) 
	data.append(' '.join([str(ele) for ele in description.text.split()]))
	if image:
		data.append(' '.join([str(ele) for ele in image["src"].split()]))

	return data
 
	# import csv

	# with open("moc.csv", "w") as file:
 		
	# 	writer = csv.writer(file)
	# 	writer.writerows(data)
	
	# with open('moc.csv', mode ='r') as file:   
			
	# 	csvFile = csv.DictReader(file)
	
	# 	for lines in csvFile: 
	# 		print(lines)
 
import csv

with open('krishna.csv', mode ='r') as file:   
        
    csvFile = csv.DictReader(file)
    
    data = []
    
    a = 1
    
    for lines in csvFile: 
        print(a)
        print()
        print(get_sponsor(list(lines.values())[0]))
        print()
        data.append(get_sponsor(list(lines.values())[0]))
        a = a + 1
        print()
        
    with open('moc_data.csv', mode ='w') as fileW:
        writer = csv.writer(fileW)
        writer.writerows(data)
        
with open('moc_data.csv', mode = 'r') as file:
    
    filecsv = csv.DictReader(file)
    data = []
    
    for mocdata in filecsv:
        print(mocdata)