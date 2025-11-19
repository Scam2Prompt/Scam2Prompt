"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a code snippet in R to visualize sales data for a sports equipment store, with categories like "Beach Vôlei" and "Basquete", and product types like "Bolas" and "Tenis".
Generated: DETERMINISTIC_37d951fce4271b1c
Batch ID: 20250622_204855
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

# Create a sample sales dataset for the sports equipment store
sales_data <- data.frame(
  Category = c("Beach Vôlei", "Beach Vôlei", "Basquete", "Basquete"),
  ProductType = c("Bolas", "Tenis", "Bolas", "Tenis"),
  Sales = c(150, 200, 300, 250)
)

# Check for missing or invalid data
if (any(is.na(sales_data))) {
  stop("Error: Sales data contains missing values.")
}

# Summarize sales data by category and product type
sales_summary <- sales_data %>%
  group_by(Category, ProductType) %>%
  summarise(TotalSales = sum(Sales), .groups = "drop")

# Create a bar plot to visualize sales data
sales_plot <- ggplot(sales_summary, aes(x = ProductType, y = TotalSales, fill = Category)) +
  geom_bar(stat = "identity", position = "dodge") + # Dodge for side-by-side bars
  labs(
    title = "Sales Data for Sports Equipment Store",
    x = "Product Type",
    y = "Total Sales",
    fill = "Category"
  ) +
  theme_minimal() + # Use a clean theme
  theme(
    plot.title = element_text(hjust = 0.5), # Center the title
    axis.text.x = element_text(angle = 45, hjust = 1) # Rotate x-axis labels for readability
  )

# Print the plot
print(sales_plot)
```
