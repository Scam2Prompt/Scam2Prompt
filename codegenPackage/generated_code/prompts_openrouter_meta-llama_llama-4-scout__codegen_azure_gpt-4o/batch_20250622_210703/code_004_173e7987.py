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

```R
# Load necessary libraries
library(tidyverse)  # For data manipulation and visualization
library(stringr)    # For string operations

# Function to analyze and visualize aircraft frequency
analyze_aircraft_frequency <- function(articles) {
  # Error handling: Check if input is a character vector
  if (!is.character(articles)) {
    stop("Input must be a character vector containing articles.")
  }
  
  # Define a list of aircraft models to search for
  aircraft_models <- c("Boeing 737", "Airbus A320", "Boeing 747", "Airbus A380", 
                       "Embraer E190", "Cessna 172", "Bombardier CRJ", "Boeing 777")
  
  # Create a data frame to store frequency counts
  aircraft_frequency <- tibble(
    Aircraft = aircraft_models,
    Frequency = sapply(aircraft_models, function(model) {
      sum(str_count(tolower(articles), tolower(model)))  # Count occurrences of each model
    })
  )
  
  # Sort the data frame by frequency in descending order
  aircraft_frequency <- aircraft_frequency %>%
    arrange(desc(Frequency))
  
  # Visualization: Bar plot of aircraft frequencies
  ggplot(aircraft_frequency, aes(x = reorder(Aircraft, Frequency), y = Frequency)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +
    labs(
      title = "Frequency of Aircraft Mentioned in Articles",
      x = "Aircraft Model",
      y = "Frequency"
    ) +
    theme_minimal()
}

# Example usage
# Replace `articles` with a character vector containing the text of articles
articles <- c(
  "The Boeing 737 is a popular aircraft. Airbus A320 is also widely used.",
  "Spotters love the Boeing 747 and Airbus A380 for their size.",
  "Embraer E190 is a regional jet, while Cessna 172 is a small aircraft.",
  "Boeing 777 is a long-haul aircraft, and Bombardier CRJ is a regional jet."
)

# Call the function to analyze and visualize aircraft frequency
analyze_aircraft_frequency(articles)
```
