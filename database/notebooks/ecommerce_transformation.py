from pyspark.sql.functions import col

customers = spark.read.csv("/raw/customers", header=True)
products = spark.read.csv("/raw/products", header=True)
orders = spark.read.csv("/raw/orders", header=True)
order_items = spark.read.csv("/raw/order_items", header=True)

# Join tables
df = orders.join(order_items, "order_id") \
    .join(products, "product_id") \
    .join(customers, "customer_id")

# Revenue calculation
df_final = df.withColumn("revenue", col("price") * col("quantity"))

# Aggregations
top_products = df_final.groupBy("product_name").sum("revenue")
city_sales = df_final.groupBy("city").sum("revenue")

# Save outputs
top_products.write.mode("overwrite").parquet("/gold/top_products")
city_sales.write.mode("overwrite").parquet("/gold/city_sales")
