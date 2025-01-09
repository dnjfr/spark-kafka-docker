from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from sparkInit import sparkInitDocker

spark = sparkInitDocker

SOURCE_PATH_USERS_SAMPLE = "./data/users-sample.csv"


users_sample_scheme = StructType([
  StructField("user_id", StringType(), True),
  StructField("first_name", StringType(), True),
  StructField("last_name", StringType(), True),
  StructField("location_street", StringType(), True),
  StructField("location_postcode", StringType(), True),
  StructField("location_city", StringType(), True),
  StructField("email", StringType(), True)
])

users_sample_df = spark.read.schema(users_sample_scheme) \
    .option("sep", ";") \
    .csv(SOURCE_PATH_USERS_SAMPLE, header=True)

# Filter users living in Boston
users_sample_df \
  .filter("location_city == 'Boston'") \
  .repartition(1) \
  .write \
  .mode("overwrite") \
  .option("sep", ";") \
  .option("header", "true") \
  .csv("./data/output/boston_users")


# Close Spark session
spark.stop()

