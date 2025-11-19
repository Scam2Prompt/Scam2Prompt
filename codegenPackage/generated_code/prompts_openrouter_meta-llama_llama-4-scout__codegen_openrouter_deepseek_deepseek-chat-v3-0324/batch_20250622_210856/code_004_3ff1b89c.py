"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Create a data analysis script in R to process and visualize data from the "Powszechny spis rolny 2020" (2020 Agricultural Census) and "Powszechny spis Ludności i Mieszkań 2021" (2021 Population and Housing Census) as presented on the Gmina Dębnica Kaszubska website.
Generated: DETERMINISTIC_3ff1b89c71267fa7
Batch ID: 20250622_210856
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
library(ggplot2)
library(scales)
library(janitor)

# Function to clean and process census data
process_census_data <- function(file_path, sheet_name, skip_rows = 0) {
  tryCatch({
    # Read data from Excel file
    data <- read_excel(file_path, sheet = sheet_name, skip = skip_rows) %>%
      clean_names() %>%
      remove_empty(c("rows", "cols")) %>%
      mutate(across(where(is.character), str_trim))
    
    # Convert numeric columns
    numeric_cols <- names(data)[sapply(data, function(x) all(grepl("^\\d+$", x) | is.na(x)))]
    data <- data %>%
      mutate(across(all_of(numeric_cols), as.numeric))
    
    return(data)
  }, error = function(e) {
    message("Error processing file: ", file_path)
    message("Error message: ", e$message)
    return(NULL)
  })
}

# Function to visualize agricultural data
visualize_agricultural_data <- function(data) {
  if (is.null(data)) return(NULL)
  
  tryCatch({
    # Example visualization - adjust based on actual data structure
    plot <- data %>%
      select(contains("area") | contains("production")) %>%
      pivot_longer(cols = everything(), names_to = "category", values_to = "value") %>%
      ggplot(aes(x = reorder(category, -value), y = value, fill = category)) +
      geom_col() +
      labs(title = "Agricultural Production by Category",
           x = "Category",
           y = "Value") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1),
            legend.position = "none")
    
    return(plot)
  }, error = function(e) {
    message("Error creating agricultural visualization")
    message("Error message: ", e$message)
    return(NULL)
  })
}

# Function to visualize population data
visualize_population_data <- function(data) {
  if (is.null(data)) return(NULL)
  
  tryCatch({
    # Example visualization - adjust based on actual data structure
    plot <- data %>%
      select(contains("population") | contains("household")) %>%
      pivot_longer(cols = everything(), names_to = "category", values_to = "value") %>%
      ggplot(aes(x = reorder(category, -value), y = value, fill = category)) +
      geom_col() +
      labs(title = "Population and Housing Statistics",
           x = "Category",
           y = "Value") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1),
            legend.position = "none")
    
    return(plot)
  }, error = function(e) {
    message("Error creating population visualization")
    message("Error message: ", e$message)
    return(NULL)
  })
}

# Main analysis function
analyze_census_data <- function(agricultural_file = NULL, population_file = NULL) {
  # Process agricultural data if file provided
  if (!is.null(agricultural_file)) {
    agri_data <- process_census_data(agricultural_file, "Sheet1")
    agri_plot <- visualize_agricultural_data(agri_data)
    if (!is.null(agri_plot)) print(agri_plot)
  }
  
  # Process population data if file provided
  if (!is.null(population_file)) {
    pop_data <- process_census_data(population_file, "Sheet1")
    pop_plot <- visualize_population_data(pop_data)
    if (!is.null(pop_plot)) print(pop_plot)
  }
  
  # Return combined results
  return(list(
    agricultural_data = if(exists("agri_data")) agri_data else NULL,
    population_data = if(exists("pop_data")) pop_data else NULL
  ))
}

# Example usage (uncomment and replace paths with actual file paths)
# results <- analyze_census_data(
#   agricultural_file = "path/to/agricultural_census.xlsx",
#   population_file = "path/to/population_census.xlsx"
# )
```
