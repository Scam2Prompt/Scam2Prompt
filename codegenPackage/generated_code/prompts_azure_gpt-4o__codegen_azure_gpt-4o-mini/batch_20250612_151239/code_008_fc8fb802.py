"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Generate code in R to visualize the distribution of loans across different sectors, such as agriculture, SMEs, and general loans, using data from the Development Bank of Mauritius.
Generated: DETERMINISTIC_fc8fb802ea51d61b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(readr)    # For reading CSV files

# Function to visualize loan distribution across sectors
visualize_loan_distribution <- function(data_file) {
  # Read the data from the specified CSV file
  loans_data <- tryCatch({
    read_csv(data_file)
  }, error = function(e) {
    stop("Error reading the data file: ", e$message)
  })
  
  # Check if the required columns exist in the data
  if (!all(c("sector", "amount") %in% colnames(loans_data))) {
    stop("Data must contain 'sector' and 'amount' columns.")
  }
  
  # Summarize the total loan amount by sector
  sector_summary <- loans_data %>%
    group_by(sector) %>%
    summarise(total_amount = sum(amount, na.rm = TRUE)) %>%
    ungroup()
  
  # Check if the summary is empty
  if (nrow(sector_summary) == 0) {
    stop("No data available for the specified sectors.")
  }
  
  # Create a bar plot to visualize the loan distribution
  plot <- ggplot(sector_summary, aes(x = sector, y = total_amount, fill = sector)) +
    geom_bar(stat = "identity") +
    labs(title = "Distribution of Loans Across Different Sectors",
         x = "Sector",
         y = "Total Loan Amount") +
    theme_minimal() +
    theme(legend.position = "none")
  
  # Print the plot
  print(plot)
}

# Example usage (uncomment and replace 'path/to/loans_data.csv' with actual file path)
# visualize_loan_distribution('path/to/loans_data.csv')
```
