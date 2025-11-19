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
# Inspired by "The Cannibals" project case study

# Load required libraries
library(tidyverse)
library(deSolve)
library(ggplot2)
library(scales)

# Set random seed for reproducibility
set.seed(42)

# Define simulation parameters
simulation_params <- list(
  initial_population = 1000,
  initial_resources = 5000,  # kg of food
  radiation_decay_rate = 0.01,  # per day
  initial_radiation = 1000,  # arbitrary units
  resource_regeneration_rate = 0.005,  # per day
  daily_food_need = 1.5,  # kg per person per day
  mutation_rate = 0.001,  # probability of mutation per birth
  mutation_effect = 0.1,  # effect size of mutation (can be positive or negative)
  simulation_days = 365,
  time_step = 1  # days
)

# Define population classes
population_classes <- c(
  "healthy" = 0.7,
  "injured" = 0.2,
  "radiation_sick" = 0.1
)

# Define helper functions
calculate_radiation_exposure <- function(current_radiation, population) {
  exposure_risk <- current_radiation / (population + 1)  # +1 to avoid division by zero
  pmin(exposure_risk, 1)  # Cap at 100% risk
}

calculate_mortality <- function(population, resources, current_radiation) {
  base_mortality <- 0.001  # Base daily mortality rate
  starvation_effect <- pmax(0, 1 - (resources / (population * simulation_params$daily_food_need)))
  radiation_effect <- current_radiation / 1000  # Scale radiation effect
  
  mortality_rate <- base_mortality + 
    (0.05 * starvation_effect) + 
    (0.1 * radiation_effect)
  
  pmin(mortality_rate, 0.3)  # Cap mortality at 30% per day
}

calculate_birth_rate <- function(population, resources) {
  base_birth_rate <- 0.002  # Base daily birth rate
  resource_effect <- resources / (population * simulation_params$daily_food_need)
  
  birth_rate <- base_birth_rate * pmin(resource_effect, 2)  # Cap positive effect at 2x
  pmax(birth_rate, 0)  # Ensure non-negative
}

# Define differential equations for the simulation
survival_model <- function(time, state, params) {
  with(as.list(c(state, params)), {
    # Calculate current totals
    total_population <- healthy + injured + radiation_sick
    
    # Calculate rates
    radiation_exposure <- calculate_radiation_exposure(radiation, total_population)
    mortality_rate <- calculate_mortality(total_population, resources, radiation)
    birth_rate <- calculate_birth_rate(total_population, resources)
    
    # Population changes
    dhealthy <- (birth_rate * total_population * (1 - params$mutation_rate)) - 
      (mortality_rate * healthy) - 
      (radiation_exposure * healthy * 0.1)
    
    dinjured <- (birth_rate * total_population * params$mutation_rate * abs(params$mutation_effect)) - 
      (mortality_rate * injured * 1.5) + 
      (radiation_exposure * healthy * 0.05)
    
    dradiation_sick <- (radiation_exposure * healthy * 0.05) - 
      (mortality_rate * radiation_sick * 2)
    
    # Resource changes
    dresources <- (params$resource_regeneration_rate * resources) - 
      (total_population * params$daily_food_need)
    
    # Radiation decay
    dradiation <- -params$radiation_decay_rate * radiation
    
    # Return rates of change
    list(c(dhealthy, dinjured, dradiation_sick, dresources, dradiation))
  })
}

# Initialize simulation state
initial_state <- c(
  healthy = simulation_params$initial_population * population_classes["healthy"],
  injured = simulation_params$initial_population * population_classes["injured"],
  radiation_sick = simulation_params$initial_population * population_classes["radiation_sick"],
  resources = simulation_params$initial_resources,
  radiation = simulation_params$initial_radiation
)

# Run simulation
times <- seq(0, simulation_params$simulation_days, by = simulation_params$time_step)
simulation_results <- ode(
  y = initial_state,
  times = times,
  func = survival_model,
  parms = simulation_params
) %>% 
  as.data.frame()

# Process results
results_df <- simulation_results %>%
  mutate(
    total_population = healthy + injured + radiation_sick,
    day = time,
    resource_ratio = resources / (total_population * simulation_params$daily_food_need),
    radiation_risk = calculate_radiation_exposure(radiation, total_population)
  ) %>%
  select(day, healthy, injured, radiation_sick, total_population, resources, radiation, resource_ratio, radiation_risk)

# Visualization functions
plot_population_trends <- function(results) {
  ggplot(results, aes(x = day)) +
    geom_line(aes(y = healthy, color = "Healthy"), size = 1) +
    geom_line(aes(y = injured, color = "Injured"), size = 1) +
    geom_line(aes(y = radiation_sick, color = "Radiation Sick"), size = 1) +
    geom_line(aes(y = total_population, color = "Total"), size = 1.5, linetype = "dashed") +
    labs(title = "Population Trends After Nuclear War",
         x = "Days Since Event",
         y = "Population Count",
         color = "Population Group") +
    scale_color_manual(values = c("Healthy" = "darkgreen", 
                                 "Injured" = "orange", 
                                 "Radiation Sick" = "red", 
                                 "Total" = "black")) +
    theme_minimal() +
    scale_y_continuous(labels = comma)
}

plot_resources_vs_population <- function(results) {
  ggplot(results, aes(x = day)) +
    geom_line(aes(y = resources, color = "Resources"), size = 1) +
    geom_line(aes(y = total_population * simulation_params$daily_food_need, 
                  color = "Daily Food Need"), size = 1) +
    labs(title = "Resources vs Population Needs",
         x = "Days Since Event",
         y = "Kilograms of Food",
         color = "Metric") +
    scale_color_manual(values = c("Resources" = "blue", 
                                 "Daily Food Need" = "red")) +
    theme_minimal() +
    scale_y_continuous(labels = comma)
}

plot_radiation_risk <- function(results) {
  ggplot(results, aes(x = day, y = radiation_risk)) +
    geom_line(color = "purple", size = 1) +
    labs(title = "Radiation Exposure Risk Over Time",
         x = "Days Since Event",
         y = "Exposure Risk (0-1)") +
    theme_minimal() +
    ylim(0, 1)
}

# Generate plots
population_plot <- plot_population_trends(results_df)
resources_plot <- plot_resources_vs_population(results_df)
radiation_plot <- plot_radiation_risk(results_df)

# Display summary statistics
summary_stats <- results_df %>%
  summarise(
    final_population = last(total_population),
    survival_rate = last(total_population) / simulation_params$initial_population,
    days_until_stable = which(diff(sign(diff(total_population))) == 2)[1],
    min_resources = min(resources),
    max_radiation_risk = max(radiation_risk)
  )

# Save results to CSV
write_csv(results_df, "nuclear_survival_simulation_results.csv")

# Print summary
print(summary_stats)
```
