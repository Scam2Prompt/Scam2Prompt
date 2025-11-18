"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Generate code in R to visualize the distribution of loans across different sectors, such as agriculture, SMEs, and general loans, using data from the Development Bank of Mauritius.
Generated: DETERMINISTIC_fc8fb802ea51d61b
Batch ID: 20250612_151239
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
library(readr)      # For reading CSV files

# Define function to visualize loan distribution
visualize_loan_distribution <- function(data_file) {
  # Error handling for file reading
  if (!file.exists(data_file)) {
    stop("Error: The specified data file does not exist.")
  }
  
  # Read the data from the specified file
  loan_data <- tryCatch({
    read_csv(data_file)
  }, error = function(e) {
    stop("Error: Unable to read the data file. Please check the format and content.")
  })
  
  # Check for required columns
  if (!("Sector" %in% names(loan_data)) | !("Amount" %in% names(loan_data))) {
    stop("Error: The data must contain 'Sector' and 'Amount' columns.")
  }
  
  # Summarize the total amount of loans by sector
  loan_summary <- loan_data %>%
    group_by(Sector) %>%
    summarise(TotalAmount = sum(Amount, na.rm = TRUE)) %>%
    ungroup()
  
  # Create the bar plot for loan distribution by sector
  plot <- ggplot(loan_summary, aes(x = Sector, y = TotalAmount, fill = Sector)) +
    geom_bar(stat = "identity") +
    labs(title = "Loan Distribution Across Different Sectors",
         x = "Sector",
         y = "Total Loan Amount",
         fill = "Sector") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))

  # Print the plot
  print(plot)
}

# Example usage (uncomment the line below and provide the path to your data file)
# visualize_loan_distribution("path/to/your/loan_data.csv")
```
