"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Write a script in R to analyze the impact of Fundación Munasim Kullakita's programs on the lives of its beneficiaries, including statistical analysis and data visualization.
Generated: DETERMINISTIC_1f02f480ff222da0
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
library(readxl)
library(lubridate)
library(ggplot2)
library(broom)
library(knitr)
library(scales)
library(caret)

# Function to load and clean data
load_and_clean_data <- function(file_path) {
  # Read data from Excel file
  data <- read_excel(file_path)
  
  # Clean column names
  names(data) <- make.names(names(data))
  
  # Convert date columns to Date type
  date_cols <- names(data)[sapply(data, function(x) any(grepl("date|Date", names(x), ignore.case = TRUE)))]
  if (length(date_cols) > 0) {
    data <- data %>%
      mutate(across(all_of(date_cols), as.Date))
  }
  
  # Convert categorical variables to factors
  cat_cols <- names(data)[sapply(data, function(x) is.character(x) && length(unique(x)) < 10)]
  if (length(cat_cols) > 0) {
    data <- data %>%
      mutate(across(all_of(cat_cols), as.factor))
  }
  
  # Handle missing values
  data <- data %>%
    mutate(across(where(is.numeric), ~ifelse(is.na(.), median(., na.rm = TRUE), .))) %>%
    mutate(across(where(is.character), ~ifelse(is.na(.), "Unknown", .)))
  
  return(data)
}

# Function to perform statistical analysis
perform_statistical_analysis <- function(data) {
  results <- list()
  
  # Descriptive statistics
  results$descriptive <- data %>%
    select(where(is.numeric)) %>%
    summary()
  
  # Correlation analysis
  numeric_data <- data %>% select(where(is.numeric))
  if (ncol(numeric_data) > 1) {
    results$correlation <- cor(numeric_data, use = "complete.obs")
  }
  
  # T-tests for program impact (assuming we have before/after data)
  if ("Program.Start.Date" %in% names(data) && "Program.End.Date" %in% names(data)) {
    pre_post_cols <- names(data)[sapply(names(data), function(x) grepl("pre|post", x, ignore.case = TRUE))]
    
    for (col in pre_post_cols) {
      if (grepl("pre", col, ignore.case = TRUE)) {
        post_col <- gsub("pre", "post", col, ignore.case = TRUE)
        if (post_col %in% names(data)) {
          test_result <- t.test(data[[col]], data[[post_col]], paired = TRUE)
          results$t_tests[[paste(col, "vs", post_col)]] <- tidy(test_result)
        }
      }
    }
  }
  
  # Regression analysis
  if ("Program.Success" %in% names(data)) {
    formula <- as.formula(paste("Program.Success ~", 
                               paste(names(data)[sapply(data, is.numeric) & 
                                                 !names(data) %in% c("Program.Success", "ID")], 
                                     collapse = "+")))
    model <- lm(formula, data = data)
    results$regression <- tidy(model)
    results$regression_summary <- glance(model)
  }
  
  return(results)
}

# Function to create visualizations
create_visualizations <- function(data) {
  plots <- list()
  
  # Distribution of program outcomes
  if ("Program.Outcome" %in% names(data)) {
    plots$outcome_dist <- ggplot(data, aes(x = Program.Outcome, fill = Program.Outcome)) +
      geom_bar() +
      labs(title = "Distribution of Program Outcomes", 
           x = "Outcome", 
           y = "Count") +
      theme_minimal() +
      scale_fill_brewer(palette = "Set2")
  }
  
  # Pre-post comparison plot
  pre_post_cols <- names(data)[sapply(names(data), function(x) grepl("pre|post", x, ignore.case = TRUE))]
  
  if (length(pre_post_cols) > 0) {
    long_data <- data %>%
      pivot_longer(cols = all_of(pre_post_cols),
                   names_to = "Time.Period",
                   values_to = "Value")
    
    plots$pre_post <- ggplot(long_data, aes(x = Time.Period, y = Value, fill = Time.Period)) +
      geom_boxplot() +
      labs(title = "Pre and Post Program Comparison",
           x = "Time Period",
           y = "Value") +
      theme_minimal() +
      scale_fill_brewer(palette = "Pastel1")
  }
  
  # Age distribution of beneficiaries
  if ("Age" %in% names(data)) {
    plots$age_dist <- ggplot(data, aes(x = Age)) +
      geom_histogram(binwidth = 5, fill = "skyblue", color = "black") +
      labs(title = "Age Distribution of Beneficiaries",
           x = "Age",
           y = "Count") +
      theme_minimal()
  }
  
  # Program success by demographic factors
  if ("Program.Success" %in% names(data) && "Gender" %in% names(data)) {
    plots$success_by_gender <- ggplot(data, aes(x = Gender, y = Program.Success, fill = Gender)) +
      geom_boxplot() +
      labs(title = "Program Success by Gender",
           x = "Gender",
           y = "Success Score") +
      theme_minimal() +
      scale_fill_brewer(palette = "Accent")
  }
  
  return(plots)
}

# Main analysis function
analyze_program_impact <- function(file_path) {
  # Load and clean data
  data <- load_and_clean_data(file_path)
  
  # Perform statistical analysis
  analysis_results <- perform_statistical_analysis(data)
  
  # Create visualizations
  plots <- create_visualizations(data)
  
  # Return results
  return(list(
    data = data,
    analysis = analysis_results,
    plots = plots
  ))
}

# Example usage (commented out for production)
# results <- analyze_program_impact("path_to_your_data_file.xlsx")
# print(results$analysis$descriptive)
# print(results$analysis$correlation)
# print(results$analysis$t_tests)
# print(results$analysis$regression)

# Save plots to files
# for (plot_name in names(results$plots)) {
#   ggsave(paste0(plot_name, ".png"), plot = results$plots[[plot_name]], width = 8, height = 6)
# }

# Generate report (requires RMarkdown setup)
# render("program_impact_report.Rmd", output_file = "Program_Impact_Analysis.html")
```
