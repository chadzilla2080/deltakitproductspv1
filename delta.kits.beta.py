from urllib.request import urlopen as open
from bs4 import BeautifulSoup as soup

urls = ["https://www.deltakits.com/shop/windshield-repair-products/", "https://www.deltakits.com/shop/windshield-repair-products/page/2/", "https://www.deltakits.com/shop/windshield-repair-products/page/3/", "https://www.deltakits.com/shop/windshield-repair-products/page/4/", "https://www.deltakits.com/shop/windshield-repair-products/page/5/", "https://www.deltakits.com/shop/windshield-repair-products/page/6/", "https://www.deltakits.com/shop/windshield-repair-products/page/7/", "https://www.deltakits.com/shop/windshield-repair-products/page/8/", "https://www.deltakits.com/shop/windshield-repair-products/page/9/", "https://www.deltakits.com/shop/windshield-repair-products/page/10/", "https://www.deltakits.com/shop/windshield-repair-products/page/11/", "https://www.deltakits.com/shop/windshield-repair-products/page/15/"] 

for url in urls:
    download = open(url)
    page_html = download.read()
    download.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("", {"class":"product-inner"})

    for container in containers:
        kit_model = container.findAll("div",{"class":"cat-list"})
        kit = kit_model[0].text.strip()

        kit_price = container.findAll("span", {"class":"woocommerce-Price-amount"})
        price = kit_price[0].text.strip()

        kit_rating = container.findAll("div", {"class":"star-rating"})
        rating = kit_rating[0].text.strip()

        print(kit)
        print(price)
        print(rating)