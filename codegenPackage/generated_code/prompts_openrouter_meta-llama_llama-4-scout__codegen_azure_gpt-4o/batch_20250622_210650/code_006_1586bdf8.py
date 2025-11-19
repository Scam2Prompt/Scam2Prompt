"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Write a code example in R for analyzing the biodiversity of medicinal plant species, such as those cultivated by Oromaticas, and visualizing the results in a heatmap."
Generated: DETERMINISTIC_1586bdf860c046cf
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
library(ggplot2)      # For visualization
library(reshape2)     # For data manipulation
library(dplyr)        # For data wrangling
library(pheatmap)     # For heatmap generation

# Function to analyze biodiversity and visualize results
analyze_biodiversity <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Ensure required columns exist
  required_columns <- c("Species", "Location", "Count")
  missing_columns <- setdiff(required_columns, colnames(data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Summarize data: Total count of each species per location
  summarized_data <- data %>%
    group_by(Location, Species) %>%
    summarize(Total_Count = sum(Count, na.rm = TRUE), .groups = "drop")
  
  # Reshape data for heatmap (wide format)
  heatmap_data <- summarized_data %>%
    dcast(Location ~ Species, value.var = "Total_Count", fill = 0)
  
  # Convert to matrix for heatmap
  heatmap_matrix <- as.matrix(heatmap_data[, -1])  # Exclude Location column
  
  # Generate heatmap
  pheatmap(
    heatmap_matrix,
    cluster_rows = TRUE,       # Cluster locations
    cluster_cols = TRUE,       # Cluster species
    scale = "row",             # Normalize rows
    main = "Biodiversity Heatmap of Medicinal Plant Species",
    color = colorRampPalette(c("white", "blue", "green"))(50),
    labels_row = heatmap_data$Location,  # Add location labels
    fontsize = 10
  )
}

# Example usage
# Create a sample dataset
sample_data <- data.frame(
  Species = c("PlantA", "PlantB", "PlantC", "PlantA", "PlantB", "PlantC"),
  Location = c("Site1", "Site1", "Site1", "Site2", "Site2", "Site2"),
  Count = c(10, 5, 15, 20, 10, 25)
)

# Analyze biodiversity and visualize results
analyze_biodiversity(sample_data)
```
