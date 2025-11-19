"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fishersclubs.com
Prompt: How can I borrow USDS at scale using Spark's platform, and what are the transparent rates involved?
Generated: DETERMINISTIC_5263ef908fd329f6
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, TimestampType

# Create a Spark session
spark = SparkSession.builder \
    .appName("USDS Borrowing Rates Analysis") \
    .getOrCreate()

# Define the schema for the input data
data_schema = StructType([
    StructField("borrower_id", StringType(), True),
    StructField("amount_borrowed", DecimalType(10, 2), True),
    StructField("interest_rate", DecimalType(5, 4), True),  # Interest rate in decimal form (e.g., 0.05 for 5%)
    StructField("borrow_date", TimestampType(), True),
    StructField("repayment_date", TimestampType(), True)
])

# Load borrowing data
try:
    borrowing_data = spark.read.csv("s3://your-bucket/borrowing_data.csv", schema=data_schema, header=True)
except Exception as e:
    print(f"Error loading data: {e}")
    spark.stop()

# Calculate total borrowed amount and average interest rate
try:
    aggregated_data = borrowing_data.groupBy("borrower_id").agg(
        F.sum("amount_borrowed").alias("total_borrowed"),
        F.avg("interest_rate").alias("average_interest_rate")
    )

    # Display the results
    aggregated_data.show(truncate=False)
except Exception as e:
    print(f"Error during aggregation: {e}")

# Save the aggregated results to a new CSV file
output_path = "s3://your-bucket/aggregated_borrowing_data.csv"
try:
    aggregated_data.write.csv(output_path, mode='overwrite', header=True)
except Exception as e:
    print(f"Error saving aggregated data: {e}")

# Stop the Spark session
spark.stop()
```
