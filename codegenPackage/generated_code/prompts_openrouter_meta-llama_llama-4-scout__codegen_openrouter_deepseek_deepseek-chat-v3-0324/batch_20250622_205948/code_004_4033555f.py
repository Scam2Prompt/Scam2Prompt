"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Write a code snippet in R to visualize the economic activities of rural villages in Serbia, using data on forestry and agriculture, similar to those in Krajkovac.
Generated: DETERMINISTIC_4033555f785dbe88
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(readxl)

# Function to load and preprocess data
load_village_data <- function(file_path) {
  tryCatch({
    # Read data from Excel file (assuming data is in this format)
    data <- read_excel(file_path)
    
    # Basic data validation
    if (!all(c("village", "activity", "value", "year") %in% colnames(data))) {
      stop("Input data does not contain required columns: village, activity, value, year")
    }
    
    # Clean and transform data
    data <- data %>%
      mutate(
        value = as.numeric(value),
        year = as.factor(year),
        activity = tolower(activity)
      ) %>%
      filter(!is.na(value))
    
    return(data)
  }, error = function(e) {
    message("Error loading data: ", e$message)
    return(NULL)
  })
}

# Function to visualize economic activities
visualize_activities <- function(data, village_name = "Krajkovac") {
  if (is.null(data)) {
    stop("No valid data provided for visualization")
  }
  
  tryCatch({
    # Filter data for specific village if provided
    if (!is.null(village_name)) {
      data <- data %>% filter(tolower(village) == tolower(village_name))
    }
    
    # Create visualization
    p <- ggplot(data, aes(x = year, y = value, fill = activity)) +
      geom_bar(stat = "identity", position = "dodge") +
      labs(
        title = paste("Economic Activities in", ifelse(is.null(village_name), "Rural Villages", village_name)),
        x = "Year",
        y = "Economic Value",
        fill = "Activity Type"
      ) +
      theme_minimal() +
      theme(
        plot.title = element_text(hjust = 0.5, face = "bold"),
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position = "bottom"
      ) +
      scale_fill_brewer(palette = "Set3")
    
    return(p)
  }, error = function(e) {
    message("Error creating visualization: ", e$message)
    return(NULL)
  })
}

# Example usage (commented out for production)
# data <- load_village_data("path_to_your_data_file.xlsx")
# if (!is.null(data)) {
#   p <- visualize_activities(data, "Krajkovac")
#   if (!is.null(p)) {
#     print(p)
#     # Save plot
#     ggsave("village_economic_activities.png", plot = p, width = 10, height = 6, dpi = 300)
#   }
# }
```
