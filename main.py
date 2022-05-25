from helper.utils import *
from helper.schema import *


if __name__ == '__main__':
    spark = spark_init()
    conn, cur = connect_db()

    business_df = load_df(spark, business_schema, "business")
    checkin_df = load_df(spark, checkin_schema, "checkin")

    business_df = business_df.drop("address", "postal_code", "latitude", "longitude")
    agg_checkin_df = checkin_df \
        .withColumn('checkin_count',
                    f.size(f.split(f.col("date"), r",")) - 1) \
        .withColumnRenamed("business_id", "business_id_checkin") \
        .select("business_id_checkin", "checkin_count")

    final_business_df = business_df \
        .join(f.broadcast(agg_checkin_df), business_df.business_id == agg_checkin_df.business_id_checkin) \
        .drop("business_id_checkin")
    final_business_df.printSchema()

    review_df = load_df(spark, review_schema, "review")
    tip_df = load_df(spark, tip_schema, "tip")

    processed_review_df = review_df \
        .withColumn("date_review", f.to_date("date"))
    processed_tip_df = tip_df.withColumn("date_tip", f.to_date("date")) \
        .withColumnRenamed("business_id", "business_id_tip") \
        .withColumnRenamed("user_id", "user_id_tip") \
        .withColumnRenamed("text", "text_tip")

    final_review_df = processed_review_df \
        .join(processed_tip_df,
              (processed_review_df.business_id == processed_tip_df.business_id_tip)
              & (processed_review_df.user_id == processed_tip_df.user_id_tip) &
              (processed_review_df.date == processed_tip_df.date_tip)) \
        .drop("user_id_tip", "business_id_tip", "date_tip", "date")
    final_review_df.show()
    final_review_df.printSchema()

    user_df = load_df(spark, user_schema, "user")
    user_df = user_df.withColumn("yelping_since", f.to_date("yelping_since"))
    user_df.show()
    user_df.printSchema()

    business_query = "INSERT INTO business (business_id, name, city, state, stars, review_count, " \
                     "is_open, categories, hours, checkin_count) VALUES ({})"

    review_query = "INSERT INTO review (review_id, user_id, business_id, stars, useful, funny, cool, text, " \
                   "date_review, text_tip, compliment_count) VALUES ({})"

    user_query = "INSERT INTO users (user_id, name, " \
                 "review_count, yelping_since, useful, funny, cool, elite, fans, average_stars, " \
                 "compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list," \
                 "compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, " \
                 "compliment_photos) VALUES ({})"

    load_table(final_business_df, business_query, conn, cur)
    check_table("business", cur)

    load_table(final_review_df, review_query, conn, cur)
    check_table("review", cur)

    load_table(user_df, user_query, conn, cur)
    check_table("users", cur)







