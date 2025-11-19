"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Write a code snippet in R to analyze the benefits and premium rates of Aflac's Life Insurance policy (B60000 Series) in Arkansas, using statistical models to visualize the data.
Generated: DETERMINISTIC_29ca1f7bfb02f2a6
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(readxl)
library(scales)

# Function to load and clean Aflac life insurance data
load_aflac_data <- function(file_path) {
  tryCatch({
    # Read Excel file
    data <- read_excel(file_path)
    
    # Clean column names
    names(data) <- tolower(names(data))
    names(data) <- gsub(" ", "_", names(data))
    
    # Filter for Arkansas and B60000 series
    data <- data %>%
      filter(state == "Arkansas", 
             grepl("B60000", policy_series, ignore.case = TRUE))
    
    # Convert premium to numeric if needed
    if (!is.numeric(data$premium)) {
      data$premium <- as.numeric(gsub("[\\$,]", "", data$premium))
    }
    
    # Convert benefit to numeric if needed
    if (!is.numeric(data$benefit)) {
      data$benefit <- as.numeric(gsub("[\\$,]", "", data$benefit))
    }
    
    return(data)
  }, error = function(e) {
    message("Error loading data: ", e$message)
    return(NULL)
  })
}

# Function to analyze premium vs benefit relationship
analyze_premium_benefit <- function(data) {
  if (is.null(data)) {
    stop("No valid data provided for analysis")
  }
  
  tryCatch({
    # Linear model
    model <- lm(premium ~ benefit + age + gender, data = data)
    print(summary(model))
    
    # Visualization
    p <- ggplot(data, aes(x = benefit, y = premium, color = age)) +
      geom_point() +
      geom_smooth(method = "lm", se = FALSE) +
      scale_x_continuous(labels = dollar) +
      scale_y_continuous(labels = dollar) +
      labs(title = "Aflac B60000 Series: Premium vs Benefit in Arkansas",
           x = "Benefit Amount ($)",
           y = "Premium ($)",
           color = "Age") +
      theme_minimal()
    
    print(p)
    
    return(model)
  }, error = function(e) {
    message("Analysis error: ", e$message)
    return(NULL)
  })
}

# Function to visualize age distribution of premiums
visualize_age_premium <- function(data) {
  if (is.null(data)) {
    stop("No valid data provided for visualization")
  }
  
  tryCatch({
    p <- ggplot(data, aes(x = age, y = premium, fill = gender)) +
      geom_boxplot() +
      scale_y_continuous(labels = dollar) +
      labs(title = "Aflac B60000 Series: Premium by Age in Arkansas",
           x = "Age",
           y = "Premium ($)",
           fill = "Gender") +
      theme_minimal()
    
    print(p)
  }, error = function(e) {
    message("Visualization error: ", e$message)
  })
}

# Main execution
file_path <- "aflac_life_insurance_data.xlsx"  # Update with actual file path
aflac_data <- load_aflac_data(file_path)

if (!is.null(aflac_data)) {
  model <- analyze_premium_benefit(aflac_data)
  visualize_age_premium(aflac_data)
}
```
