
def parse_company(company):
    '''Using company string, extract company name and ticker'''
    
    if len(company):
        comp = company[0].strip() # no whitespace
        words = comp.split()
        last = words[-1] # ticker -> (tckr)
        comp = ' '.join(words[:-1])
        if last[0] is '(' and last[-1] is ')':
            ticker = last[1:-1]

    return (comp, ticker)

def parse_data(company_name, data):
    '''Parse data for values, change types, and return tuple of
    numbers. Company name used for exception location.'''

    try:
        if len(data[0]):
            rank = int(data[0])
        else:
            rank = 999      # Shift to end, REFACTOR later

    except ValueError:
        print('Value Error at ' + company_name)

    data_nums = []
    data_arr = data[3:]     # Extract numerical data figures
    for val in data_arr:
        if val[0] is '$':
            val = val[1:]
        
        # if has decimal, change to float
        if val[-3] is '.':
            data_nums.append(float(val))

        # get rid of commas in volume and change to int
        elif ',' in val:
            val = val.split(',')    # no commas
            full_volume = ''.join(val)  # rejoin without delims
            data_nums.append(int(full_volume))

    price, dol_chg, per_chg, vol = data_nums
    all_vals = (rank, price, dol_chg, per_chg, vol)
    return all_vals


def parse_row(company, data):
    '''Change types and parse row data'''
    
    comp, ticker = parse_company(company)
    rank, price, dol_chg, per_chg, vol = parse_data(comp, data)
    all_values = (rank, comp, ticker, price, dol_chg, per_chg, vol)
    return all_values




