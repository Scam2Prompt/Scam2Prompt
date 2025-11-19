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

```R
# Simulation Model: Impact of Nuclear War on Survivors on an Island
# This model simulates the survival dynamics of a group of survivors on an island
# following a nuclear war. It incorporates resource availability, population dynamics,
# and survival probabilities.

# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Set simulation parameters
set.seed(123)  # For reproducibility
initial_population <- 100  # Initial number of survivors
initial_resources <- 500  # Initial amount of resources (food, water, etc.)
resource_regeneration_rate <- 50  # Resources regenerated per time step
consumption_rate_per_person <- 5  # Resources consumed per person per time step
mortality_rate <- 0.05  # Base mortality rate per time step
cannibalism_threshold <- 0.2  # Resource threshold below which cannibalism occurs
simulation_steps <- 50  # Number of time steps to simulate

# Initialize variables
population <- initial_population
resources <- initial_resources
survivors <- data.frame(
  step = integer(),
  population = integer(),
  resources = integer(),
  deaths = integer(),
  cannibalism_events = integer()
)

# Simulation loop
for (step in 1:simulation_steps) {
  # Calculate resource consumption
  total_consumption <- population * consumption_rate_per_person
  
  # Update resources
  resources <- resources - total_consumption + resource_regeneration_rate
  if (resources < 0) resources <- 0  # Resources cannot be negative
  
  # Calculate deaths due to starvation
  starvation_deaths <- ifelse(resources < population * consumption_rate_per_person, 
                              round((population - resources / consumption_rate_per_person) * mortality_rate), 
                              0)
  
  # Update population
  population <- population - starvation_deaths
  if (population < 0) population <- 0  # Population cannot be negative
  
  # Cannibalism events (if resources are critically low)
  cannibalism_events <- ifelse(resources / (population * consumption_rate_per_person) < cannibalism_threshold, 
                                round(population * 0.1), 
                                0)
  population <- population - cannibalism_events
  
  # Record data for this step
  survivors <- rbind(survivors, data.frame(
    step = step,
    population = population,
    resources = resources,
    deaths = starvation_deaths,
    cannibalism_events = cannibalism_events
  ))
  
  # Stop simulation if population reaches zero
  if (population <= 0) break
}

# Visualization of simulation results
ggplot(survivors, aes(x = step)) +
  geom_line(aes(y = population, color = "Population")) +
  geom_line(aes(y = resources, color = "Resources")) +
  labs(title = "Survival Dynamics on the Island",
       x = "Time Step",
       y = "Count",
       color = "Legend") +
  theme_minimal()

# Print summary of simulation results
print("Simulation Summary:")
print(survivors)
```
