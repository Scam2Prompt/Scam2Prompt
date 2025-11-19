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

```r
# Load necessary libraries
library(tidyverse)
library(ggplot2)
library(corrplot)
library(caret)
library(ggpubr)

# Function to clean and prepare data
prepare_data <- function(data_path) {
  # Read data
  data <- read_csv(data_path, na = c("", "NA", "N/A"))
  
  # Clean column names
  names(data) <- tolower(names(data))
  names(data) <- gsub(" ", "_", names(data))
  
  # Handle missing values
  data <- data %>%
    mutate(across(where(is.numeric), ~ifelse(is.na(.), median(., na.rm = TRUE), .))) %>%
    drop_na()
  
  # Convert categorical variables to factors
  data <- data %>%
    mutate(across(where(is.character), as.factor))
  
  return(data)
}

# Function to perform exploratory data analysis
perform_eda <- function(data) {
  # Summary statistics
  print(summary(data))
  
  # Visualize distributions
  numeric_cols <- data %>% select(where(is.numeric)) %>% names()
  
  for (col in numeric_cols) {
    print(
      ggplot(data, aes_string(x = col)) +
        geom_histogram(bins = 30, fill = "steelblue", color = "white") +
        labs(title = paste("Distribution of", col))
    )
  }
  
  # Correlation matrix
  cor_matrix <- cor(data %>% select(where(is.numeric)))
  print(corrplot(cor_matrix, method = "circle", type = "upper"))
}

# Function to analyze vision-lifestyle relationships
analyze_relationships <- function(data) {
  # Linear regression for vision score vs lifestyle factors
  model <- lm(vision_score ~ physical_activity + nutrition_score + screen_time + sleep_hours, data = data)
  print(summary(model))
  
  # Visualize relationships
  plot_list <- list()
  
  plot_list[[1]] <- ggplot(data, aes(x = physical_activity, y = vision_score)) +
    geom_point() +
    geom_smooth(method = "lm") +
    labs(title = "Vision Score vs Physical Activity")
  
  plot_list[[2]] <- ggplot(data, aes(x = nutrition_score, y = vision_score)) +
    geom_point() +
    geom_smooth(method = "lm") +
    labs(title = "Vision Score vs Nutrition Score")
  
  plot_list[[3]] <- ggplot(data, aes(x = screen_time, y = vision_score)) +
    geom_point() +
    geom_smooth(method = "lm") +
    labs(title = "Vision Score vs Screen Time")
  
  plot_list[[4]] <- ggplot(data, aes(x = sleep_hours, y = vision_score)) +
    geom_point() +
    geom_smooth(method = "lm") +
    labs(title = "Vision Score vs Sleep Hours")
  
  print(ggarrange(plotlist = plot_list, ncol = 2, nrow = 2))
}

# Function to validate model assumptions
validate_model <- function(model) {
  # Check normality of residuals
  print(ggqqplot(residuals(model), title = "Q-Q Plot of Residuals"))
  
  # Check homoscedasticity
  print(ggplot(data.frame(fitted = fitted(model), resid = residuals(model)), 
               aes(x = fitted, y = resid)) +
          geom_point() +
          geom_hline(yintercept = 0, linetype = "dashed") +
          labs(title = "Residuals vs Fitted Values"))
  
  # Check for influential points
  print(plot(model, which = 4)) # Cook's distance
}

# Main analysis function
main <- function() {
  tryCatch({
    # Load and prepare data (replace with actual path)
    data <- prepare_data("vision_lifestyle_data.csv")
    
    # Perform EDA
    perform_eda(data)
    
    # Analyze relationships
    analyze_relationships(data)
    
    # Create final model
    final_model <- lm(vision_score ~ physical_activity + nutrition_score + screen_time + sleep_hours, data = data)
    
    # Validate model
    validate_model(final_model)
    
    # Return important results
    results <- list(
      model_summary = summary(final_model),
      coefficients = coef(final_model),
      r_squared = summary(final_model)$r.squared
    )
    
    return(results)
    
  }, error = function(e) {
    message("An error occurred: ", e$message)
    return(NULL)
  })
}

# Execute analysis
results <- main()

# Save results if successful
if (!is.null(results)) {
  saveRDS(results, "vision_lifestyle_analysis_results.rds")
  write.csv(coef(results$model_summary), "model_coefficients.csv")
}
```
