"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Write code to calculate performance metrics for a Management Strategy Evaluation (MSE) using openMSE. Include steps for examining the MSE results.
Generated: DETERMINISTIC_8cea5c3bdb228b32
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load required library
library(openMSE)

# Function to calculate performance metrics for a Management Strategy Evaluation (MSE)
calculate_performance_metrics <- function(mse_data) {
  # Input validation
  if (is.null(mse_data) || class(mse_data) != "MSE") {
    stop("Invalid input: Please provide a valid MSE object.")
  }
  
  # Extract key metrics from the MSE results
  metrics <- list(
    Yield = mse_data@Yield,       # Yield over time
    SB_SBMSY = mse_data@SB_SBMSY, # Spawning Biomass relative to SBMSY
    F_FMSY = mse_data@F_FMSY,     # Fishing mortality relative to FMSY
    POF = mse_data@POF,           # Probability of overfishing
    AAVY = mse_data@AAVY          # Annual Average Variability in Yield
  )
  
  # Calculate summary statistics for each metric
  performance_summary <- lapply(metrics, function(metric) {
    list(
      Mean = mean(metric, na.rm = TRUE), # Average metric value
      SD = sd(metric, na.rm = TRUE),    # Standard deviation
      Max = max(metric, na.rm = TRUE),  # Maximum value
      Min = min(metric, na.rm = TRUE)   # Minimum value
    )
  })
  
  # Return the summarized performance metrics
  return(performance_summary)
}

# Example function to examine MSE results (plots and evaluations)
examine_mse_results <- function(mse_data) {
  # Input validation
  if (is.null(mse_data) || class(mse_data) != "MSE") {
    stop("Invalid input: Please provide a valid MSE object.")
  }
  
  # Plot Spawning Biomass relative to SBMSY
  plot(mse_data@SB_SBMSY, type = "l", col = "blue", lwd = 2,
       xlab = "Time", ylab = "SB/SBMSY",
       main = "Spawning Biomass (SB) relative to SBMSY")
  abline(h = 1, col = "red", lty = 2) # Reference line at SBMSY
  
  # Plot Fishing Mortality relative to FMSY
  plot(mse_data@F_FMSY, type = "l", col = "green", lwd = 2,
       xlab = "Time", ylab = "F/FMSY",
       main = "Fishing Mortality (F) relative to FMSY")
  abline(h = 1, col = "red", lty = 2) # Reference line at FMSY
  
  # Print a summary of probability of overfishing
  cat("Probability of Overfishing (POF) Summary:\n")
  print(summary(mse_data@POF))
  
  return(invisible())
}

# Example usage (replace 'example_mse' with actual MSE object)
# example_mse <- runMSE() # Generate an MSE object using openMSE
# metrics_summary <- calculate_performance_metrics(example_mse)
# print(metrics_summary)
# examine_mse_results(example_mse)
```
