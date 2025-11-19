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

```r
# Install and load necessary libraries
# install.packages(c("vegan", "ggplot2", "RColorBrewer"))
library(vegan)
library(ggplot2)
library(RColorBrewer)

# Sample dataset: medicinal plant species abundance
set.seed(123)
species_data <- data.frame(
  Species = c("Aloe vera", "Calendula officinalis", "Hypericum perforatum", 
               "Melissa officinalis", "Passiflora incarnata", "Valeriana officinalis"),
  Site1 = c(10, 5, 8, 12, 6, 9),
  Site2 = c(8, 10, 7, 11, 9, 5),
  Site3 = c(12, 6, 9, 8, 10, 7),
  Site4 = c(9, 8, 11, 7, 5, 10),
  Site5 = c(7, 12, 5, 10, 8, 6)
)

# Convert data to matrix
species_matrix <- as.matrix(species_data[, 2:6])

# Perform Bray-Curtis dissimilarity
distance_matrix <- vegdist(species_matrix, method = "bray")

# Perform non-metric multidimensional scaling (NMDS)
nmds_result <- cmdscale(distance_matrix, k = 2, eig = TRUE)

# Create a data frame for NMDS results
nmds_df <- data.frame(
  Species = rownames(species_matrix),
  NMDS1 = nmds_result$points[, 1],
  NMDS2 = nmds_result$points[, 2]
)

# Create a data frame for heatmap
heatmap_df <- data.frame(
  Site = rep(c("Site1", "Site2", "Site3", "Site4", "Site5"), each = 6),
  Species = rep(rownames(species_matrix), 5),
  Abundance = as.vector(species_matrix)
)

# Plot NMDS
ggplot(nmds_df, aes(x = NMDS1, y = NMDS2)) +
  geom_point() +
  theme_classic() +
  labs(title = "Non-metric Multidimensional Scaling (NMDS) of Medicinal Plant Species",
       subtitle = "Bray-Curtis Dissimilarity",
       x = "NMDS Axis 1",
       y = "NMDS Axis 2")

# Plot heatmap
ggplot(heatmap_df, aes(x = Species, y = Site, fill = Abundance)) +
  geom_tile() +
  scale_fill_gradient(low = "blue", high = "red") +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(title = "Heatmap of Medicinal Plant Species Abundance",
       subtitle = "",
       x = "Medicinal Plant Species",
       y = "Site",
       fill = "Abundance")
```
