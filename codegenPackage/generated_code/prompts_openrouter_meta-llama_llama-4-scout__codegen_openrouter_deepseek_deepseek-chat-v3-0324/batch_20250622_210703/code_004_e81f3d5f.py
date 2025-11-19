"""
Generated Code Metadata:
========================
Original URL: https://balletcristinavaz.com.br
Prompt: Write a script in R to analyze the relationship between the number of years a dance school has been in operation and its number of awards, using data from Ballet Cristina Vaz's 100+ national and international awards.
Generated: DETERMINISTIC_e81f3d5f59d18f66
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(readr)
library(stats)

# Function to load and preprocess data
load_dance_school_data <- function(file_path) {
  tryCatch({
    # Read data from CSV file
    data <- read_csv(file_path, col_types = cols(
      year_founded = col_integer(),
      awards_count = col_integer()
    ))
    
    # Calculate years in operation
    current_year <- as.integer(format(Sys.Date(), "%Y"))
    data <- data %>%
      mutate(years_in_operation = current_year - year_founded) %>%
      filter(years_in_operation > 0)  # Remove schools not yet operational
    
    return(data)
  }, error = function(e) {
    stop(paste("Error loading data:", e$message))
  })
}

# Function to analyze relationship between years in operation and awards
analyze_awards_relationship <- function(data) {
  tryCatch({
    # Check if data is valid
    if (nrow(data) == 0) {
      stop("No valid data to analyze")
    }
    
    # Basic statistics
    stats <- data %>%
      summarise(
        mean_years = mean(years_in_operation),
        mean_awards = mean(awards_count),
        correlation = cor(years_in_operation, awards_count)
      )
    
    # Linear regression model
    model <- lm(awards_count ~ years_in_operation, data = data)
    model_summary <- summary(model)
    
    # Visualization
    plot <- ggplot(data, aes(x = years_in_operation, y = awards_count)) +
      geom_point(color = "steelblue", size = 3) +
      geom_smooth(method = "lm", color = "darkred", se = FALSE) +
      labs(
        title = "Relationship Between Years in Operation and Awards",
        x = "Years in Operation",
        y = "Number of Awards"
      ) +
      theme_minimal()
    
    return(list(
      statistics = stats,
      model_summary = model_summary,
      plot = plot
    ))
  }, error = function(e) {
    stop(paste("Error in analysis:", e$message))
  })
}

# Main execution function
main <- function() {
  tryCatch({
    # File path to the dance school data (replace with actual path)
    file_path <- "ballet_cristina_vaz_awards.csv"
    
    # Load and preprocess data
    dance_data <- load_dance_school_data(file_path)
    
    # Perform analysis
    analysis_results <- analyze_awards_relationship(dance_data)
    
    # Print results
    print("Summary Statistics:")
    print(analysis_results$statistics)
    
    print("\nRegression Model Summary:")
    print(analysis_results$model_summary)
    
    # Display plot
    print(analysis_results$plot)
    
  }, error = function(e) {
    message("Error: ", e$message)
  })
}

# Execute the analysis
main()
```
