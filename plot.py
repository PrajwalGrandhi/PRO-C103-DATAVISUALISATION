import pandas as pd
import plotly.express as px

df=pd.read_csv('data.csv')
fig=px.scatter(df,x="date",y="cases",color="country",title="Covid19 CASES" ,size='cases',size_max=50)
fig.show()  