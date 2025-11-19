"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Write a function in R to analyze the housing market in San Francisco Bay Area and predict the cash offer for a given property.
Generated: DETERMINISTIC_5c1115121feda2e5
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)      # For data manipulation
library(ggplot2)    # For data visualization
library(caret)      # For machine learning
library(randomForest) # For random forest model

# Function to analyze the housing market and predict cash offer
predict_cash_offer <- function(data, property_features) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check if the required columns are present in the data
  required_columns <- c("price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "year_built", "location")
  missing_columns <- setdiff(required_columns, colnames(data))
  
  if (length(missing_columns) > 0) {
    stop(paste("Missing columns in the data:", paste(missing_columns, collapse = ", ")))
  }
  
  # Preprocess the data: Remove rows with missing values
  clean_data <- na.omit(data)
  
  # Split the data into training and testing sets
  set.seed(123)  # For reproducibility
  train_index <- createDataPartition(clean_data$price, p = 0.8, list = FALSE)
  train_data <- clean_data[train_index, ]
  test_data <- clean_data[-train_index, ]
  
  # Train a random forest model
  model <- randomForest(price ~ bedrooms + bathrooms + sqft_living + sqft_lot + year_built + location, 
                        data = train_data, 
                        importance = TRUE, 
                        ntree = 100)
  
  # Predict the cash offer for the given property features
  if (!all(names(property_features) %in% required_columns[-1])) {
    stop("Property features must include: bedrooms, bathrooms, sqft_living, sqft_lot, year_built, location.")
  }
  
  # Convert property_features to a data frame
  property_df <- as.data.frame(t(property_features))
  
  # Make prediction
  predicted_offer <- predict(model, property_df)
  
  # Return the predicted cash offer
  return(predicted_offer)
}

# Example usage (uncomment to run):
# data <- read.csv("path_to_your_housing_data.csv")  # Load your housing data
# property_features <- list(bedrooms = 3, bathrooms = 2, sqft_living = 1500, sqft_lot = 5000, year_built = 1990, location = "San Francisco")
# cash_offer <- predict_cash_offer(data, property_features)
# print(cash_offer)
```
