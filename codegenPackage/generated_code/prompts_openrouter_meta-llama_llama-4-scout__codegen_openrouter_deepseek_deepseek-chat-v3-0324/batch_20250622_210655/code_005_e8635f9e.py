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
# Load required libraries
library(ggplot2)
library(sf)
library(rnaturalearth)
library(dplyr)

# Get Brazil map data
brazil_map <- ne_states(country = "brazil", returnclass = "sf")

# Filter for Sul and Sudeste regions
target_regions <- c("Sul", "Sudeste")
regions_data <- brazil_map %>% 
  filter(region %in% target_regions)

# Create the visualization
ggplot() +
  geom_sf(data = brazil_map, fill = "lightgray", color = "white") +
  geom_sf(data = regions_data, fill = "#1f78b4", color = "white") +
  labs(title = "Geographic Regions Served by Sal Diana's Facility",
       subtitle = "Sul and Sudeste Regions of Brazil",
       caption = "Source: Natural Earth Data") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5),
        axis.text = element_blank(),
        axis.title = element_blank(),
        panel.grid = element_blank())
```
