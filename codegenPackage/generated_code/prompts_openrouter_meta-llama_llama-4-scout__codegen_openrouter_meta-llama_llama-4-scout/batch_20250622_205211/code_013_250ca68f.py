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
# Import necessary libraries
library(ggplot2)
library(dplyr)

# Sample data (replace with actual data from Predaia Arte e Natura project)
photo_contest_data <- data.frame(
  year = c(2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020),
  submission_type = c("submission", "submission", "winner", "submission", "submission", "winner", "submission", "submission", "winner"),
  id = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
)

# Function to visualize photo contest data
visualize_photo_contest_data <- function(data) {
  # Count submissions and winners by year
  yearly_submissions <- data %>%
    group_by(year, submission_type) %>%
    summarise(count = n())

  # Separate submissions and winners for clearer visualization
  submissions <- yearly_submissions %>% 
    filter(submission_type == "submission")
  winners <- yearly_submissions %>% 
    filter(submission_type == "winner")

  # Create a line plot for submissions and a bar plot for winners
  ggplot(submissions, aes(x = year, y = count)) +
    geom_line(color = "blue") +
    labs(title = "Number of Submissions by Year", x = "Year", y = "Number of Submissions") +
    theme_classic()

  ggplot(winners, aes(x = year, y = count)) +
    geom_bar(stat = "identity", color = "red", fill = "lightblue") +
    labs(title = "Number of Winners by Year", x = "Year", y = "Number of Winners") +
    theme_classic()

  # Combine plots for a single figure (optional)
  # library(cowplot)
  # plot_grid <- plot_grid(submissions_plot, winners_plot, nrow = 2)
  # print(plot_grid)
}

# Call the function with sample data
visualize_photo_contest_data(photo_contest_data)
```
