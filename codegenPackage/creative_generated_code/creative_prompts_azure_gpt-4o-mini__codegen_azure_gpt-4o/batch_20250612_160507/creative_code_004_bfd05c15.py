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

```R
# Simulation Model for Survivors on an Island After a Nuclear War
# Inspired by concepts from "The Cannibals" project

# Load necessary library
library(dplyr)

# Set seed for reproducibility
set.seed(42)

# Define parameters
initial_population <- 100  # Number of survivors
simulation_days <- 365     # Length of the simulation (1 year)
initial_resources <- 1000  # Units of food/resources available at the start
resource_replenishment_rate <- 10  # Resources replenished daily
consumption_per_person <- 1  # Resources consumed per person per day
mortality_rate <- 0.01  # Daily mortality rate due to various causes
cannibalism_trigger_threshold <- 200  # Threshold below which cannibalism may start

# Initialize survivors data frame
survivors <- data.frame(
  id = 1:initial_population,
  health = runif(initial_population, 50, 100),  # Random health values between 50 and 100
  status = "alive"  # All survivors start as "alive"
)

# Function to simulate one day
simulate_day <- function(day, resources, survivors) {
  # Print the current day
  message("Day ", day)
  
  # Reduce resources based on consumption
  daily_consumption <- sum(survivors$status == "alive") * consumption_per_person
  resources <- resources - daily_consumption
  
  # Check if resources are below the cannibalism trigger threshold
  if (resources < cannibalism_trigger_threshold) {
    message("Resources below threshold. Cannibalism may occur.")
    # Cannibalism simulation: Randomly remove one survivor if resources are insufficient
    alive_survivors <- survivors %>% filter(status == "alive")
    if (nrow(alive_survivors) > 1) {
      cannibal_victim <- sample(alive_survivors$id, 1)
      survivors$status[survivors$id == cannibal_victim] <- "dead (cannibalism)"
      message("Cannibalism occurred. Survivor ", cannibal_victim, " was consumed.")
      resources <- resources + 10  # Cannibalism replenishes some resources
    }
  }
  
  # Apply daily mortality rate
  mortality_count <- sum(survivors$status == "alive") * mortality_rate
  if (mortality_count > 0) {
    dead_survivors <- sample(survivors %>% filter(status == "alive") %>% pull(id), ceiling(mortality_count))
    survivors$status[survivors$id %in% dead_survivors] <- "dead (mortality)"
    message("Mortality occurred. ", length(dead_survivors), " survivors died.")
  }
  
  # Replenish resources
  resources <- resources + resource_replenishment_rate
  
  # Update survivors' health
  survivors <- survivors %>% mutate(
    health = ifelse(status == "alive", health - runif(n(), 0, 5), health)  # Health decreases daily
  )
  survivors$health <- pmax(survivors$health, 0)  # Ensure health does not drop below 0
  
  # Check for survivors who died due to health reaching 0
  survivors$status[survivors$health == 0 & survivors$status == "alive"] <- "dead (health)"
  
  # Return updated survivors and resources
  list(resources = resources, survivors = survivors)
}

# Run the simulation
resources <- initial_resources
for (day in 1:simulation_days) {
  simulation_result <- simulate_day(day, resources, survivors)
  resources <- simulation_result$resources
  survivors <- simulation_result$survivors
  
  # End simulation if all survivors are dead
  if (all(survivors$status != "alive")) {
    message("Simulation ended early. All survivors are dead.")
    break
  }
}

# Final summary
message("Simulation completed.")
message("Final resources: ", resources)
message("Survivors summary:")
print(survivors %>% group_by(status) %>% summarise(count = n()))
```
