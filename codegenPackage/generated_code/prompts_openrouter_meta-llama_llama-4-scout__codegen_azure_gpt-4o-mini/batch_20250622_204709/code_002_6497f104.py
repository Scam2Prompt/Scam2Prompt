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
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(tidyr)    # For data tidying

# Function to visualize gene expression data
# This function takes a data frame of gene expression data and a gene of interest
# It generates a boxplot to visualize the expression levels across different conditions
visualize_gene_expression <- function(data, gene, condition_col, expression_col) {
  # Check if the required columns exist in the data
  if (!(condition_col %in% colnames(data))) {
    stop(paste("Condition column", condition_col, "not found in data."))
  }
  if (!(expression_col %in% colnames(data))) {
    stop(paste("Expression column", expression_col, "not found in data."))
  }
  
  # Filter the data for the gene of interest
  gene_data <- data %>%
    filter(!!sym(expression_col) == gene)
  
  # Check if the gene data is empty
  if (nrow(gene_data) == 0) {
    stop(paste("No data found for gene:", gene))
  }
  
  # Create the boxplot
  plot <- ggplot(gene_data, aes_string(x = condition_col, y = expression_col)) +
    geom_boxplot(fill = "lightblue", outlier.colour = "red") +
    labs(title = paste("Expression of", gene),
         x = "Condition",
         y = "Expression Level") +
    theme_minimal() +
    theme(text = element_text(size = 12))
  
  # Print the plot
  print(plot)
}

# Example usage
# Load example data (replace with actual data)
# data <- read.csv("gene_expression_data.csv")

# Call the function with the appropriate parameters
# visualize_gene_expression(data, "GeneA", "Condition", "Expression")
```

Make sure to replace the example data loading and function call with your actual data and parameters when using the code.
