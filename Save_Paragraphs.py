from bs4 import BeautifulSoup

with open('scrape_paragraphs.html') as f:
    soup = BeautifulSoup(f, 'html.parser')
    target=soup.dl.find_all('dd')[-1]
    p_elements=target.find_all('p')
