"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.com
Prompt: "Write a script in R to visualize the locations of Budi Bromo Tour's homestays and Jeep rental services in Mount Bromo using Google Maps API."
Generated: DETERMINISTIC_b9a80209e9287e4c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(httr)
library(jsonlite)
library(ggplot2)
library(ggmap)
library(dplyr)

# Google Maps API Key (replace with your actual API key)
api_key <- "YOUR_GOOGLE_MAPS_API_KEY"

# Register the Google Maps API key
register_google(key = api_key)

# Sample data for Budi Bromo Tour services
locations <- data.frame(
  name = c("Budi Bromo Homestay", "Jeep Rental Service 1", "Jeep Rental Service 2", 
           "Bromo View Homestay", "Jeep Rental Service 3"),
  type = c("homestay", "jeep", "jeep", "homestay", "jeep"),
  lat = c(-7.9425, -7.9400, -7.9412, -7.9438, -7.9395),
  lng = c(112.9530, 112.9515, 112.9543, 112.9521, 112.9508),
  stringsAsFactors = FALSE
)

# Function to get map centered on Bromo area
get_bromo_map <- function() {
  bromo_center <- c(lon = 112.95, lat = -7.94)
  map <- get_map(location = bromo_center, zoom = 14, maptype = "terrain")
  return(map)
}

# Function to plot locations on the map
plot_locations <- function(map_data, locations_df) {
  ggmap(map_data) +
    geom_point(data = locations_df, 
               aes(x = lng, y = lat, color = type), 
               size = 4, alpha = 0.8) +
    scale_color_manual(values = c("homestay" = "blue", "jeep" = "red")) +
    labs(title = "Budi Bromo Tour Services in Mount Bromo Area",
         subtitle = "Homestays and Jeep Rental Locations",
         x = "Longitude", 
         y = "Latitude",
         color = "Service Type") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"),
          plot.subtitle = element_text(hjust = 0.5))
}

# Main function to execute the visualization
visualize_bromo_services <- function() {
  tryCatch({
    # Get the map
    bromo_map <- get_bromo_map()
    
    # Plot the locations
    service_map <- plot_locations(bromo_map, locations)
    
    # Display the map
    print(service_map)
    
    # Save the plot
    ggsave("bromo_services_map.png", plot = service_map, width = 10, height = 8, dpi = 300)
    
    message("Map successfully generated and saved as 'bromo_services_map.png'")
  }, error = function(e) {
    message("Error occurred: ", e$message)
    message("Please check your API key and internet connection.")
  })
}

# Execute the visualization
visualize_bromo_services()
```
