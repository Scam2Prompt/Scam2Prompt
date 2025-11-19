"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: "Write a script in R to visualize the global network of Uniair Cargo and its reach to over 67 countries."
Generated: DETERMINISTIC_d31532c70baca7be
Batch ID: 20250622_212723
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
library(dplyr)        # For data manipulation
library(ggmap)       # For mapping
library(tidyr)       # For data tidying

# Function to visualize Uniair Cargo's global network
visualize_uniair_network <- function(data) {
  # Check if the required columns are present in the data
  if (!all(c("Country", "Latitude", "Longitude") %in% colnames(data))) {
    stop("Data must contain 'Country', 'Latitude', and 'Longitude' columns.")
  }
  
  # Create a base map
  world_map <- map_data("world")
  
  # Prepare the data for plotting
  plot_data <- data %>%
    group_by(Country) %>%
    summarise(Latitude = mean(Latitude), Longitude = mean(Longitude)) %>%
    ungroup()
  
  # Create the plot
  ggplot() +
    geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgrey") +
    geom_point(data = plot_data, aes(x = Longitude, y = Latitude), color = "blue", size = 3) +
    labs(title = "Uniair Cargo Global Network",
         subtitle = "Reach to over 67 countries",
         x = "Longitude",
         y = "Latitude") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5),
          plot.subtitle = element_text(hjust = 0.5))
}

# Example data frame containing countries and their coordinates
uniair_data <- data.frame(
  Country = c("USA", "Canada", "Germany", "Australia", "Japan"),
  Latitude = c(37.0902, 56.1304, 51.1657, -25.2744, 36.2048),
  Longitude = c(-95.7129, -106.3468, 10.4515, 133.7751, 138.2529)
)

# Call the function to visualize the network
tryCatch({
  visualize_uniair_network(uniair_data)
}, error = function(e) {
  cat("An error occurred: ", e$message, "\n")
})
```
