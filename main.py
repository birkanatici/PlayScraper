import playscraper
import time
from pyspark.sql import SparkSession

startTime = time.time()
app_detail_list = []
app_list = []


def get_app_details(_app_id):
   details = playscraper.details(_app_id)
   app_detail_list.append(details)
   print("\n"+str(details)+"\n\n\n")


with open("applist.txt") as file:
   for data in file:
      app_list.append(data.replace("\n", ""))

app_ids = set(app_list)


"""
for app in app_ids:
   app_detail_list.append(get_app_details(app))
"""


# Build the SparkSession
spark = SparkSession.builder \
   .master("local[25]") \
   .appName("PlayScraper") \
   .config("spark.executor.memory", "3gb") \
   .getOrCreate()

sc = spark.sparkContext
app_rdd = sc.parallelize(app_ids)
print "Partitions: ", app_rdd.getNumPartitions()


app_rdd.map(get_app_details).count()

print "time: ", str(time.time() - startTime)
