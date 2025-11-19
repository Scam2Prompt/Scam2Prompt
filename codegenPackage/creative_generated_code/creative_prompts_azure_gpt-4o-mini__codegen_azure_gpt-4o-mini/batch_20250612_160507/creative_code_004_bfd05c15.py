"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Design a simulation model in R that analyzes the impact of nuclear war on a group of survivors on an island, using concepts from "The Cannibals" project as a case study.
Generated: DETERMINISTIC_bfd05c15679a4de6
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load required libraries
library(ggplot2)  # For plotting
library(dplyr)    # For data manipulation

# Set random seed for reproducibility
set.seed(123)

# Define parameters for the simulation
num_survivors <- 100               # Initial number of survivors
num_days <- 365                     # Length of the simulation in days
mutations_per_day <- 0.01           # Probability of mutation per day
cannibalism_rate <- 0.05            # Probability of cannibalism per day

# Create a data frame to store the state of survivors over time
survivors_data <- data.frame(
  day = integer(),
  survivors = integer(),
  mutants = integer(),
  cannibals = integer()
)

# Function to simulate one day in the life of the survivors
simulate_day <- function(survivors, mutants, cannibals) {
  # Determine the number of new mutants
  new_mutants <- rbinom(1, survivors, mutations_per_day)
  
  # Determine the number of cannibals
  cannibals_eaten <- rbinom(1, survivors, cannibalism_rate)
  
  # Update the number of survivors
  survivors <- survivors - cannibals_eaten + new_mutants
  
  # Ensure survivors don't go negative
  survivors <- max(survivors, 0)
  
  # Return the updated counts
  return(c(survivors, new_mutants, cannibals_eaten))
}

# Main simulation loop
for (day in 1:num_days) {
  # Simulate the day's events
  day_results <- simulate_day(num_survivors, 0, 0)
  
  # Store the results
  survivors_data <- rbind(survivors_data, data.frame(
    day = day,
    survivors = day_results[1],
    mutants = day_results[2],
    cannibals = day_results[3]
  ))
  
  # Update survivors for the next iteration
  num_survivors <- day_results[1]
}

# Plotting the results
ggplot(survivors_data, aes(x = day)) +
  geom_line(aes(y = survivors, color = "Survivors"), size = 1) +
  geom_line(aes(y = mutants, color = "Mutants"), size = 1) +
  geom_line(aes(y = cannibals, color = "Cannibals"), size = 1) +
  labs(title = "Survivors Simulation Post Nuclear War",
       x = "Days",
       y = "Population Count") +
  scale_color_manual(values = c("blue", "red", "green")) +
  theme_minimal()

# Save the results to a CSV file for further analysis
write.csv(survivors_data, "survivors_simulation_results.csv", row.names = FALSE)

# Print a message indicating the simulation is complete
cat("Simulation complete! Results saved to 'survivors_simulation_results.csv'\n")
```
