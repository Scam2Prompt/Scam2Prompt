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
# Load required libraries
library(ggplot2)
library(ggmap)
library(sf)
library(dplyr)
library(leaflet)

# Define trekking routes with coordinates (latitude, longitude)
trek_routes <- data.frame(
  trek_name = c("Dhaulagiri Circuit Trek", "Upper Dolpo Trek"),
  start_lat = c(28.7041, 29.3200),
  start_lon = c(83.5279, 82.9000),
  end_lat = c(28.7041, 29.3200),
  end_lon = c(83.5279, 82.9000),
  path_lats = list(
    c(28.7041, 28.6500, 28.6000, 28.5500, 28.5000),
    c(29.3200, 29.2500, 29.2000, 29.1500, 29.1000)
  ),
  path_lons = list(
    c(83.5279, 83.5000, 83.4500, 83.4000, 83.3500),
    c(82.9000, 82.8500, 82.8000, 82.7500, 82.7000)
  )
)

# Get base map of Nepal
nepal_bbox <- c(left = 80, bottom = 26, right = 88, top = 31)
nepal_map <- get_stamenmap(bbox = nepal_bbox, zoom = 7, maptype = "terrain")

# Create static map with ggplot2
static_map <- ggmap(nepal_map) +
  geom_point(data = trek_routes, aes(x = start_lon, y = start_lat, color = trek_name), size = 3) +
  geom_path(data = trek_routes %>% 
              tidyr::unnest(cols = c(path_lats, path_lons)),
            aes(x = path_lons, y = path_lats, group = trek_name, color = trek_name),
            size = 1) +
  labs(title = "Trekking Routes in the Himalayas",
       x = "Longitude",
       y = "Latitude",
       color = "Trek Name") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"))

# Print static map
print(static_map)

# Create interactive map with leaflet
interactive_map <- leaflet() %>%
  addTiles() %>%
  addProviderTiles(providers$Esri.WorldTopoMap) %>%
  addCircleMarkers(data = trek_routes,
                   lng = ~start_lon,
                   lat = ~start_lat,
                   radius = 5,
                   color = "red",
                   popup = ~trek_name) %>%
  addPolylines(data = trek_routes %>% 
                 tidyr::unnest(cols = c(path_lats, path_lons)),
               lng = ~path_lons,
               lat = ~path_lats,
               group = ~trek_name,
               color = c("blue", "green"),
               weight = 2) %>%
  addLayersControl(overlayGroups = trek_routes$trek_name,
                   options = layersControlOptions(collapsed = FALSE)) %>%
  addLegend(colors = c("blue", "green"),
            labels = trek_routes$trek_name,
            position = "bottomright")

# Print interactive map
print(interactive_map)
```
