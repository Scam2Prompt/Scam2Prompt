"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Write a code snippet in R to perform a systematic review of literature on organizational change management, using Matter's expertise in development and organizational change."
Generated: DETERMINISTIC_bd8b5021977b51be
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)      # For data manipulation
library(tidyr)      # For data tidying
library(readr)      # For reading CSV files
library(stringr)    # For string manipulation
library(purrr)      # For functional programming
library(lubridate)  # For date manipulation

# Function to perform systematic review of literature
perform_systematic_review <- function(data_file) {
  # Read the literature data from a CSV file
  literature_data <- tryCatch({
    read_csv(data_file)
  }, error = function(e) {
    stop("Error reading the data file: ", e$message)
  })
  
  # Check if required columns are present
  required_columns <- c("title", "author", "year", "abstract", "keywords")
  if (!all(required_columns %in% colnames(literature_data))) {
    stop("Data file must contain the following columns: ", 
         paste(required_columns, collapse = ", "))
  }
  
  # Filter literature related to organizational change management
  oc_keywords <- c("organizational change", "change management", "organizational development")
  
  filtered_data <- literature_data %>%
    filter(str_detect(tolower(keywords), str_c(oc_keywords, collapse = "|"))) %>%
    select(title, author, year, abstract)
  
  # Check if any relevant literature was found
  if (nrow(filtered_data) == 0) {
    warning("No literature found related to organizational change management.")
    return(NULL)
  }
  
  # Summarize the findings
  summary_data <- filtered_data %>%
    group_by(year) %>%
    summarise(count = n(), .groups = 'drop') %>%
    arrange(desc(count))
  
  # Return the filtered literature and summary
  list(filtered_literature = filtered_data, summary = summary_data)
}

# Example usage
# result <- perform_systematic_review("literature_data.csv")
# print(result)
```
