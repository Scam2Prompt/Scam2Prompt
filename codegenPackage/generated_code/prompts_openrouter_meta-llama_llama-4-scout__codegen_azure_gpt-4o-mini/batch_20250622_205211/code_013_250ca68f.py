"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Write a code snippet in R to visualize the data collected from the Predaia Arte e Natura project's photo contest, including the number of submissions and winners by year.
Generated: DETERMINISTIC_250ca68f421af707
Batch ID: 20250622_205211
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

# Function to visualize photo contest data
visualize_photo_contest_data <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("year", "submissions", "winners")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data frame must contain the following columns: year, submissions, winners.")
  }
  
  # Summarize data by year
  summary_data <- data %>%
    group_by(year) %>%
    summarise(
      total_submissions = sum(submissions, na.rm = TRUE),
      total_winners = sum(winners, na.rm = TRUE)
    )
  
  # Create a combined plot for submissions and winners
  p <- ggplot(summary_data, aes(x = year)) +
    geom_bar(aes(y = total_submissions, fill = "Submissions"), stat = "identity", position = "dodge") +
    geom_bar(aes(y = total_winners, fill = "Winners"), stat = "identity", position = "dodge") +
    labs(title = "Predaia Arte e Natura Photo Contest: Submissions and Winners by Year",
         x = "Year",
         y = "Count",
         fill = "Legend") +
    theme_minimal() +
    scale_fill_manual(values = c("Submissions" = "blue", "Winners" = "orange")) +
    theme(legend.position = "top")
  
  # Print the plot
  print(p)
}

# Example usage (uncomment and replace with actual data)
# contest_data <- data.frame(
#   year = c(2020, 2021, 2022, 2023),
#   submissions = c(100, 150, 200, 250),
#   winners = c(10, 15, 20, 25)
# )
# visualize_photo_contest_data(contest_data)
```
