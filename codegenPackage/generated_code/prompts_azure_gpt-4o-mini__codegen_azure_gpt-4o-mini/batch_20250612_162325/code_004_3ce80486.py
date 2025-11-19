"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Construct a data visualization in R that illustrates the findings from FESIT's academic conferences on taxpayer rights in Chile.
Generated: DETERMINISTIC_3ce804860702bf42
Batch ID: 20250612_162325
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
library(readr)    # For reading data

# Function to load and preprocess data
load_and_preprocess_data <- function(file_path) {
  # Attempt to read the CSV file
  data <- tryCatch({
    read_csv(file_path)
  }, error = function(e) {
    stop("Error reading the data file: ", e$message)
  })
  
  # Check for necessary columns
  required_columns <- c("Year", "Conference", "Participants", "Topics")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain the following columns: ", paste(required_columns, collapse = ", "))
  }
  
  # Return the preprocessed data
  return(data)
}

# Function to create a bar plot of conference participation by year
create_participation_plot <- function(data) {
  # Summarize data by year
  summary_data <- data %>%
    group_by(Year) %>%
    summarise(Total_Participants = sum(Participants, na.rm = TRUE)) %>%
    ungroup()
  
  # Create the bar plot
  plot <- ggplot(summary_data, aes(x = Year, y = Total_Participants)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Total Participants in FESIT Academic Conferences on Taxpayer Rights in Chile",
         x = "Year",
         y = "Total Participants") +
    theme_minimal() +
    theme(text = element_text(size = 12))
  
  # Return the plot
  return(plot)
}

# Main function to execute the data visualization
main <- function() {
  # Define the path to the data file
  data_file_path <- "path/to/your/data.csv"  # Update this path accordingly
  
  # Load and preprocess the data
  conference_data <- load_and_preprocess_data(data_file_path)
  
  # Create the participation plot
  participation_plot <- create_participation_plot(conference_data)
  
  # Print the plot
  print(participation_plot)
}

# Run the main function
main()
```
