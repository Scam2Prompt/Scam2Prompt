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
library(ggplot2)
library(dplyr)

# Sample data for PSHP membership growth
pshp_membership_data <- data.frame(
  Year = c(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020),
  Membership = c(1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200, 3500)
)

# Function to visualize PSHP membership growth
visualize_membership_growth <- function(data) {
  # Check if data is not empty
  if (nrow(data) == 0) {
    stop("No data available for visualization.")
  }
  
  # Validate required columns
  required_columns <- c("Year", "Membership")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain 'Year' and 'Membership' columns.")
  }
  
  # Create line plot
  ggplot(data, aes(x = Year, y = Membership)) +
    geom_line(color = "blue") +
    geom_point(color = "red") +
    labs(title = "PSHP Membership Growth Over the Years",
         subtitle = "Line Plot of Membership Growth",
         x = "Year",
         y = "Membership Count") +
    theme_classic()
}

# Example usage
tryCatch(
  expr = {
    visualize_membership_growth(pshp_membership_data) +
      theme(legend.position = "none")
  },
  error = function(e) {
    print(paste("An error occurred: ", e$message))
  }
)
```
