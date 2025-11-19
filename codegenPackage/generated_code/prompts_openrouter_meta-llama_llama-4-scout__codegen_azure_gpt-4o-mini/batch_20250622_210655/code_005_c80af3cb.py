"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write a function in R to analyze customer reviews and ratings for Chile Horse Riding's tours, such as the Rari Day Ride and Laguna Ride.
Generated: DETERMINISTIC_c80af3cb4ad63d1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)
library(tidyr)
library(ggplot2)
library(stringr)

# Function to analyze customer reviews and ratings for Chile Horse Riding's tours
analyze_reviews <- function(reviews_data) {
  # Check if the input is a data frame
  if (!is.data.frame(reviews_data)) {
    stop("Input must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("tour_name", "rating", "review")
  missing_columns <- setdiff(required_columns, colnames(reviews_data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Clean and preprocess the data
  reviews_data <- reviews_data %>%
    mutate(tour_name = str_to_title(tour_name),  # Standardize tour names
           rating = as.numeric(rating)) %>%      # Ensure ratings are numeric
    filter(!is.na(rating), !is.na(review))      # Remove NA values
  
  # Summary statistics for ratings
  rating_summary <- reviews_data %>%
    group_by(tour_name) %>%
    summarise(
      average_rating = mean(rating, na.rm = TRUE),
      total_reviews = n(),
      .groups = 'drop'
    )
  
  # Print summary statistics
  print(rating_summary)
  
  # Visualize the average ratings
  ggplot(rating_summary, aes(x = reorder(tour_name, -average_rating), y = average_rating)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Average Ratings for Chile Horse Riding Tours",
         x = "Tour Name",
         y = "Average Rating") +
    theme_minimal() +
    coord_flip()  # Flip coordinates for better readability
  
  # Return the summary data frame
  return(rating_summary)
}

# Example usage (uncomment to run):
# reviews <- data.frame(
#   tour_name = c("Rari Day Ride", "Laguna Ride", "Rari Day Ride", "Laguna Ride"),
#   rating = c(5, 4, 4, 5),
#   review = c("Amazing experience!", "Beautiful scenery.", "Loved the horses!", "Great guides!")
# )
# analyze_reviews(reviews)
```
