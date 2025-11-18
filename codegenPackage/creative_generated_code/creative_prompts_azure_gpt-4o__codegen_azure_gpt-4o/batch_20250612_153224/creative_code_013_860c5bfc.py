"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a script in R to analyze the profitability of recycling Styrofoam into products like picture frames and crown moldings, using data on recycled EPS demand.
Generated: DETERMINISTIC_860c5bfc30d47477
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# R Script to Analyze the Profitability of Recycling Styrofoam (EPS) into Products
# Products: Picture Frames and Crown Moldings
# Using Demand Data for Recycled EPS

# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# ------------------------------
# STEP 1: Load and Validate Data
# ------------------------------

# Define the file path for the data (update with actual file path)
data_file <- "recycled_eps_demand.csv"

# Try to load the data and handle errors
recycled_eps_data <- tryCatch(
  {
    read.csv(data_file)
  },
  error = function(e) {
    stop("Error: Unable to load data file. Please check the file path and format.")
  }
)

# Validate that required columns exist
required_columns <- c("Product", "Demand", "Production_Cost", "Selling_Price")
if (!all(required_columns %in% colnames(recycled_eps_data))) {
  stop("Error: Missing required columns in the data. Ensure data includes Product, Demand, Production_Cost, Selling_Price.")
}

# ------------------------------
# STEP 2: Calculate Profitability
# ------------------------------

# Add a profitability column
# Profit per unit = Selling Price - Production Cost
recycled_eps_data <- recycled_eps_data %>%
  mutate(Profit_Per_Unit = Selling_Price - Production_Cost)

# Add total profit column (Profit per unit multiplied by demand)
recycled_eps_data <- recycled_eps_data %>%
  mutate(Total_Profit = Profit_Per_Unit * Demand)

# ------------------------------
# STEP 3: Summarize Results
# ------------------------------

# Calculate overall profitability and summarize by product
profit_summary <- recycled_eps_data %>%
  group_by(Product) %>%
  summarize(
    Total_Demand = sum(Demand),
    Average_Production_Cost = mean(Production_Cost),
    Average_Selling_Price = mean(Selling_Price),
    Total_Profit = sum(Total_Profit)
  ) %>%
  arrange(desc(Total_Profit))  # Sort by profitability

# ------------------------------
# STEP 4: Visualize Results
# ------------------------------

# Bar plot of total profit by product
profit_plot <- ggplot(profit_summary, aes(x = Product, y = Total_Profit, fill = Product)) +
  geom_bar(stat = "identity") +
  labs(
    title = "Total Profit by Product",
    x = "Product",
    y = "Total Profit (USD)"
  ) +
  theme_minimal()

# Display the plot
print(profit_plot)

# ------------------------------
# STEP 5: Export Results
# ------------------------------

# Define output file paths
summary_file <- "profitability_summary.csv"

# Save summarized results to a CSV file
write.csv(profit_summary, summary_file, row.names = FALSE)

# ------------------------------
# STEP 6: Final Output
# ------------------------------

# Print summarized results to the console
print(profit_summary)

# Notify user of successful completion
message("Analysis complete! Results saved to 'profitability_summary.csv'.")
```
