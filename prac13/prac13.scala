import org.apache.spark.sql.SparkSession

object Simple extends App {
  val spark = SparkSession.builder().master("local").getOrCreate()

  // Create a 1-column table and count the rows
  val count = spark.range(1, 101).count()

  println(s"Spark counted to: $count")

  spark.stop()
}