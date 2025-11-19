"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Write a script in R to visualize the growth of tractor pulling as a sport in Australia, using hypothetical data similar to what Kelvin Jobling discusses on his website."
Generated: DETERMINISTIC_da7cc214f68dfec2
Batch ID: 20250622_205138
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
library(tidyr)
library(lubridate)

# Set seed for reproducibility
set.seed(123)

# Generate hypothetical tractor pulling data for Australia (2010-2023)
years <- 2010:2023
events <- round(seq(5, 50, length.out = length(years)) + rnorm(length(years), sd = 3))
participants <- round(seq(20, 300, length.out = length(years)) + rnorm(length(years), sd = 15))
spectators <- round(seq(500, 15000, length.out = length(years)) + rnorm(length(years), sd = 500))
prize_money <- round(seq(5000, 200000, length.out = length(years)) + rnorm(length(years), sd = 10000))

# Create data frame
tractor_data <- data.frame(
  Year = years,
  Events = pmax(events, 0), # Ensure no negative values
  Participants = pmax(participants, 0),
  Spectators = pmax(spectators, 0),
  PrizeMoney = pmax(prize_money, 0)
)

# Function to create growth visualization
visualize_tractor_growth <- function(data) {
  tryCatch({
    # Reshape data for plotting
    plot_data <- data %>%
      pivot_longer(cols = -Year, names_to = "Metric", values_to = "Value")
    
    # Create growth plot
    growth_plot <- ggplot(plot_data, aes(x = Year, y = Value, color = Metric)) +
      geom_line(size = 1.2) +
      geom_point(size = 3) +
      scale_y_continuous(labels = scales::comma) +
      scale_color_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728")) +
      labs(
        title = "Growth of Tractor Pulling in Australia (2010-2023)",
        subtitle = "Hypothetical data based on trends discussed by Kelvin Jobling",
        x = "Year",
        y = "Count/Amount",
        color = "Metric"
      ) +
      theme_minimal() +
      theme(
        plot.title = element_text(size = 16, face = "bold"),
        plot.subtitle = element_text(size = 12),
        legend.position = "bottom",
        panel.grid.major = element_line(color = "gray90"),
        panel.grid.minor = element_blank()
      )
    
    # Create faceted plot for individual metrics
    facet_plot <- ggplot(plot_data, aes(x = Year, y = Value)) +
      geom_line(color = "#1f77b4", size = 1.2) +
      geom_point(color = "#1f77b4", size = 3) +
      scale_y_continuous(labels = scales::comma) +
      facet_wrap(~Metric, scales = "free_y", ncol = 2) +
      labs(
        title = "Detailed Growth Metrics of Tractor Pulling in Australia",
        x = "Year",
        y = "Count/Amount"
      ) +
      theme_minimal() +
      theme(
        plot.title = element_text(size = 16, face = "bold"),
        strip.text = element_text(size = 12, face = "bold"),
        panel.grid.major = element_line(color = "gray90"),
        panel.grid.minor = element_blank()
      )
    
    # Return both plots in a list
    list(combined_plot = growth_plot, facet_plot = facet_plot)
    
  }, error = function(e) {
    message("Error in visualization: ", e$message)
    return(NULL)
  })
}

# Generate visualizations
plots <- visualize_tractor_growth(tractor_data)

# Display plots if successful
if (!is.null(plots)) {
  print(plots$combined_plot)
  print(plots$facet_plot)
  
  # Save plots
  try({
    ggsave("tractor_pulling_growth_combined.png", plot = plots$combined_plot, 
           width = 10, height = 6, dpi = 300)
    ggsave("tractor_pulling_growth_faceted.png", plot = plots$facet_plot, 
           width = 10, height = 8, dpi = 300)
    message("Plots saved successfully.")
  }, error = function(e) {
    message("Failed to save plots: ", e$message)
  })
} else {
  message("Failed to generate visualizations.")
}
```
