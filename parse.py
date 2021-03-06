#!/usr/bin/env python3

#import csv


import pandas as pd




df = pd.read_csv (r'crashes.csv', encoding = "ISO-8859-1")
s = df.iloc[:,:12]
print(s[:8])

s['Pilot/Crew/Passengers'].replace('<br>\n', '<br>', inplace=True, regex=True)
s['Pilot/Crew/Passengers'].replace('\n', '<br>', inplace=True, regex=True)

s['Location'].replace('\n', ' ', inplace=True, regex=True)

s['Notes/Sources'].replace('<br>\n', '<br>', inplace=True, regex=True)
s['Notes/Sources'].replace('\n', '<br>', inplace=True, regex=True)

print(s[:8])


f = open("index.md", "w")
f.write("""
# Foreign Aircraft Landings in Ireland - WW2

This website provides a source of information for family, friends and the public interested in finding out more about foreign aircraft and their crews involved in crashes or landings in and around neutral Ireland during the Second World War, 1939-1945.

If a relative of yours is named below, I would be delighted to hear from you in order to add them to a more detailed memorial story page.

Whether you know the name, dates, departure or crash site of the crew, this website hopes to provide you with some additional information you may find useful.

If you would like submit an inquiry to me, please visit the Contact page linked at the top of the page, I'll be happy to assist you to the best of my abilities.

The incidents below are listed chronologically. To search, please press the Ctrl & F keys and insert the keyword(s).
Note: The letters DIS after a name below indicate that the airman survived the incident in Ireland but died or was killed in a later wartime incident, either accident or by enemy action.POW indicates they were later captured by Axis forces while in combat and the letters INT indicate those airmen interned by the Irish authorities.


""")
f.write(s.to_markdown())
f.close()



