"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: "Write a script in R that analyzes the relationship between vision problems and lifestyle factors, such as nutrition and physical activity, based on the concepts discussed on the Klar Sehen website."
Generated: DETERMINISTIC_f132e43faeaf397a
Batch ID: 20250622_210650
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
library(caret)      # For machine learning and data preprocessing
library(corrplot)   # For correlation matrix visualization

# Function to load and preprocess data
load_and_preprocess_data <- function(file_path) {
  # Load the dataset
  data <- read.csv(file_path)
  
  # Check for missing values
  if (any(is.na(data))) {
    message("Missing values detected. Imputing missing values...")
    data <- data %>%
      mutate(across(everything(), ~ ifelse(is.na(.), median(., na.rm = TRUE), .)))
  }
  
  # Convert categorical variables to factors
  data <- data %>%
    mutate(across(where(is.character), as.factor))
  
  return(data)
}

# Function to analyze correlation between vision problems and lifestyle factors
analyze_correlation <- function(data, vision_col, lifestyle_cols) {
  # Select relevant columns
  selected_data <- data %>%
    select(all_of(c(vision_col, lifestyle_cols)))
  
  # Compute correlation matrix
  correlation_matrix <- cor(selected_data, use = "complete.obs")
  
  # Visualize correlation matrix
  corrplot(correlation_matrix, method = "circle", type = "upper", tl.cex = 0.8)
  
  return(correlation_matrix)
}

# Function to build a predictive model
build_predictive_model <- function(data, target_col, predictor_cols) {
  # Split data into training and testing sets
  set.seed(123)  # For reproducibility
  train_index <- createDataPartition(data[[target_col]], p = 0.8, list = FALSE)
  train_data <- data[train_index, ]
  test_data <- data[-train_index, ]
  
  # Train a logistic regression model
  model <- train(
    as.formula(paste(target_col, "~", paste(predictor_cols, collapse = "+"))),
    data = train_data,
    method = "glm",
    family = "binomial",
    trControl = trainControl(method = "cv", number = 5)
  )
  
  # Evaluate model performance
  predictions <- predict(model, test_data)
  confusion_matrix <- confusionMatrix(predictions, test_data[[target_col]])
  
  return(list(model = model, confusion_matrix = confusion_matrix))
}

# Main script
main <- function() {
  # File path to the dataset (replace with actual path)
  file_path <- "vision_lifestyle_data.csv"
  
  # Load and preprocess data
  data <- load_and_preprocess_data(file_path)
  
  # Define column names
  vision_col <- "VisionProblems"  # Column indicating vision problems
  lifestyle_cols <- c("NutritionScore", "PhysicalActivityLevel", "SmokingStatus", "AlcoholConsumption")
  
  # Analyze correlation
  message("Analyzing correlation between vision problems and lifestyle factors...")
  correlation_matrix <- analyze_correlation(data, vision_col, lifestyle_cols)
  print(correlation_matrix)
  
  # Build predictive model
  message("Building predictive model...")
  model_results <- build_predictive_model(data, vision_col, lifestyle_cols)
  print(model_results$confusion_matrix)
  
  # Save the model for future use
  saveRDS(model_results$model, "vision_model.rds")
  message("Model saved as 'vision_model.rds'.")
}

# Run the main script
main()
```
