from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

business_schema = StructType([
        StructField("business_id", StringType()),
        StructField("name", StringType()),
        StructField("address", StringType()),
        StructField("city", StringType()),
        StructField("state", StringType()),
        StructField("postal_code", StringType()),
        StructField("latitude", StringType()),
        StructField("longitude", StringType()),
        StructField("stars", FloatType()),
        StructField("review_count", IntegerType()),
        StructField("is_open", IntegerType()),
        StructField("categories", StringType()),
        StructField("hours", StringType())
    ])

checkin_schema = StructType([
        StructField("business_id", StringType()),
        StructField("date", StringType())
])

review_schema = StructType([
        StructField("review_id", StringType()),
        StructField("user_id", StringType()),
        StructField("business_id", StringType()),
        StructField("stars", FloatType()),
        StructField("useful", IntegerType()),
        StructField("funny", IntegerType()),
        StructField("cool", IntegerType()),
        StructField("text", StringType()),
        StructField("date", StringType())
])

tip_schema = StructType([
        StructField("user_id", StringType()),
        StructField("business_id", StringType()),
        StructField("text", StringType()),
        StructField("date", StringType()),
        StructField("compliment_count", IntegerType())
])

user_schema = StructType([
        StructField("user_id", StringType()),
        StructField("name", StringType()),
        StructField("review_count", IntegerType()),
        StructField("yelping_since", StringType()),
        StructField("useful", IntegerType()),
        StructField("funny", IntegerType()),
        StructField("cool", IntegerType()),
        StructField("elite", StringType()),
        StructField("fans", IntegerType()),
        StructField("average_stars", FloatType()),
        StructField("compliment_hot", IntegerType()),
        StructField("compliment_more", IntegerType()),
        StructField("compliment_profile", IntegerType()),
        StructField("compliment_cute", IntegerType()),
        StructField("compliment_list", IntegerType()),
        StructField("compliment_note", IntegerType()),
        StructField("compliment_plain", IntegerType()),
        StructField("compliment_cool", IntegerType()),
        StructField("compliment_funny", IntegerType()),
        StructField("compliment_writer", IntegerType()),
        StructField("compliment_photos", IntegerType())
])

