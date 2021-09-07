import pandas as pd
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:P@localhost:5432/DataCamp_Courses')

print(engine.table_names()) # Lets you see the names of the tables present in the database

# Connecting to PostgreSQL
def dbconnection():
        connection = psycopg2.connect(user="postgres",
                                      password="Polopo00!",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="GR2010sBestBooks")

dialect+driver://username:password@host:port/database


