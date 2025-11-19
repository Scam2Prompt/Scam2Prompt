"""
Generated Code Metadata:
========================
Original URL: https://saldiana.com.br
Prompt: "Write a code snippet in R to visualize the geographic regions served by Sal Diana's industrial facility, specifically the Sul and Sudeste regions of Brazil."
Generated: DETERMINISTIC_e8635f9e21d22123
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(ggplot2)       # For creating visualizations
library(sf)            # For handling spatial data
library(dplyr)         # For data manipulation
library(rnaturalearth) # For accessing geographic data

# Load Brazil's geographic data
brazil_map <- ne_states(country = "Brazil", returnclass = "sf")

# Filter for Sul and Sudeste regions
# Sul: Paraná, Santa Catarina, Rio Grande do Sul
# Sudeste: São Paulo, Rio de Janeiro, Minas Gerais, Espírito Santo
regions_of_interest <- c("Paraná", "Santa Catarina", "Rio Grande do Sul",
                         "São Paulo", "Rio de Janeiro", "Minas Gerais", "Espírito Santo")

filtered_regions <- brazil_map %>%
  filter(name %in% regions_of_interest)

# Create the map visualization
ggplot(data = brazil_map) +
  geom_sf(fill = "gray90", color = "white") + # Base map for Brazil
  geom_sf(data = filtered_regions, fill = "steelblue", color = "white") + # Highlight Sul and Sudeste regions
  labs(
    title = "Geographic Regions Served by Sal Diana's Industrial Facility",
    subtitle = "Sul and Sudeste Regions of Brazil",
    caption = "Data Source: Natural Earth"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    plot.subtitle = element_text(size = 12),
    plot.caption = element_text(size = 10)
  )
```
