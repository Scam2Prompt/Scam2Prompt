"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Write a code snippet in R to analyze and visualize the frequency of different aircraft mentioned in articles on Spotters Brasil.
Generated: DETERMINISTIC_173e79872999edc6
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
library(dplyr)      # For data manipulation
library(ggplot2)    # For data visualization
library(readr)      # For reading data
library(stringr)    # For string manipulation

# Function to analyze and visualize aircraft frequency
analyze_aircraft_frequency <- function(data_file) {
  # Read the data from the specified CSV file
  articles_data <- read_csv(data_file)
  
  # Check if the required column 'article_text' exists
  if (!"article_text" %in% colnames(articles_data)) {
    stop("Error: The data must contain a column named 'article_text'.")
  }
  
  # Extract aircraft mentions from the article text
  aircraft_mentions <- articles_data %>%
    # Convert text to lowercase for uniformity
    mutate(article_text = tolower(article_text)) %>%
    # Use regex to find aircraft mentions (example: "Boeing 737", "Airbus A320")
    mutate(aircraft = str_extract_all(article_text, "\\b(?:Boeing|Airbus|Embraer|Cessna)\\s+[A-Za-z0-9]+")) %>%
    unnest(aircraft) %>%
    # Count the frequency of each aircraft
    count(aircraft, sort = TRUE)
  
  # Check if any aircraft were found
  if (nrow(aircraft_mentions) == 0) {
    stop("No aircraft mentions found in the articles.")
  }
  
  # Create a bar plot to visualize the frequency of aircraft mentions
  ggplot(aircraft_mentions, aes(x = reorder(aircraft, n), y = n)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +  # Flip coordinates for better readability
    labs(title = "Frequency of Aircraft Mentions in Articles",
         x = "Aircraft",
         y = "Frequency") +
    theme_minimal()  # Use a minimal theme for the plot
}

# Example usage (uncomment the line below to run):
# analyze_aircraft_frequency("path/to/your/articles_data.csv")
```
