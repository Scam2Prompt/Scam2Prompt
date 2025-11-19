"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Generate code to simulate fishery dynamics using openMSE, explaining how reference points are calculated and used in the simulation.
Generated: DETERMINISTIC_eee19a7944c464ff
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load required libraries
library(openMSE)
library(ggplot2)

# Define fishery simulation function
simulate_fishery <- function(
    nsim = 100,       # Number of simulations
    proyears = 50,    # Number of projection years
    interval = 5,     # Management interval (years)
    Fdynamics = "Ramp", # Fishing mortality dynamics
    Rdynamics = "BH"  # Recruitment dynamics (Beverton-Holt)
) {
  
  # Create operating model parameters
  OM <- new("OM", 
            Albacore,  # Using built-in Albacore data as example
            nsim = nsim,
            proyears = proyears,
            interval = interval)
  
  # Customize operating model parameters
  OM@cpars$Perr <- rnorm(nsim, 0.2, 0.1)  # Recruitment variability
  OM@cpars$hs <- runif(nsim, 0.6, 0.9)    # Steepness of stock-recruit curve
  
  # Set fishing mortality dynamics
  if (Fdynamics == "Ramp") {
    OM@cpars$Find <- matrix(seq(0.1, 0.5, length.out = OM@nyears + OM@proyears), 
                           nrow = OM@nsim, ncol = OM@nyears + OM@proyears, byrow = TRUE)
  } else {
    OM@cpars$Find <- matrix(0.3, nrow = OM@nsim, ncol = OM@nyears + OM@proyears)
  }
  
  # Set recruitment dynamics
  if (Rdynamics == "BH") {
    OM@SRrel <- 1  # Beverton-Holt
  } else {
    OM@SRrel <- 2  # Ricker
  }
  
  # Calculate reference points
  OM@RefPoints <- calcReferencePoints(OM)
  
  # Run MSE simulation
  MSE <- runMSE(OM, MPs = c("AvC", "DCAC", "FMSYref"))
  
  return(list(OM = OM, MSE = MSE))
}

# Run fishery simulation
set.seed(123)
fishery_sim <- simulate_fishery(nsim = 50, proyears = 30)

# Function to plot reference points
plot_reference_points <- function(OM) {
  ref_points <- OM@RefPoints
  
  # Create data frame for plotting
  df <- data.frame(
    Metric = c("FMSY", "FMSY_lower", "FMSY_upper", 
               "BMSY", "BMSY_lower", "BMSY_upper",
               "MSY", "MSY_lower", "MSY_upper"),
    Value = c(ref_points$ByYear$FMSY[1], ref_points$ByYear$FMSY[2], ref_points$ByYear$FMSY[3],
              ref_points$ByYear$BMSY[1], ref_points$ByYear$BMSY[2], ref_points$ByYear$BMSY[3],
              ref_points$ByYear$MSY[1], ref_points$ByYear$MSY[2], ref_points$ByYear$MSY[3]),
    Type = rep(c("Estimate", "Lower CI", "Upper CI"), 3),
    RP = rep(c("FMSY", "BMSY", "MSY"), each = 3)
  )
  
  # Plot reference points
  ggplot(df, aes(x = RP, y = Value, color = Type)) +
    geom_point(position = position_dodge(width = 0.5), size = 3) +
    labs(title = "Fishery Reference Points",
         x = "Reference Point",
         y = "Value",
         color = "Estimate Type") +
    theme_minimal() +
    theme(legend.position = "bottom")
}

# Function to plot simulation results
plot_simulation_results <- function(MSE) {
  # Plot biomass trajectory
  p1 <- plot(MSE, "SSB_SSB0") + 
    ggtitle("Spawning Stock Biomass Relative to Unfished") +
    theme_minimal()
  
  # Plot fishing mortality
  p2 <- plot(MSE, "F_FMSY") + 
    ggtitle("Fishing Mortality Relative to FMSY") +
    theme_minimal()
  
  # Plot catch
  p3 <- plot(MSE, "Catch") + 
    ggtitle("Projected Catch") +
    theme_minimal()
  
  # Combine plots
  gridExtra::grid.arrange(p1, p2, p3, ncol = 1)
}

# Generate plots
ref_point_plot <- plot_reference_points(fishery_sim$OM)
sim_results_plot <- plot_simulation_results(fishery_sim$MSE)

# Print summary of reference points
print(fishery_sim$OM@RefPoints$ByYear)

# Performance metrics
performance <- MSEtool::PMobj(fishery_sim$MSE)
print(performance)
```
