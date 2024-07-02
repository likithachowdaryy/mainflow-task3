import request
from bs4 import Beautifulsoup

#uRL of the web page to scrape
url='https://realpython.com/python-web-scraping-practial-introduction/'   #Replace wit

#send a GET request to the web page
response = requests.get(url)

#check if the request was successful
if respone.status_code == 200:
    #parse the HTML contect of the page
    soup = Beautifulsoup(response.text,'html.parser')

    #Extract all the text from the page
    page_text=soup.get_text()

    #Extract all the links from the page
    links =[a['href']for a in soup.find_all('a',href=True)]

    # Extract all the image from the page
    images =[img['src']for img in soup.find_all('img',src=true)]

    # print the extracted data
    print("page Text:")
    print(page_text)

    print("\nlinks:")
    for link in links:
        print(link)

        print("\nImages:")
        for image in images:
            print(image)
    else:
        print(f"Failed to retrive the web page.status code:{response.status_code}")        