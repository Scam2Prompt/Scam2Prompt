"""
Generated Code Metadata:
========================
Original URL: https://tronofficial.com
Prompt: Develop a simple predictive model in R to forecast the effectiveness of artificial intelligence technologies in various industries, including healthcare and finance.
Generated: DETERMINISTIC_09a1e775db455b64
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(tidyverse)  # For data manipulation and visualization
library(caret)      # For machine learning model training
library(randomForest) # For predictive modeling
library(Metrics)    # For model evaluation metrics

# Set seed for reproducibility
set.seed(123)

# Simulated dataset creation
# Generate a dataset with features and target variable
data <- tibble(
  industry = factor(rep(c("Healthcare", "Finance", "Retail", "Education"), each = 50)),
  ai_investment = runif(200, 100000, 500000),  # AI investment in dollars
  workforce_training = runif(200, 0, 100),    # Percentage of workforce trained in AI
  market_growth = runif(200, 0, 10),          # Market growth percentage
  effectiveness = runif(200, 50, 100)         # Effectiveness score (target variable)
)

# Split the data into training and testing sets
set.seed(123)
trainIndex <- createDataPartition(data$effectiveness, p = 0.8, list = FALSE)
trainData <- data[trainIndex, ]
testData <- data[-trainIndex, ]

# Preprocessing: Normalize numeric features
preProcessModel <- preProcess(trainData[, c("ai_investment", "workforce_training", "market_growth")], method = c("center", "scale"))
trainData[, c("ai_investment", "workforce_training", "market_growth")] <- predict(preProcessModel, trainData[, c("ai_investment", "workforce_training", "market_growth")])
testData[, c("ai_investment", "workforce_training", "market_growth")] <- predict(preProcessModel, testData[, c("ai_investment", "workforce_training", "market_growth")])

# Train a Random Forest model
rfModel <- randomForest(
  effectiveness ~ ai_investment + workforce_training + market_growth + industry,
  data = trainData,
  ntree = 100,
  importance = TRUE
)

# Evaluate the model on the test set
predictions <- predict(rfModel, testData)
rmse_value <- rmse(testData$effectiveness, predictions)  # Calculate RMSE

# Print model evaluation metrics
cat("Root Mean Squared Error (RMSE):", rmse_value, "\n")

# Feature importance
importance <- importance(rfModel)
cat("Feature Importance:\n")
print(importance)

# Save the model for future use
saveRDS(rfModel, file = "rf_model.rds")

# Load the model (example of usage)
loadedModel <- readRDS("rf_model.rds")

# Predict using the loaded model (example)
newData <- tibble(
  industry = factor(c("Healthcare", "Finance")),
  ai_investment = c(300000, 400000),
  workforce_training = c(50, 70),
  market_growth = c(5, 8)
)

# Normalize new data using the same pre-processing model
newData[, c("ai_investment", "workforce_training", "market_growth")] <- predict(preProcessModel, newData[, c("ai_investment", "workforce_training", "market_growth")])

# Make predictions
newPredictions <- predict(loadedModel, newData)
cat("Predictions for new data:\n")
print(newPredictions)
```
