"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Design a simulation model in R that analyzes the impact of nuclear war on a group of survivors on an island, using concepts from "The Cannibals" project as a case study.
Generated: DETERMINISTIC_bfd05c15679a4de6
Batch ID: 20250612_160507
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

# Set seed for reproducibility
set.seed(123)

# Define parameters for the simulation
num_survivors <- 100  # Initial number of survivors
num_days <- 30        # Number of days to simulate
initial_food <- 500   # Initial food supply
food_consumption_rate <- 2  # Food consumed per survivor per day
food_growth_rate <- 10  # Food growth per day

# Create a data frame to store the simulation results
simulation_results <- data.frame(
  day = integer(),
  survivors = integer(),
  food_supply = integer(),
  status = character()
)

# Function to simulate one day
simulate_day <- function(day, survivors, food_supply) {
  # Calculate food consumption
  total_consumption <- survivors * food_consumption_rate
  
  # Update food supply
  food_supply <- food_supply - total_consumption + food_growth_rate
  
  # Check if food supply is negative
  if (food_supply < 0) {
    # Calculate the number of survivors that can be sustained
    survivors <- max(0, survivors + floor(food_supply / food_consumption_rate))
    food_supply <- 0  # Set food supply to zero if negative
  }
  
  # Determine the status of the group
  if (survivors == 0) {
    status <- "Extinct"
  } else {
    status <- "Surviving"
  }
  
  return(c(day, survivors, food_supply, status))
}

# Run the simulation for the specified number of days
for (day in 1:num_days) {
  # Simulate the day and store results
  result <- simulate_day(day, num_survivors, initial_food)
  simulation_results <- rbind(simulation_results, result)
  
  # Update survivors and food supply for the next day
  num_survivors <- as.integer(result[2])
  initial_food <- as.integer(result[3])
}

# Rename columns for clarity
colnames(simulation_results) <- c("Day", "Survivors", "Food_Supply", "Status")

# Convert Day to numeric and Survivors, Food_Supply to integer
simulation_results$Day <- as.numeric(simulation_results$Day)
simulation_results$Survivors <- as.integer(simulation_results$Survivors)
simulation_results$Food_Supply <- as.integer(simulation_results$Food_Supply)

# Plot the results
ggplot(simulation_results, aes(x = Day)) +
  geom_line(aes(y = Survivors, color = "Survivors"), size = 1) +
  geom_line(aes(y = Food_Supply, color = "Food Supply"), size = 1) +
  scale_y_continuous(sec.axis = sec_axis(~., name = "Food Supply")) +
  labs(title = "Survivors and Food Supply Over Time",
       x = "Days",
       y = "Count",
       color = "Legend") +
  theme_minimal()

# Print the final results
print(simulation_results)
```
