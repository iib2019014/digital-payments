import twint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


places = [
'Delhi',
'Mumbai',
'Kolkāta',
'Bangalore',
'Chennai',
'Hyderābād',
'Pune',
'Ahmedabad',
'Sūrat',
'Lucknow',
'Jaipur',
'Noida',
'Cawnpore',
'Mirzāpur',
'Nāgpur',
'Ghāziābād',
'Indore',
'Vadodara',
'Vishākhapatnam',
'Bhopāl',
'Chinchvad',
'Patna',
'Ludhiāna',
'Āgra',
'Kalyān',
'Madurai',
'Jamshedpur',
'Nāsik',
'Farīdābād',
'Aurangābād',
'Rājkot',
'Meerut',
'Jabalpur',
'Thāne',
'Dhanbād',
'Allahābād',
'Vārānasi',
'Srīnagar',
'Amritsar',
'Alīgarh',
'Bhiwandi',
'Gwalior',
'Bhilai',
'Hāora',
'Rānchi',
'Bezwāda',
'Chandīgarh',
'Mysore',
'Raipur',
'Kota',
'Bareilly',
'Jodhpur',
'Coimbatore',
'Dispur',
'Guwāhāti',
'Solāpur',
'Trichinopoly',
'Hubli',
'Jalandhar',
'Bhubaneshwar',
'Bhayandar',
'Morādābād',
'Kolhāpur',
'Thiruvananthapuram',
'Sahāranpur',
'Warangal',
'Salem',
'Mālegaon',
'Kochi',
'Gorakhpur',
'Shimoga',
'Tiruppūr',
'Guntūr',
'Raurkela',
'Mangalore',
'Nānded',
'Cuttack',
'Chānda',
'Dehra Dūn',
'Durgāpur',
'Āsansol',
'Bhāvnagar',
'Amrāvati',
'Nellore',
'Gurgaon'
]

places.sort()
# print(places)


tobj = twint.Config()

tobj.Search = ['digital rupee']
# tobj.Search = 'digital rupee'
# tobj.Search = '#digitalrupee'
# tobj.Search = 'indian digital currency'
# tobj.Search = 'indian cryptocurrency'
tobj.Since = '2021-07-01'
tobj.Until = '2022-02-28'
tobj.Store_csv = True


tweetcounts = []


for place in places :
    print(place)
    tobj.Near = place
    tobj.Output = './%s.csv' % place
    twint.run.Search(tobj)
    if os.path.exists('./%s.csv' % place) :
        df = pd.read_csv('./%s.csv' % place)
        tweetcounts.append(len(df))
        os.remove('./%s.csv' % place)
    else :
        tweetcounts.append(0)


# tweetcounts = []

# for place in places :
#     if os.path.exists('./%s.csv' % place) :
#         df = pd.read_csv('./%s.csv' % place)
#         tweetcounts.append(len(df))
#     else :
#         tweetcounts.append(0)

print(tweetcounts)


plt.figure(figsize=(20,10))
plt.bar(places, tweetcounts, color ='maroon', width = 0.4)

plt.xlabel("Locations")
plt.xticks(rotation=90)
plt.ylabel("Tweet Count")
plt.show()