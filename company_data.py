
class Company():
    """A class to hold current company data."""

    def __init__(self, data_tuple):
        """Initialize object and set values of the rank in top
           100 gainers, company name, ticker, Price, Change ($),
           Change (%), and Volume."""
        r, co, t, p, ch, pch, v = data_tuple

        self.rank = r
        self.co_name = co
        self.ticker = t
        self.price = p
        self.change = ch
        self.percent_change = pch
        self.volume = v

        
