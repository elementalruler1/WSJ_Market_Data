
from scraper import Request_Gainers as r_gainers

def main():

    data = r_gainers()
    for line in data:
        print line


main()
