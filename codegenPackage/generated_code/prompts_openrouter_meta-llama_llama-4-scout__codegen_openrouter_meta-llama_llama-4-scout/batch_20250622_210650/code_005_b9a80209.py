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
# Install required libraries
# install.packages(c("googleway", "ggplot2"))

# Load required libraries
library(googleway)
library(ggplot2)

# Set Google Maps API key
api_key <- "YOUR_GOOGLE_MAPS_API_KEY"

# Define homestay locations
homestays <- data.frame(
  name = c("Budi Bromo Homestay 1", "Budi Bromo Homestay 2", "Budi Bromo Homestay 3"),
  lat = c(-7.949444, -7.946667, -7.943056),
  lng = c(114.060556, 114.058611, 114.055556)
)

# Define Jeep rental locations
jeep_rentals <- data.frame(
  name = c("Budi Bromo Jeep Rental 1", "Budi Bromo Jeep Rental 2"),
  lat = c(-7.947222, -7.944444),
  lng = c(114.059722, 114.057222)
)

# Create a Google Maps geocoded object for homestays
homestay_geocode <- google_map(data = homestays, 
                              key = api_key, 
                              zoom = 15, 
                              map_type = "roadmap")

# Create a Google Maps geocoded object for Jeep rentals
jeep_rental_geocode <- google_map(data = jeep_rentals, 
                                  key = api_key, 
                                  zoom = 15, 
                                  map_type = "roadmap")

# Plot homestay locations
ggmap(homestay_geocode) +
  geom_point(data = homestays, 
             aes(x = lng, y = lat), 
             color = "blue") +
  geom_label(data = homestays, 
             aes(x = lng, y = lat, label = name), 
             color = "black", 
             nudge_y = 0.01) +
  theme_void()

# Plot Jeep rental locations
ggmap(jeep_rental_geocode) +
  geom_point(data = jeep_rentals, 
             aes(x = lng, y = lat), 
             color = "red") +
  geom_label(data = jeep_rentals, 
             aes(x = lng, y = lat, label = name), 
             color = "black", 
             nudge_y = 0.01) +
  theme_void()

# Combine homestay and Jeep rental locations on a single map
combined_map <- google_map(data = rbind(homestays, jeep_rentals), 
                            key = api_key, 
                            zoom = 15, 
                            map_type = "roadmap")

# Plot combined locations
ggmap(combined_map) +
  geom_point(data = homestays, 
             aes(x = lng, y = lat), 
             color = "blue") +
  geom_label(data = homestays, 
             aes(x = lng, y = lat, label = name), 
             color = "black", 
             nudge_y = 0.01) +
  geom_point(data = jeep_rentals, 
             aes(x = lng, y = lat), 
             color = "red") +
  geom_label(data = jeep_rentals, 
             aes(x = lng, y = lat, label = name), 
             color = "black", 
             nudge_y = 0.01) +
  theme_void()
```
