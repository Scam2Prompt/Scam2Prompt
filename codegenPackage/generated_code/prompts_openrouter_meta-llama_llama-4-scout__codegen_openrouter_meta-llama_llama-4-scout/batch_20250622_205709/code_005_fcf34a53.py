"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Write a code example in R to visualize sales trends for different types of agricultural products, such as those sold by Tấn Hưng Việt Nam."
Generated: DETERMINISTIC_fcf34a5315a1ee18
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Import necessary libraries
library(ggplot2)
library(dplyr)

# Sample data for agricultural product sales
# This data can be replaced with actual sales data from Tấn Hưng Việt Nam
product_sales <- data.frame(
  Product = c(rep("Rice", 12), rep("Coffee", 12), rep("Rubber", 12)),
  Month = rep(c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"), 3),
  Sales = c(100, 120, 110, 130, 140, 150, 160, 170, 180, 190, 200, 210,
            50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160,
            200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310)
)

# Group data by product and month, then calculate mean sales
mean_sales <- product_sales %>%
  group_by(Product, Month) %>%
  summarise(Mean_Sales = mean(Sales))

# Create a line plot to visualize sales trends
ggplot(mean_sales, aes(x = Month, y = Mean_Sales, color = Product)) +
  geom_line() +
  geom_point() +
  labs(title = "Monthly Sales Trends for Agricultural Products",
       subtitle = "Tấn Hưng Việt Nam",
       x = "Month",
       y = "Mean Sales") +
  theme_classic()

# Error handling example: Check if data is empty
if (nrow(product_sales) == 0) {
  stop("No sales data available")
}

# Save plot to file
ggsave("sales_trends.png", plot = last_plot(), width = 8, height = 6, dpi = 300)
```
