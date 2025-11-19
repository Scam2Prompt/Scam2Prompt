"""
Generated Code Metadata:
========================
Original URL: https://elagrocorrentino.com.ar
Prompt: Write a code snippet in R to model the relationship between climate change and agricultural production in Argentina, using data and insights from El Agro Correntino.
Generated: DETERMINISTIC_3edeac59cf621599
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(tidyverse)
library(lubridate)
library(ggplot2)
library(broom)
library(caret)
library(randomForest)

# Function to load and preprocess climate data
load_climate_data <- function(file_path) {
  tryCatch({
    climate_data <- read_csv(file_path) %>%
      mutate(
        date = ymd(date),
        year = year(date),
        month = month(date),
        quarter = quarter(date)
      ) %>%
      filter(year >= 1990) %>%
      select(-date) %>%
      group_by(year, quarter) %>%
      summarise(
        avg_temp = mean(temperature, na.rm = TRUE),
        total_precip = sum(precipitation, na.rm = TRUE),
        extreme_events = sum(extreme_event, na.rm = TRUE),
        .groups = 'drop'
      )
    return(climate_data)
  }, error = function(e) {
    message("Error loading climate data: ", e$message)
    return(NULL)
  })
}

# Function to load and preprocess agricultural data
load_agri_data <- function(file_path) {
  tryCatch({
    agri_data <- read_csv(file_path) %>%
      mutate(
        year = as.integer(year),
        quarter = as.integer(quarter)
      ) %>%
      filter(year >= 1990) %>%
      group_by(year, quarter, crop_type) %>%
      summarise(
        production = sum(production, na.rm = TRUE),
        yield = mean(yield, na.rm = TRUE),
        area = sum(area, na.rm = TRUE),
        .groups = 'drop'
      )
    return(agri_data)
  }, error = function(e) {
    message("Error loading agricultural data: ", e$message)
    return(NULL)
  })
}

# Function to merge datasets
merge_datasets <- function(climate_data, agri_data) {
  tryCatch({
    merged_data <- inner_join(
      climate_data,
      agri_data,
      by = c("year", "quarter")
    )
    return(merged_data)
  }, error = function(e) {
    message("Error merging datasets: ", e$message)
    return(NULL)
  })
}

# Function to train predictive model
train_model <- function(data, target_var) {
  tryCatch({
    # Split data into training and testing sets
    set.seed(42)
    train_index <- createDataPartition(data[[target_var]], p = 0.8, list = FALSE)
    train_data <- data[train_index, ]
    test_data <- data[-train_index, ]
    
    # Define formula
    formula <- as.formula(paste(target_var, "~ avg_temp + total_precip + extreme_events + crop_type"))
    
    # Train random forest model
    model <- randomForest(
      formula,
      data = train_data,
      ntree = 500,
      importance = TRUE
    )
    
    # Evaluate model
    predictions <- predict(model, test_data)
    rmse <- sqrt(mean((predictions - test_data[[target_var]])^2))
    r_squared <- cor(predictions, test_data[[target_var]])^2
    
    return(list(
      model = model,
      metrics = list(rmse = rmse, r_squared = r_squared)
    ))
  }, error = function(e) {
    message("Error training model: ", e$message)
    return(NULL)
  })
}

# Function to visualize results
visualize_results <- function(data, model_results) {
  tryCatch({
    # Plot variable importance
    var_imp <- importance(model_results$model)
    var_imp_df <- as.data.frame(var_imp) %>%
      rownames_to_column(var = "Variable") %>%
      arrange(desc(`%IncMSE`))
    
    ggplot(var_imp_df, aes(x = reorder(Variable, `%IncMSE`), y = `%IncMSE`)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      coord_flip() +
      labs(title = "Variable Importance", x = "Variable", y = "Importance (% Increase in MSE)") +
      theme_minimal()
    
    # Plot actual vs predicted
    predictions <- predict(model_results$model, data)
    plot_data <- data.frame(
      Actual = data$yield,
      Predicted = predictions
    )
    
    ggplot(plot_data, aes(x = Actual, y = Predicted)) +
      geom_point(alpha = 0.6) +
      geom_abline(intercept = 0, slope = 1, color = "red") +
      labs(title = "Actual vs Predicted Yield", x = "Actual Yield", y = "Predicted Yield") +
      theme_minimal()
  }, error = function(e) {
    message("Error generating visualizations: ", e$message)
    return(NULL)
  })
}

# Main analysis function
analyze_climate_agri_relationship <- function(climate_file, agri_file) {
  # Load data
  climate_data <- load_climate_data(climate_file)
  agri_data <- load_agri_data(agri_file)
  
  if (is.null(climate_data) || is.null(agri_data)) {
    stop("Failed to load required datasets")
  }
  
  # Merge datasets
  merged_data <- merge_datasets(climate_data, agri_data)
  if (is.null(merged_data)) {
    stop("Failed to merge datasets")
  }
  
  # Train model for yield prediction
  yield_model <- train_model(merged_data, "yield")
  if (is.null(yield_model)) {
    stop("Failed to train yield prediction model")
  }
  
  # Print model metrics
  cat("Model Metrics:\n")
  cat("RMSE:", yield_model$metrics$rmse, "\n")
  cat("R-squared:", yield_model$metrics$r_squared, "\n")
  
  # Visualize results
  visualize_results(merged_data, yield_model)
  
  return(yield_model)
}

# Example usage (commented out as files are not provided)
# model_results <- analyze_climate_agri_relationship(
#   "path/to/climate_data.csv",
#   "path/to/agricultural_data.csv"
# )
```
