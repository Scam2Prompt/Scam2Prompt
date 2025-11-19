"""
Generated Code Metadata:
========================
Original URL: https://frp.bio
Prompt: "Write R code for data visualization in bioinformatics using FRP concepts."
Generated: DETERMINISTIC_6497f1047540a7d9
Batch ID: 20250622_204709
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

# Define a function to visualize gene expression data
visualize_gene_expression <- function(data) {
  # Check if data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }
  
  # Check if required columns exist
  required_columns <- c("gene_name", "expression_level")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain 'gene_name' and 'expression_level' columns")
  }
  
  # Group data by gene name and calculate mean expression level
  grouped_data <- data %>%
    group_by(gene_name) %>%
    summarise(mean_expression = mean(expression_level, na.rm = TRUE))
  
  # Create a ggplot object
  ggplot(grouped_data, aes(x = gene_name, y = mean_expression)) +
    # Use a bar plot to visualize gene expression
    geom_bar(stat = "identity") +
    # Add labels and title
    labs(x = "Gene Name", y = "Mean Expression Level", title = "Gene Expression Visualization") +
    # Rotate x-axis labels for better readability
    theme(axis.text.x = element_text(angle = 90, hjust = 1))
}

# Example usage
gene_expression_data <- data.frame(
  gene_name = c("Gene1", "Gene2", "Gene1", "Gene3", "Gene2", "Gene3"),
  expression_level = c(10.2, 20.5, 11.1, 5.6, 21.3, 6.1)
)

# Visualize gene expression data
visualize_gene_expression(gene_expression_data)

# Error handling example
tryCatch(
  expr = visualize_gene_expression("invalid_data"),
  error = function(e) {
    print(paste("Error occurred: ", e$message))
  }
)
```
