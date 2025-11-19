"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: "Generate a code snippet in R to visualize the production data of Omega Energy's Bloque Buenavista, Campo Corrales, and Campo Bolívar operations."
Generated: DETERMINISTIC_634913e105d69bc2
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Simulated production data for Omega Energy's operations
# Replace this with actual data if available
production_data <- data.frame(
  Operation = c("Bloque Buenavista", "Campo Corrales", "Campo Bolívar"),
  Month = rep(seq.Date(from = as.Date("2023-01-01"), to = as.Date("2023-12-01"), by = "month"), each = 3),
  Production = c(
    # Bloque Buenavista
    runif(12, min = 500, max = 1000),
    # Campo Corrales
    runif(12, min = 300, max = 800),
    # Campo Bolívar
    runif(12, min = 400, max = 900)
  )
)

# Ensure data is clean and structured
if (any(is.na(production_data))) {
  stop("Error: Production data contains missing values.")
}

# Summarize data for visualization
summary_data <- production_data %>%
  group_by(Operation, Month) %>%
  summarise(TotalProduction = sum(Production), .groups = "drop")

# Create a line plot to visualize production data
production_plot <- ggplot(summary_data, aes(x = Month, y = TotalProduction, color = Operation)) +
  geom_line(size = 1) + # Line plot for production trends
  geom_point(size = 2) + # Points for better visibility
  labs(
    title = "Production Data of Omega Energy Operations",
    subtitle = "Bloque Buenavista, Campo Corrales, and Campo Bolívar",
    x = "Month",
    y = "Total Production (Units)",
    color = "Operation"
  ) +
  theme_minimal() + # Clean theme for better readability
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    plot.subtitle = element_text(hjust = 0.5, size = 12),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

# Display the plot
print(production_plot)
```
