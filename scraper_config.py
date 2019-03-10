
class rank_xpath():
    '''Class containing xpaths to parse gainers/laggards'''

    def __init__(self):
        '''contains url and xpaths to extract data'''

        self.url = 'http://www.wsj.com/mdc/public/page/2_3021-gainnyse-gainer.html'

        self.rows = '//table[@class="mdcTable"]/tr' # rows.xpath
        self.stock_row = './td/a[@class="linkb"]/text()' # row in rows -> row.xpath
#        self.stock_row = './/text()'
#        self.link = ('.//@href')
        self.data = './td/text()'
