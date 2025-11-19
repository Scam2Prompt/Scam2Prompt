"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a code snippet in R to visualize the geographical locations of different trekking routes in the Himalayas, such as the Dhaulagiri Circuit Trek and the Upper Dolpo Trek.
Generated: DETERMINISTIC_4fbe7e7f2381c8f6
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install required libraries
# install.packages(c("ggplot2", "leaflet", "sf"))

# Load required libraries
library(ggplot2)
library(leaflet)
library(sf)

# Define trekking routes data
trekking_routes <- data.frame(
  name = c("Dhaulagiri Circuit Trek", "Upper Dolpo Trek"),
  latitude = c(29.5, 29.0),
  longitude = c(83.5, 83.0),
  elevation_gain = c(6000, 5000),
  duration = c(20, 18)
)

# Create a SpatialPoints object
trekking_routes_sf <- st_as_sf(trekking_routes, 
                                coords = c("longitude", "latitude"), 
                                crs = 4326)

# Leaflet map
leaflet_map <- leaflet(trekking_routes_sf) %>%
  addTiles() %>%
  addMarkers(~longitude, ~latitude, 
             label = ~name, 
             labelOptions = labelOptions(textsize = "15px"))

# Print leaflet map
leaflet_map

# GGplot
ggplot(trekking_routes_sf) + 
  geom_sf() + 
  geom_sf_label(aes(label = name), 
                size = 3, 
                color = "red") + 
  theme_void() + 
  theme(legend.position = "none")

# Save GGplot to file
ggsave("trekking_routes_ggplot.png")

# Save Leaflet map to file
library(htmltools)
saveWidget(leaflet_map, "trekking_routes_leaflet.html")
```
