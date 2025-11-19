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
# Load necessary libraries
library(ggplot2)      # For data visualization
library(sf)           # For handling spatial data
library(dplyr)        # For data manipulation
library(ggmap)        # For Google Maps integration

# Define a function to visualize trekking routes
visualize_trekking_routes <- function(routes_data) {
  # Check if the input data is a data frame
  if (!is.data.frame(routes_data)) {
    stop("Input must be a data frame.")
  }
  
  # Ensure required columns are present
  required_columns <- c("route_name", "latitude", "longitude")
  if (!all(required_columns %in% colnames(routes_data))) {
    stop("Data frame must contain the following columns: route_name, latitude, longitude.")
  }
  
  # Create a base map of the Himalayas
  himalayas_map <- get_map(location = c(lon = 82.5, lat = 28.5), zoom = 6, maptype = "terrain")

  # Plot the trekking routes on the map
  ggmap(himalayas_map) +
    geom_point(data = routes_data, aes(x = longitude, y = latitude, color = route_name), size = 3) +
    labs(title = "Trekking Routes in the Himalayas",
         x = "Longitude",
         y = "Latitude",
         color = "Trekking Route") +
    theme_minimal() +
    theme(legend.position = "bottom")
}

# Example data for trekking routes
trekking_routes <- data.frame(
  route_name = c("Dhaulagiri Circuit Trek", "Upper Dolpo Trek"),
  latitude = c(28.6941, 29.2000),  # Example coordinates
  longitude = c(83.4870, 82.8000)
)

# Call the function to visualize the trekking routes
visualize_trekking_routes(trekking_routes)
```
