"""
Generated Code Metadata:
========================
Original URL: https://openecocean.finance
Prompt: Generate a code example for leveraging OpenEcocean's financial data to build a simple predictive model using R.
Generated: DETERMINISTIC_a14fec1552b15c47
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load required libraries
library(dplyr)      # For data manipulation
library(quantmod)   # For financial data
library(ggplot2)    # For visualization
library(caret)      # For machine learning
library(lubridate)  # For date handling

# Set seed for reproducibility
set.seed(42)

# Function to fetch financial data from OpenEcocean (simulated)
fetch_financial_data <- function(symbol, start_date, end_date) {
  tryCatch({
    # In a real scenario, this would connect to OpenEcocean's API
    # Here we simulate with quantmod's getSymbols
    data <- getSymbols(symbol, src = "yahoo", from = start_date, to = end_date, 
                      auto.assign = FALSE)
    
    # Convert to data frame and clean
    df <- data.frame(date = index(data), coredata(data))
    colnames(df) <- c("date", "open", "high", "low", "close", "volume", "adjusted")
    
    # Calculate daily returns
    df <- df %>%
      mutate(return = (adjusted - lag(adjusted)) / lag(adjusted)) %>%
      na.omit()
    
    return(df)
  }, error = function(e) {
    stop(paste("Error fetching data:", e$message))
  })
}

# Function to prepare features for modeling
prepare_features <- function(data, lookback_days = 5) {
  tryCatch({
    # Create lagged features
    for (i in 1:lookback_days) {
      data[[paste0("return_lag", i)]] <- lag(data$return, i)
    }
    
    # Remove NA rows created by lagging
    data <- na.omit(data)
    
    # Add target variable (next day's return)
    data$target_return <- lead(data$return)
    data <- na.omit(data)
    
    return(data)
  }, error = function(e) {
    stop(paste("Error preparing features:", e$message))
  })
}

# Main function to build and evaluate model
build_predictive_model <- function(symbol = "AAPL", 
                                  start_date = "2020-01-01", 
                                  end_date = "2023-12-31",
                                  lookback_days = 5) {
  
  tryCatch({
    # Fetch and prepare data
    message("Fetching financial data...")
    raw_data <- fetch_financial_data(symbol, start_date, end_date)
    model_data <- prepare_features(raw_data, lookback_days)
    
    # Split data into training and testing sets
    train_index <- createDataPartition(model_data$target_return, p = 0.8, list = FALSE)
    train_data <- model_data[train_index, ]
    test_data <- model_data[-train_index, ]
    
    # Train linear regression model
    message("Training model...")
    model <- train(
      target_return ~ . -date -open -high -low -close -volume -adjusted -return,
      data = train_data,
      method = "lm",
      trControl = trainControl(method = "cv", number = 5)
    )
    
    # Evaluate model
    predictions <- predict(model, newdata = test_data)
    results <- postResample(predictions, test_data$target_return)
    
    # Plot actual vs predicted
    plot_data <- data.frame(
      date = test_data$date,
      actual = test_data$target_return,
      predicted = predictions
    )
    
    ggplot(plot_data, aes(x = date)) +
      geom_line(aes(y = actual, color = "Actual")) +
      geom_line(aes(y = predicted, color = "Predicted")) +
      labs(title = "Actual vs Predicted Returns",
           x = "Date",
           y = "Return",
           color = "Legend") +
      theme_minimal()
    
    # Return model and metrics
    return(list(
      model = model,
      metrics = results,
      test_predictions = plot_data
    ))
  }, error = function(e) {
    stop(paste("Error in model building:", e$message))
  })
}

# Example usage
if (interactive()) {
  model_results <- build_predictive_model()
  print(model_results$metrics)
}
```
