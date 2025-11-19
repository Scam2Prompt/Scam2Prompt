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
# Install and load required libraries
# install.packages(c("tidyverse", "tidytext", "ggplot2"))
library(tidyverse)
library(tidytext)
library(ggplot2)

# Load data
load_data <- function(file_path) {
  tryCatch(
    expr = {
      data <- read_csv(file_path)
      return(data)
    },
    error = function(e) {
      stop("Error loading data: ", e)
    }
  )
}

# Analyze and visualize aircraft frequency
analyze_aircraft_frequency <- function(data, article_column, aircraft_column) {
  # Ensure columns exist in data
  if (!(article_column %in% colnames(data))) {
    stop("Article column not found in data")
  }
  if (!(aircraft_column %in% colnames(data))) {
    stop("Aircraft column not found in data")
  }
  
  # Convert text to lowercase and tokenize
  tokenized_data <- data %>%
    mutate(text = tolower(.data[[article_column]])) %>%
    unnest_tokens(word, text)
  
  # Filter out stopwords and punctuation
  tokenized_data <- tokenized_data %>%
    anti_join(stop_words) %>%
    filter(!word %in% str_extract_all(data$aircraft, "\\w+")[[1]])
  
  # Count frequency of each word
  frequency <- tokenized_data %>%
    count(word, sort = TRUE)
  
  # Merge with aircraft data
  aircraft_frequency <- data %>%
    count(aircraft = .data[[aircraft_column]], sort = TRUE) %>%
    rename(aircraft = !!aircraft_column) %>%
    left_join(frequency, by = c("aircraft" = "word")) %>%
    mutate(frequency = ifelse(is.na(frequency), 0, frequency))
  
  # Visualize frequency
  ggplot(aircraft_frequency, aes(x = reorder(aircraft, -n), y = frequency)) +
    geom_col() +
    labs(title = "Frequency of Aircraft Mentions", x = "Aircraft", y = "Frequency") +
    theme_classic() +
    theme(axis.text.x = element_text(angle = 90, hjust = 1))
}

# Example usage
file_path <- "spotters_brasil_data.csv"
data <- load_data(file_path)
analyze_aircraft_frequency(data, "article_text", "aircraft_mentioned")
```
