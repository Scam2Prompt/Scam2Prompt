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
# Nuclear War Survival Simulation Model

# Load required libraries
library(ggplot2)
library(dplyr)

# Define a function to simulate the impact of nuclear war on survivors
simulate_nuclear_war <- function(
  population_size,
  island_area,
  food_availability,
  water_availability,
  medical_supplies,
  days_to_simulate
) {
  # Initialize a data frame to store simulation results
  survivors <- data.frame(
    day = numeric(),
    population = numeric(),
    hunger = numeric(),
    thirst = numeric(),
    health = numeric()
  )

  # Initialize survivor population
  population <- population_size
  hunger <- 0
  thirst <- 0
  health <- 100

  # Simulate each day
  for (day in 1:days_to_simulate) {
    # Update hunger and thirst levels
    hunger <- hunger + 10
    thirst <- thirst + 10

    # Update health based on hunger and thirst levels
    health <- health - (hunger / 100) - (thirst / 100)

    # Update population based on health
    population <- population - (population * (1 - (health / 100)))

    # Update food and water availability
    food_availability <- food_availability - (population * 0.1)
    water_availability <- water_availability - (population * 0.1)

    # Check for medical supply usage
    if (medical_supplies > 0) {
      health <- health + 5
      medical_supplies <- medical_supplies - 1
    }

    # Check for survival conditions
    if (population <= 0 | food_availability <= 0 | water_availability <= 0) {
      break
    }

    # Store simulation results
    survivors <- rbind(survivors, data.frame(
      day = day,
      population = population,
      hunger = hunger,
      thirst = thirst,
      health = health
    ))
  }

  return(survivors)
}

# Define a function to plot simulation results
plot_simulation_results <- function(survivors) {
  # Create a ggplot object
  ggplot(survivors, aes(x = day)) +
    geom_line(aes(y = population, color = "Population")) +
    geom_line(aes(y = health, color = "Health")) +
    geom_line(aes(y = hunger, color = "Hunger")) +
    geom_line(aes(y = thirst, color = "Thirst")) +
    labs(title = "Nuclear War Survival Simulation", x = "Day", y = "Value") +
    theme_classic()
}

# Run the simulation
set.seed(123)
simulation_results <- simulate_nuclear_war(
  population_size = 1000,
  island_area = 100,
  food_availability = 1000,
  water_availability = 1000,
  medical_supplies = 100,
  days_to_simulate = 100
)

# Plot the simulation results
plot_simulation_results(simulation_results)

# Print summary statistics
summary_stats <- simulation_results %>%
  summarise(
    average_population = mean(population),
    average_health = mean(health),
    average_hunger = mean(hunger),
    average_thirst = mean(thirst)
  )
print(summary_stats)
```
