"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: "Create a function in R to compare different Chevrolet car models' prices and financing options under the Plan de Ahorro."
Generated: DETERMINISTIC_6d6a099f6912fbc3
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Chevrolet Car Models Comparison Function

# Define a function to compare Chevrolet car models' prices and financing options
compare_chevrolet_models <- function(car_models) {
  # Check if input is a data frame
  if (!is.data.frame(car_models)) {
    stop("Input must be a data frame")
  }
  
  # Required columns
  required_columns <- c("Model", "Price", "Down_Payment", "Monthly_Payment", "Interest_Rate")
  
  # Check if required columns exist
  if (!all(required_columns %in% colnames(car_models))) {
    stop("Data frame must contain the following columns: Model, Price, Down_Payment, Monthly_Payment, Interest_Rate")
  }
  
  # Validate data types
  if (!all(sapply(car_models[, c("Price", "Down_Payment", "Monthly_Payment")], function(x) is.numeric(x)))) {
    stop("Price, Down_Payment, and Monthly_Payment must be numeric")
  }
  
  if (!all(sapply(car_models[, "Interest_Rate"], function(x) is.numeric(x) & x >= 0 & x <= 100))) {
    stop("Interest_Rate must be a numeric value between 0 and 100")
  }
  
  # Calculate total cost for each model
  car_models$total_cost <- car_models$Price + (car_models$Monthly_Payment * 60) - car_models$Down_Payment
  
  # Calculate APR for each model
  car_models$apr <- car_models$Interest_Rate / 100
  
  # Sort car models by total cost
  car_models <- car_models[order(car_models$total_cost), ]
  
  return(car_models)
}

# Example usage
chevrolet_models <- data.frame(
  Model = c("Chevrolet Onix", "Chevrolet Cruze", "Chevrolet Tracker"),
  Price = c(20000, 25000, 28000),
  Down_Payment = c(2000, 3000, 3500),
  Monthly_Payment = c(350, 400, 450),
  Interest_Rate = c(6, 8, 10)
)

tryCatch(
  expr = {
    result <- compare_chevrolet_models(chevrolet_models)
    print(result)
  },
  error = function(e) {
    print(paste("An error occurred: ", e$message))
  }
)
```
