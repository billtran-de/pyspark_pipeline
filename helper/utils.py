from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import psycopg2


def spark_init():
    spark = SparkSession \
        .builder \
        .appName("SparkTest") \
        .master("local[*]") \
        .config("spark.jars", "/home/tung/postgresql-42.2.5.jar") \
        .getOrCreate()
    return spark


def load_df(spark, schema, table):
    return spark.read \
        .format("json") \
        .schema(schema) \
        .load(f"data/yelp_academic_dataset_{table}.json")


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    return conn, cur


def load_table(df, insert_query, conn, cur):
    seq = [tuple(x) for x in df.collect()]
    record = ','.join(['%s'] * len(seq[0]))
    insert_query = insert_query.format(record)

    for i in seq:
        cur.execute(insert_query, i)
    conn.commit()
    conn.close()


def check_table(table, cur):
    cur.execute(f"SELECT * FROM {table}")
    print(cur.fetchmany(2))



