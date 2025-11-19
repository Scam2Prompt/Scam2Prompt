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

```R
# Load necessary libraries
library(ggplot2)       # For visualization
library(ggmap)         # For working with maps
library(dplyr)         # For data manipulation

# Define trekking route data (latitude and longitude coordinates for each route)
trekking_routes <- data.frame(
  Trek = c("Dhaulagiri Circuit Trek", "Upper Dolpo Trek"),
  Latitude = c(28.7465, 29.0845),
  Longitude = c(83.6187, 82.9310)
)

# Function to fetch the base map of the Himalayas
get_himalayas_map <- function() {
  # Define the bounding box for the Himalayas region
  bbox <- c(left = 80.0, bottom = 27.0, right = 88.0, top = 30.0)
  
  # Fetch the map using ggmap
  himalayas_map <- get_stamenmap(bbox, zoom = 8, maptype = "terrain")
  
  return(himalayas_map)
}

# Fetch the map
himalayas_map <- get_himalayas_map()

# Plot the map with trekking routes
ggmap(himalayas_map) +
  geom_point(data = trekking_routes, aes(x = Longitude, y = Latitude, color = Trek), size = 3) +
  geom_text(data = trekking_routes, aes(x = Longitude, y = Latitude, label = Trek), vjust = -1, hjust = 0.5, size = 3) +
  labs(
    title = "Geographical Locations of Trekking Routes in the Himalayas",
    x = "Longitude",
    y = "Latitude",
    color = "Trekking Route"
  ) +
  theme_minimal()

# Note: Ensure you have an active internet connection to fetch the map data.
# If ggmap is not installed, install it using install.packages("ggmap").
```
