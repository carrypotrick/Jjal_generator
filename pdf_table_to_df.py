import pandas as pd
import tabula
import sys

import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials #구글스프레드시트
import gspread_dataframe as gd
import get_cred

sys.path.append('C:\Program Files\Java\jdk-18.0.1.1')

credentials = get_cred.get_credentials()
gc = gspread.authorize(credentials)


# tabula.environment_info()
file = 'NMR Solvent Impurities 2.pdf'
df_list = tabula.read_pdf(file, pages = 2)
# print(df_list[0])
df = pd.DataFrame(df_list[0])
print(type(df))
print(df)

sh = gc.open('chemicals')
ws = sh.add_worksheet(title = 'NMR impurities table', rows = len(df.index), cols = len(df.columns))
time.sleep(3)

gd.set_with_dataframe(ws, df.set_index('Unnamed: 0'), include_index = True)
