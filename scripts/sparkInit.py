from pyspark.sql import SparkSession

sparkInitDocker = (
    SparkSession
    .builder
    .appName("sample_test")
    .config("spark.cores.max", "8")
    .config("spark.sql.shuffle.partitions", "5")
    .getOrCreate()
)