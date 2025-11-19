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
# Load required libraries
library(vegan)       # For biodiversity analysis
library(ggplot2)     # For visualization
library(dplyr)       # For data manipulation
library(tidyr)       # For data tidying
library(RColorBrewer) # For color palettes

# Function to calculate biodiversity indices
calculate_biodiversity <- function(species_data) {
  # Calculate Shannon diversity index
  shannon <- diversity(species_data, index = "shannon")
  
  # Calculate Simpson diversity index
  simpson <- diversity(species_data, index = "simpson")
  
  # Calculate species richness
  richness <- specnumber(species_data)
  
  # Return results as a data frame
  data.frame(
    Site = rownames(species_data),
    Shannon = shannon,
    Simpson = simpson,
    Richness = richness
  )
}

# Function to create heatmap visualization
create_heatmap <- function(species_data, title = "Medicinal Plant Biodiversity") {
  # Convert data to long format for ggplot
  long_data <- species_data %>%
    gather(key = "Species", value = "Abundance", -Site) %>%
    mutate(Abundance = as.numeric(Abundance))
  
  # Create heatmap
  ggplot(long_data, aes(x = Site, y = Species, fill = Abundance)) +
    geom_tile(color = "white") +
    scale_fill_gradientn(
      colours = brewer.pal(9, "YlOrRd"),
      na.value = "white",
      name = "Abundance"
    ) +
    labs(
      title = title,
      x = "Cultivation Site",
      y = "Plant Species"
    ) +
    theme_minimal() +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1),
      plot.title = element_text(hjust = 0.5, face = "bold")
    )
}

# Example usage with simulated data
# Simulate medicinal plant species data for Oromaticas cultivation sites
set.seed(123)
num_sites <- 5
num_species <- 10
site_names <- paste("Site", LETTERS[1:num_sites])
species_names <- paste("Species", 1:num_species)

# Create simulated abundance data
species_data <- matrix(
  sample(0:100, num_sites * num_species, replace = TRUE),
  nrow = num_sites,
  ncol = num_species,
  dimnames = list(site_names, species_names)
)

# Convert to data frame
species_df <- as.data.frame(species_data)
species_df$Site <- rownames(species_df)

# Calculate biodiversity indices
biodiversity_results <- calculate_biodiversity(species_data)
print(biodiversity_results)

# Create and display heatmap
heatmap_plot <- create_heatmap(species_df)
print(heatmap_plot)
```
