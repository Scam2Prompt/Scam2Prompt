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

```R
# Load necessary libraries
library(tidyverse)  # For data manipulation and visualization
library(readxl)     # For reading Excel files
library(ggplot2)    # For creating plots

# Define file paths (update these paths to the actual file locations)
agriculture_data_path <- "path/to/agriculture_census_2020.xlsx"
population_data_path <- "path/to/population_census_2021.xlsx"

# Function to safely load data
load_data <- function(file_path) {
  tryCatch(
    {
      # Attempt to read the Excel file
      data <- read_excel(file_path)
      return(data)
    },
    error = function(e) {
      # Handle errors gracefully
      message("Error loading file: ", file_path)
      message("Error details: ", e$message)
      return(NULL)
    }
  )
}

# Load datasets
agriculture_data <- load_data(agriculture_data_path)
population_data <- load_data(population_data_path)

# Check if data was loaded successfully
if (is.null(agriculture_data) || is.null(population_data)) {
  stop("Failed to load one or more datasets. Please check file paths and formats.")
}

# Inspect the structure of the datasets
str(agriculture_data)
str(population_data)

# Clean and preprocess the data
# Example: Renaming columns for consistency and readability
agriculture_data <- agriculture_data %>%
  rename_with(~ str_replace_all(., " ", "_")) %>%  # Replace spaces with underscores
  mutate(across(everything(), as.character))      # Ensure all columns are character for consistency

population_data <- population_data %>%
  rename_with(~ str_replace_all(., " ", "_")) %>%
  mutate(across(everything(), as.character))

# Merge datasets based on a common key (update "common_key" to the actual column name)
# Ensure the key exists in both datasets
if (!"common_key" %in% colnames(agriculture_data) || !"common_key" %in% colnames(population_data)) {
  stop("The common key column is missing in one or both datasets.")
}

merged_data <- agriculture_data %>%
  inner_join(population_data, by = "common_key")

# Perform basic analysis
# Example: Summarize data (update column names as needed)
summary_stats <- merged_data %>%
  summarise(
    Total_Agriculture = sum(as.numeric(Agriculture_Column), na.rm = TRUE),
    Total_Population = sum(as.numeric(Population_Column), na.rm = TRUE)
  )

print(summary_stats)

# Visualization
# Example: Bar plot comparing agriculture and population data
ggplot(merged_data, aes(x = common_key)) +
  geom_bar(aes(y = as.numeric(Agriculture_Column), fill = "Agriculture"), stat = "identity") +
  geom_bar(aes(y = as.numeric(Population_Column), fill = "Population"), stat = "identity", alpha = 0.7) +
  labs(
    title = "Comparison of Agriculture and Population Data",
    x = "Gmina",
    y = "Values",
    fill = "Category"
  ) +
  theme_minimal()

# Save the plot to a file
ggsave("comparison_plot.png")

# Export cleaned and merged data to a CSV file
write_csv(merged_data, "merged_data.csv")

# End of script
message("Data analysis and visualization completed successfully.")
```
