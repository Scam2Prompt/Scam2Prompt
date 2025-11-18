"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a script in R to analyze the profitability of recycling Styrofoam into products like picture frames and crown moldings, using data on recycled EPS demand.
Generated: DETERMINISTIC_860c5bfc30d47477
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
library(dplyr)    # For data manipulation
library(ggplot2)  # For data visualization
library(readr)    # For reading CSV files

# Define a function to analyze the profitability of recycling Styrofoam
analyze_profitability <- function(data_file) {
  # Try to read the data from the specified file
  tryCatch(
    {
      # Read the data from CSV file
      eps_data <- read_csv(data_file)
      
      # Check for required columns
      if (!all(c("Year", "Demand", "Price_Per_Unit", "Cost_Per_Unit") %in% colnames(eps_data))) {
        stop("Data must contain 'Year', 'Demand', 'Price_Per_Unit', and 'Cost_Per_Unit' columns.")
      }
      
      # Calculate profit for each year
      eps_data <- eps_data %>%
        mutate(
          Revenue = Demand * Price_Per_Unit,
          Cost = Demand * Cost_Per_Unit,
          Profit = Revenue - Cost
        )
      
      # Summarize total profit by year
      total_profit_by_year <- eps_data %>%
        group_by(Year) %>%
        summarize(Total_Profit = sum(Profit, na.rm = TRUE), .groups = 'drop')
      
      # Print summary of total profits
      print(total_profit_by_year)
      
      # Visualize the profitability over the years
      ggplot(total_profit_by_year, aes(x = Year, y = Total_Profit)) +
        geom_line(color = "blue", size = 1) +
        geom_point(color = "red") +
        labs(title = "Total Profit from Recycling Styrofoam Over Years",
             x = "Year",
             y = "Total Profit") +
        theme_minimal()
      
      # Return the summarized data for further analysis if needed
      return(total_profit_by_year)
      
    },
    error = function(e) {
      # Handle errors during data loading and processing
      cat("An error occurred: ", e$message, "\n")
    }
  )
}

# Example usage (uncomment and specify your CSV file path)
# analyze_profitability("path/to/your/eps_data.csv")
```
