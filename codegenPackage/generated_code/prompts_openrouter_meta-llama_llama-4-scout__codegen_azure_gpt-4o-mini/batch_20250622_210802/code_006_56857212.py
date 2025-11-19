"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Write a code snippet in R to analyze student satisfaction ratings for Global Healthcare Management College, using sample testimonials from the website.
Generated: DETERMINISTIC_56857212fc31b244
Batch ID: 20250622_210802
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
library(ggplot2)

# Sample data: Student satisfaction ratings and testimonials
# This data frame simulates testimonials with ratings and comments
student_data <- data.frame(
  student_id = 1:10,
  rating = c(5, 4, 3, 4, 5, 2, 4, 5, 3, 4),
  testimonial = c(
    "Excellent program with great faculty!",
    "Very good experience, learned a lot.",
    "Average, could be better.",
    "Good course structure and support.",
    "Outstanding education and networking opportunities.",
    "Not satisfied, needs improvement.",
    "Great learning environment.",
    "Loved the hands-on approach!",
    "Decent, but some courses were lacking.",
    "Overall a good experience."
  )
)

# Function to analyze student satisfaction ratings
analyze_student_satisfaction <- function(data) {
  # Check if the data frame is valid
  if (!is.data.frame(data) || ncol(data) < 2) {
    stop("Invalid data: Please provide a data frame with at least two columns (rating and testimonial).")
  }
  
  # Summarize the ratings
  summary_stats <- data %>%
    summarise(
      mean_rating = mean(rating),
      median_rating = median(rating),
      sd_rating = sd(rating),
      count = n()
    )
  
  # Print summary statistics
  print("Summary Statistics:")
  print(summary_stats)
  
  # Create a bar plot of ratings
  ggplot(data, aes(x = factor(rating))) +
    geom_bar(fill = "skyblue") +
    labs(title = "Student Satisfaction Ratings",
         x = "Rating (1-5)",
         y = "Number of Students") +
    theme_minimal()
}

# Run the analysis function with the sample data
analyze_student_satisfaction(student_data)
```
