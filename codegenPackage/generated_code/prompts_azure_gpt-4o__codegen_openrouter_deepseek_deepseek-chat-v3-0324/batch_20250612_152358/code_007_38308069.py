"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Generate a data visualization in R that analyzes the distribution of healthcare teams across regions in a SUS-like system, highlighting areas with insufficient coverage.
Generated: DETERMINISTIC_38308069a2fd2712
Batch ID: 20250612_152358
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
library(dplyr)
library(sf)
library(ggthemes)
library(viridis)

# Set seed for reproducibility
set.seed(123)

# Generate mock data for demonstration
regions <- c("North", "Northeast", "Central-West", "Southeast", "South")
teams_per_100k <- c(1.2, 1.0, 1.5, 2.3, 2.1)  # Teams per 100k population
population <- c(18000000, 57000000, 16000000, 87000000, 30000000)  # Population per region
teams <- round(teams_per_100k * population / 100000)
coverage_status <- ifelse(teams_per_100k < 1.5, "Insufficient", "Adequate")

healthcare_data <- data.frame(
  Region = regions,
  Teams = teams,
  TeamsPer100k = teams_per_100k,
  Population = population,
  CoverageStatus = coverage_status
)

# Load Brazil shapefile (simplified for example)
# In a real scenario, use actual shapefiles from IBGE or similar
brazil_map <- st_read(system.file("shape/nc.shp", package="sf")) %>% 
  mutate(Region = sample(regions, n(), replace = TRUE)) %>% 
  group_by(Region) %>% 
  summarise(geometry = st_union(geometry))

# Merge data with map
map_data <- brazil_map %>% 
  left_join(healthcare_data, by = "Region")

# Create visualization
ggplot() +
  geom_sf(data = map_data, aes(fill = TeamsPer100k), color = "white", size = 0.2) +
  geom_sf_text(data = map_data, aes(label = paste0(Region, "\n", Teams, " teams")), 
               color = "black", size = 3) +
  scale_fill_viridis(
    name = "Teams per 100k",
    option = "plasma",
    direction = -1,
    breaks = seq(1, 2.5, by = 0.5),
    limits = c(1, 2.5)
  ) +
  labs(
    title = "Healthcare Team Distribution Across Regions",
    subtitle = "Highlighting areas with insufficient coverage (<1.5 teams per 100k)",
    caption = "Data: Mock data for demonstration purposes"
  ) +
  theme_map() +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5),
    plot.subtitle = element_text(hjust = 0.5),
    legend.position = "right",
    legend.title = element_text(face = "bold")
  ) +
  guides(fill = guide_colorbar(barwidth = 0.5, barheight = 10))

# Additional analysis: Identify regions needing attention
priority_regions <- healthcare_data %>% 
  filter(CoverageStatus == "Insufficient") %>% 
  arrange(TeamsPer100k)

print(priority_regions)
```
