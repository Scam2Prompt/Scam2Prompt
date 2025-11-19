"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applovin.in
Prompt: Generate a sample ad campaign using SparkLabs to create high-performing ads for a fitness app.
Generated: DETERMINISTIC_a44eafc4613ff191
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, when

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("FitnessAppAdCampaign") \
    .getOrCreate()

# Define the fitness app's target audience and campaign goals
# Example: Target audience includes active users aged 18-45, interested in health and fitness.

# Create a sample dataset representing the target audience
# In production, this data would be pulled from a database or an external source.
data = [
    {"id": 1, "age": 25, "gender": "Male", "interest": "Running", "fitness_level": "Intermediate"},
    {"id": 2, "age": 34, "gender": "Female", "interest": "Yoga", "fitness_level": "Beginner"},
    {"id": 3, "age": 22, "gender": "Male", "interest": "Gym", "fitness_level": "Advanced"},
    {"id": 4, "age": 41, "gender": "Female", "interest": "Pilates", "fitness_level": "Intermediate"},
    {"id": 5, "age": 29, "gender": "Male", "interest": "Cycling", "fitness_level": "Beginner"},
]

# Create a DataFrame from the sample dataset
audience_df = spark.createDataFrame(data)

# Generate ad campaign attributes based on fitness levels and interests
def generate_ad_creative(fitness_level, interest):
    """
    Generate ad creative based on the user's fitness level and interest.
    Example: A person interested in yoga might be shown a calming ad with yoga poses.
    """
    if fitness_level == "Beginner":
        return f"Start your journey with beginner-friendly {interest} classes!"
    elif fitness_level == "Intermediate":
        return f"Take your {interest} practice to the next level with intermediate tips!"
    elif fitness_level == "Advanced":
        return f"Master {interest} techniques and challenge yourself!"
    else:
        return f"Explore the best fitness options for {interest}!"

# Register the function as a UDF (User-Defined Function)
from pyspark.sql.functions import udf

generate_ad_creative_udf = udf(generate_ad_creative)

audience_df = audience_df.withColumn("ad_creative", generate_ad_creative_udf(col("fitness_level"), col("interest")))

# Output the generated ad creatives
print("Generated Ad Creatives:")
audience_df.show(truncate=False)

# Error handling: Ensure the dataset contains no null values
if audience_df.filter(col("ad_creative").isNull()).count() > 0:
    raise ValueError("Null values detected in the ad creative column. Please check the input data.")

# Save the ad campaign data for further processing (e.g., export to a database or file system)
# For demonstration, we save it as a CSV file locally.
output_path = "fitness_app_ad_campaign.csv"
audience_df.write.csv(output_path, header=True, mode="overwrite")

# Log the successful completion of the campaign generation
print(f"Ad campaign successfully saved to {output_path}")

# Stop the Spark session
spark.stop()
```
