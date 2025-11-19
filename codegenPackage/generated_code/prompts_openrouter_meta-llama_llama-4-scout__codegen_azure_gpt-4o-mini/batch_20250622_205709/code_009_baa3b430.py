"""
Generated Code Metadata:
========================
Original URL: https://getarcadeapp.pages.dev
Prompt: "Create a data visualization code snippet in R to represent the distribution of APRs among active loans on the Arcade platform."
Generated: DETERMINISTIC_baa3b43008f1c067
Batch ID: 20250622_205709
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

# Function to visualize the distribution of APRs among active loans
visualize_apr_distribution <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check if the required column 'APR' exists in the data
  if (!"APR" %in% colnames(data)) {
    stop("Data frame must contain an 'APR' column.")
  }
  
  # Filter for active loans (assuming 'status' column indicates loan status)
  active_loans <- data %>%
    filter(status == "active")
  
  # Check if there are any active loans
  if (nrow(active_loans) == 0) {
    stop("No active loans found in the data.")
  }
  
  # Create the histogram to visualize the distribution of APRs
  apr_plot <- ggplot(active_loans, aes(x = APR)) +
    geom_histogram(binwidth = 0.5, fill = "blue", color = "black", alpha = 0.7) +
    labs(title = "Distribution of APRs Among Active Loans",
         x = "Annual Percentage Rate (APR)",
         y = "Number of Loans") +
    theme_minimal() +
    theme(text = element_text(size = 12))
  
  # Print the plot
  print(apr_plot)
}

# Example usage (uncomment and replace 'your_data_frame' with actual data)
# your_data_frame <- read.csv("path_to_your_data.csv")  # Load your data
# visualize_apr_distribution(your_data_frame)  # Call the function to visualize APR distribution
```
