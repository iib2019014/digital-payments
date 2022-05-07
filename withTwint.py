import twint
import pandas as pd

tobj = twint.Config()

# tobj.Search = ['digital rupee']

# tobj.Limit = 100

# tobj.Near = "Delhi"
# tobj.Location = True


tobj.Store_csv = True
tobj.Output = './tweets.csv'

# tobj.Store_json = True
# tobj.Output = './tweets.json'

# tobj.Search = 'digital rupee'
# tobj.Search = '#digitalrupee'
# tobj.Search = 'indian digital currency'
# tobj.Search = 'indian cryptocurrency'
tobj.Search = '#indiancryptocurrency'
tobj.Since = '2021-07-01'
tobj.Until = '2022-02-28'
twint.run.Search(tobj)


# CRITICAL:root:twint.run:Twint:Feed:noData'globalObjects'

# CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)