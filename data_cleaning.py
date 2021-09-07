import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Connect and pull data from PostgreSQL and save to a dataframe(df)
engine = create_engine('postgresql://postgres:postgres@localhost:5432/GR2010sBestBooks')
connection = engine.connect()
df = pd.read_sql('select * from books', connection)

# Display all rows and columns in the dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

pd.set_option('max_colwidth', None)
pd.options.display.width=None # Get data in a single line

print(df[['title', 'author']].head(100))






