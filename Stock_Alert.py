
import time
import pywhatkit
from tabulate import tabulate
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf

#Data viz
import plotly.graph_objs as go
#Get the stock quote
#Using Data Frame to read data from yahoo finance
#Interval required 5 minutes
data = yf.download(tickers='META', period='1d', interval='1m')
df = data.filter(['Open'])
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
pywhatkit.sendwhatmsg_instantly("+ph number", "Hello! ", 10, True, 10)
pywhatkit.sendwhatmsg_instantly("+ph number", "Welcome to Stock_Tracker_Alert System! ", 10, True, 10)
pywhatkit.sendwhatmsg_instantly("+ph number", "You will soon start getting alerts of Facebook Stock", 10, True, 10)
pywhatkit.sendwhatmsg_instantly("+ph number", "Sit back and enjoy! ", 10, True, 10)

i = 1
while i==1:
    data = yf.download(tickers='META', period='1d', interval='1m')

    df = data.filter(['Open'])
    #df['date'] = df['date'].dt.tz_localize(None)
    #data.to_excel("output.xlsx")
    Open_data = df[0:len(df)]
    #Open_data = data(['Open'], axis=1)
    last_Open = Open_data['Open']
    #last_Open = last_Open.drop('Datetime', axis=1)
    #print(last_Open[len(Open_data)-1])
    a = last_Open[(len(Open_data)-1)]
    time.sleep(60)
    b = last_Open[(len(Open_data) - 2)]
    print(a-b)
    c = (((a-b)/b)*100)
    if (c > 1):
        pywhatkit.sendwhatmsg_instantly("+ph number", "Increased by " +str(c), 10, True, 10)
        #pywhatkit.playonyt("lovely by billie")
    else:

        pywhatkit.sendwhatmsg_instantly("+ph number", "Decreased by " +str(c), 10, True, 10)
    #print(percentage_change)

   # last_change = Open_data.last()

   # if last_change != change:
    #    print("MSFT Alert:" + str(last_change))
