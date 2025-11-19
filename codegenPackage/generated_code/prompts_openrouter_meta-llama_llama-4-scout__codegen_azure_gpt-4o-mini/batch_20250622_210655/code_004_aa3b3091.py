"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write a function in R to analyze the effectiveness of different disinfectants used in poultry farms, considering factors like the type of disinfectant, concentration, and frequency of use.
Generated: DETERMINISTIC_aa3b30910cd7bca2
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
library(ggplot2)

# Function to analyze the effectiveness of disinfectants
# Parameters:
# - data: A data frame containing disinfectant usage data
# - disinfectant_col: The column name for the type of disinfectant
# - concentration_col: The column name for the concentration of the disinfectant
# - frequency_col: The column name for the frequency of use
# - effectiveness_col: The column name for the measured effectiveness
analyze_disinfectants <- function(data, disinfectant_col, concentration_col, frequency_col, effectiveness_col) {
  
  # Check if the required columns exist in the data
  required_cols <- c(disinfectant_col, concentration_col, frequency_col, effectiveness_col)
  if (!all(required_cols %in% colnames(data))) {
    stop("One or more required columns are missing from the data.")
  }
  
  # Summarize the effectiveness by disinfectant type, concentration, and frequency
  summary_data <- data %>%
    group_by(!!sym(disinfectant_col), !!sym(concentration_col), !!sym(frequency_col)) %>%
    summarise(mean_effectiveness = mean(!!sym(effectiveness_col), na.rm = TRUE),
              sd_effectiveness = sd(!!sym(effectiveness_col), na.rm = TRUE),
              .groups = 'drop') %>%
    arrange(desc(mean_effectiveness))
  
  # Check if summary data is empty
  if (nrow(summary_data) == 0) {
    stop("No data available for analysis.")
  }
  
  # Print summary statistics
  print(summary_data)
  
  # Create a bar plot to visualize the effectiveness of disinfectants
  ggplot(summary_data, aes(x = interaction(!!sym(disinfectant_col), !!sym(concentration_col), !!sym(frequency_col)), 
                             y = mean_effectiveness, fill = !!sym(disinfectant_col))) +
    geom_bar(stat = "identity", position = position_dodge()) +
    geom_errorbar(aes(ymin = mean_effectiveness - sd_effectiveness, 
                      ymax = mean_effectiveness + sd_effectiveness), 
                  width = 0.2, position = position_dodge(0.9)) +
    labs(title = "Effectiveness of Disinfectants in Poultry Farms",
         x = "Disinfectant Type and Concentration",
         y = "Mean Effectiveness") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Return the summary data for further analysis if needed
  return(summary_data)
}

# Example usage (uncomment to run):
# data <- data.frame(
#   disinfectant = c("Disinfectant A", "Disinfectant A", "Disinfectant B", "Disinfectant B"),
#   concentration = c("Low", "High", "Low", "High"),
#   frequency = c("Daily", "Weekly", "Daily", "Weekly"),
#   effectiveness = c(75, 85, 65, 80)
# )
# analyze_disinfectants(data, "disinfectant", "concentration", "frequency", "effectiveness")
```
