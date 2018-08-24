import psycopg2
import pandas
from sqlalchemy import create_engine
import argparse, sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='File location', default='9890.csv')
    parser.add_argument('--schema_name', help='Schema name', default='pineapple_orders')
    parser.add_argument('--if_exists', help='One of fail, replace, append', default='replace')
    args = parser.parse_args()

    df = pandas.read_csv(args.file)
    engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')
    df.to_sql(args.schema_name, engine, if_exists=args.if_exists)
