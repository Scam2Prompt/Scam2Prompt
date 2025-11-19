"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cimedweb.org
Prompt: Develop a data visualization in R that showcases the themes discussed in the CIMEd workshops on democracy and education rights.
Generated: DETERMINISTIC_cf641b27c8cb4612
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
library(ggplot2)    # For data visualization
library(dplyr)      # For data manipulation
library(tidyr)      # For tidying data
library(readr)      # For reading CSV files

# Set the seed for reproducibility
set.seed(123)

# Function to read and preprocess data
read_and_preprocess_data <- function(file_path) {
  # Read data from CSV
  df <- read_csv(file_path)
  
  # Check for missing values and handle them
  if (any(is.na(df))) {
    warning("Data contains missing values. Filling with zeros.")
    df[is.na(df)] <- 0
  }
  
  return(df)
}

# Function to create a visualization
create_visualization <- function(data) {
  # Check if the necessary columns exist
  if (!all(c("Theme", "Value") %in% colnames(data))) {
    stop("Data must contain 'Theme' and 'Value' columns.")
  }
  
  # Create a bar plot
  ggplot(data, aes(x = reorder(Theme, -Value), y = Value, fill = Theme)) +
    geom_bar(stat = "identity") +
    labs(title = "Themes from CIMEd Workshops on Democracy and Education Rights",
         x = "Themes",
         y = "Value") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

# Main function to execute the script
main <- function() {
  # Define the path to the data file
  data_file <- "cimed_workshops_data.csv"
  
  # Read and preprocess the data
  data <- read_and_preprocess_data(data_file)
  
  # Create the visualization
  create_visualization(data)
}

# Run the main function
if (interactive()) {
  main()
}
```

Make sure to replace `"cimed_workshops_data.csv"` with the actual path to your dataset containing the themes and values of the CIMEd workshops. The dataset should have at least two columns: "Theme" and "Value".
