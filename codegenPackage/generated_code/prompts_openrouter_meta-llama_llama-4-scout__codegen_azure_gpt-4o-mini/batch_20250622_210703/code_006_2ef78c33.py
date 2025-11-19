"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Write a code snippet in R to visualize the growth of PSHP membership over the years.
Generated: DETERMINISTIC_2ef78c334eddcc40
Batch ID: 20250622_210703
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

# Function to visualize PSHP membership growth
visualize_membership_growth <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check for required columns
  if (!all(c("Year", "Membership") %in% colnames(data))) {
    stop("Data frame must contain 'Year' and 'Membership' columns.")
  }
  
  # Summarize data to ensure it is in the correct format
  membership_summary <- data %>%
    group_by(Year) %>%
    summarize(Total_Membership = sum(Membership, na.rm = TRUE), .groups = 'drop')
  
  # Create the plot
  membership_plot <- ggplot(membership_summary, aes(x = Year, y = Total_Membership)) +
    geom_line(color = "blue", size = 1) +  # Line for membership growth
    geom_point(color = "red", size = 2) +  # Points for each year
    labs(title = "Growth of PSHP Membership Over the Years",
         x = "Year",
         y = "Total Membership") +
    theme_minimal() +  # Clean theme
    theme(plot.title = element_text(hjust = 0.5))  # Center title
  
  # Print the plot
  print(membership_plot)
}

# Example usage (uncomment to run):
# data <- data.frame(Year = c(2018, 2019, 2020, 2021, 2022),
#                    Membership = c(100, 150, 200, 250, 300))
# visualize_membership_growth(data)
```
