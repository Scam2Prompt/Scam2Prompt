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

```R
# Load necessary libraries
library(tidyverse)  # For data manipulation and visualization
library(litsearchr) # For systematic literature review
library(igraph)     # For network analysis
library(stringr)    # For string manipulation

# Define search terms related to organizational change management
# These terms should be refined based on domain expertise
search_terms <- c(
  "organizational change",
  "change management",
  "development",
  "organizational development",
  "leadership",
  "employee engagement",
  "organizational culture",
  "resistance to change",
  "change strategy"
)

# Function to perform systematic review
perform_systematic_review <- function(search_terms, database = "PubMed") {
  # Error handling for input validation
  if (!is.character(search_terms) || length(search_terms) == 0) {
    stop("Search terms must be a non-empty character vector.")
  }
  
  # Initialize an empty list to store results
  review_results <- list()
  
  # Loop through each search term and query the database
  for (term in search_terms) {
    tryCatch({
      # Simulate a database query (replace with actual database query code)
      # Example: Using litsearchr to search for articles
      results <- litsearchr::get_articles(
        terms = term,
        database = database
      )
      
      # Append results to the review_results list
      review_results[[term]] <- results
    }, error = function(e) {
      # Handle errors gracefully
      message(paste("Error querying term:", term, "-", e$message))
    })
  }
  
  # Combine all results into a single data frame
  combined_results <- bind_rows(review_results, .id = "search_term")
  
  # Return the combined results
  return(combined_results)
}

# Perform the systematic review
# Replace "PubMed" with the desired database name
results <- perform_systematic_review(search_terms, database = "PubMed")

# Save results to a CSV file for further analysis
write_csv(results, "systematic_review_results.csv")

# Print a summary of the results
print(paste("Systematic review completed. Results saved to 'systematic_review_results.csv'."))
```
