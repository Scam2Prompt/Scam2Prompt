"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Generate code to simulate fishery dynamics using openMSE, explaining how reference points are calculated and used in the simulation.
Generated: DETERMINISTIC_eee19a7944c464ff
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```R
# Load the necessary libraries
library(openMSE)

# Set seed for reproducibility
set.seed(123)

# Define the simulation parameters
params <- list(
  # Define the number of years to simulate
  years = 20,
  
  # Define the initial biomass
  B0 = 1000, 
  
  # Define the intrinsic growth rate
  r = 0.2, 
  
  # Define the carrying capacity
  K = 5000,
  
  # Define the natural mortality rate
  M = 0.1,
  
  # Define the fishing mortality rate
  F = 0.2,
  
  # Define the target and limit reference points
  B_target = 0.5 * 5000,  # 50% of carrying capacity
  B_limit = 0.2 * 5000    # 20% of carrying capacity
)

# Function to simulate fishery dynamics
simulate_fishery <- function(params) {
  # Initialize vectors to store biomass and fishing mortality
  biomass <- numeric(params$years)
  fishing_mortality <- numeric(params$years)
  
  # Set initial biomass
  biomass[1] <- params$B0
  
  # Loop through each year to simulate dynamics
  for (year in 2:params$years) {
    # Calculate recruitment using the Ricker model
    recruitment <- biomass[year - 1] * exp(params$r * (1 - biomass[year - 1] / params$K))
    
    # Calculate biomass at the end of the year
    biomass[year] <- biomass[year - 1] + recruitment - (fishing_mortality[year - 1] * biomass[year - 1])
    
    # Set fishing mortality based on target reference point
    if (biomass[year] < params$B_limit) {
      fishing_mortality[year] <- params$M  # Increase fishing mortality if below limit
    } else if (biomass[year] < params$B_target) {
      fishing_mortality[year] <- (params$F * (biomass[year] / params$B_target))  # Reduce fishing mortality to meet target
    } else {
      fishing_mortality[year] <- params$F  # Maintain constant fishing mortality
    }
    
    # Ensure biomass does not fall below zero
    biomass[year] <- max(biomass[year], 0)
  }
  
  return(data.frame(year = 1:params$years, biomass = biomass, fishing_mortality = fishing_mortality))
}

# Run the simulation
fishery_results <- simulate_fishery(params)

# Print the simulation results
print(fishery_results)

# Plot the results for visualization
library(ggplot2)
ggplot(fishery_results, aes(x = year)) +
  geom_line(aes(y = biomass, color = "Biomass")) +
  geom_line(aes(y = fishing_mortality * 100, color = "Fishing Mortality (scaled)")) +  # Scale fishing mortality for better visualization
  labs(title = "Fishery Dynamics Simulation", x = "Year", y = "Biomass / Fishing Mortality") +
  scale_color_manual(values = c("blue", "red")) +
  theme_minimal() +
  theme(legend.title = element_blank())
```

This R code simulates fishery dynamics using the openMSE framework. It calculates reference points based on the carrying capacity and adjusts fishing mortality according to the biomass levels relative to the target and limit reference points. The simulation results are visualized using ggplot2.
