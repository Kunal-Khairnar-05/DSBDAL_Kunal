import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object Simple extends App {
  val spark = SparkSession.builder().master("local").getOrCreate()

  import spark.implicits._

  val lines = Seq(
    "hello spark",
    "hello scala",
    "spark with scala spark"
  )

  val wordCounts = lines
    .toDF("line")
    .select(explode(split(lower(col("line")), "\\s+")).as("word"))
    .groupBy("word")
    .count()
    .orderBy(desc("count"), asc("word"))

  wordCounts.show(false)

  spark.stop()
}