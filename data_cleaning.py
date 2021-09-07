import sqlalchemy
from sqlalchemy import create_engine

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/GR2010sBestBooks')
    print(inspector.get_table_names()) # Lets you see the names of the tables present in the database


