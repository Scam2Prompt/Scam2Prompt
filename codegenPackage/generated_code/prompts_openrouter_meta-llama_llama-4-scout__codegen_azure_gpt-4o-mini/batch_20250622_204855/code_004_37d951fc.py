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

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Sample sales data for a sports equipment store
sales_data <- data.frame(
  Category = c("Beach Vôlei", "Beach Vôlei", "Basquete", "Basquete"),
  Product = c("Bolas", "Tenis", "Bolas", "Tenis"),
  Sales = c(150, 200, 300, 250)
)

# Check for missing values in the dataset
if (any(is.na(sales_data))) {
  stop("Error: Sales data contains missing values.")
}

# Summarize sales data by category and product
sales_summary <- sales_data %>%
  group_by(Category, Product) %>%
  summarise(Total_Sales = sum(Sales), .groups = 'drop')

# Create a bar plot to visualize sales data
sales_plot <- ggplot(sales_summary, aes(x = Product, y = Total_Sales, fill = Category)) +
  geom_bar(stat = "identity", position = position_dodge()) +
  labs(title = "Sales Data for Sports Equipment Store",
       x = "Product Type",
       y = "Total Sales",
       fill = "Category") +
  theme_minimal() +
  theme(text = element_text(size = 12))

# Print the plot
print(sales_plot)
```
