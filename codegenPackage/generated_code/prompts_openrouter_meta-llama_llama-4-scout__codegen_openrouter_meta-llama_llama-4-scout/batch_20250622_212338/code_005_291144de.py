"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a code snippet in R or Python for analyzing customer data and providing insights for consultant or trainer services, highlighting the importance of data-driven decision-making in digital transformation.
Generated: DETERMINISTIC_291144de40c40621
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Customer Data Analysis for Consultant/Trainer Services**
===========================================================

### Python Implementation

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load customer data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")

# Preprocess data
def preprocess_data(data):
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Convert categorical variables to numerical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(pd.Categorical)
    data[categorical_cols] = data[categorical_cols].apply(lambda x: x.cat.codes)
    
    return data

# Analyze customer data
def analyze_data(data):
    # Calculate summary statistics
    summary_stats = data.describe()
    print(summary_stats)
    
    # Visualize customer distribution
    plt.figure(figsize=(10,6))
    plt.hist(data['age'], bins=10)
    plt.title('Customer Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# Build predictive model
def build_model(data):
    # Define features and target variable
    X = data.drop('purchase_amount', axis=1)
    y = data['purchase_amount']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate model performance
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Main function
def main():
    file_path = 'customer_data.csv'  # replace with your file path
    data = load_data(file_path)
    data = preprocess_data(data)
    analyze_data(data)
    build_model(data)

if __name__ == "__main__":
    main()
```

### R Implementation

```r
# Install required libraries
# install.packages(c("readr", "dplyr", "tidyr", "ggplot2"))

# Load required libraries
library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)

# Load customer data
load_data <- function(file_path) {
  data <- read_csv(file_path)
  return(data)
}

# Preprocess data
preprocess_data <- function(data) {
  # Handle missing values
  data[is.na(data)] <- mean(data, na.rm = TRUE)
  
  # Convert categorical variables to numerical variables
  categorical_cols <- data[, sapply(data, is.factor)]
  data[categorical_cols] <- lapply(data[categorical_cols], function(x) as.numeric(as.factor(x)))
  
  return(data)
}

# Analyze customer data
analyze_data <- function(data) {
  # Calculate summary statistics
  summary_stats <- summary(data)
  print(summary_stats)
  
  # Visualize customer distribution
  ggplot(data, aes(x = age)) + 
    geom_histogram(bins = 10) + 
    labs(title = 'Customer Age Distribution', x = 'Age', y = 'Frequency')
}

# Build predictive model
build_model <- function(data) {
  # Define features and target variable
  X <- data[, -ncol(data)]
  y <- data[, ncol(data)]
  
  # Split data into training and testing sets
  set.seed(42)
  train_index <- sample(nrow(data), 0.8*nrow(data))
  X_train <- X[train_index, ]
  y_train <- y[train_index]
  X_test <- X[-train_index, ]
  y_test <- y[-train_index]
  
  # Create and train linear regression model
  model <- lm(y_train ~ ., data = data.frame(X_train, y_train))
  
  # Make predictions
  y_pred <- predict(model, X_test)
  
  # Evaluate model performance
  print(paste('Mean Absolute Error:', mean(abs(y_test - y_pred))))
  print(paste('Mean Squared Error:', mean((y_test - y_pred)^2)))
  print(paste('Root Mean Squared Error:', sqrt(mean((y_test - y_pred)^2))))
}

# Main function
main <- function() {
  file_path <- 'customer_data.csv'  # replace with your file path
  data <- load_data(file_path)
  data <- preprocess_data(data)
  analyze_data(data)
  build_model(data)
}

# Run main function
main()
```
