"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write a function in R to analyze the effectiveness of different disinfectants used in poultry farms, considering factors like the type of disinfectant, concentration, and frequency of use.
Generated: DETERMINISTIC_aa3b30910cd7bca2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Function to analyze disinfectant effectiveness in poultry farms
analyze_disinfectant_effectiveness <- function(data, disinfectant_col, concentration_col, frequency_col, effectiveness_col) {
  # Validate input data
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }
  
  required_cols <- c(disinfectant_col, concentration_col, frequency_col, effectiveness_col)
  missing_cols <- setdiff(required_cols, colnames(data))
  if (length(missing_cols) > 0) {
    stop(paste("Missing required columns:", paste(missing_cols, collapse = ", ")))
  }
  
  # Check for NA values in critical columns
  na_check <- sapply(data[, required_cols], function(x) any(is.na(x)))
  if (any(na_check)) {
    warning(paste("NA values found in columns:", paste(names(na_check)[na_check], collapse = ", ")))
  }
  
  # Convert factors if needed
  if (!is.factor(data[[disinfectant_col]])) {
    data[[disinfectant_col]] <- as.factor(data[[disinfectant_col]])
  }
  
  # Main analysis
  results <- list()
  
  # Summary statistics by disinfectant type
  results$summary_by_disinfectant <- data %>%
    group_by(!!sym(disinfectant_col)) %>%
    summarise(
      avg_effectiveness = mean(!!sym(effectiveness_col), na.rm = TRUE),
      sd_effectiveness = sd(!!sym(effectiveness_col), na.rm = TRUE),
      min_effectiveness = min(!!sym(effectiveness_col), na.rm = TRUE),
      max_effectiveness = max(!!sym(effectiveness_col), na.rm = TRUE),
      n = n()
    )
  
  # ANOVA test for disinfectant type
  anova_formula <- as.formula(paste(effectiveness_col, "~", disinfectant_col))
  anova_result <- aov(anova_formula, data = data)
  results$anova_disinfectant <- summary(anova_result)
  
  # Correlation between concentration and effectiveness
  results$concentration_correlation <- cor.test(
    data[[concentration_col]], 
    data[[effectiveness_col]],
    method = "pearson",
    na.action = na.omit
  )
  
  # Correlation between frequency and effectiveness
  results$frequency_correlation <- cor.test(
    data[[frequency_col]], 
    data[[effectiveness_col]],
    method = "pearson",
    na.action = na.omit
  )
  
  # Linear model with all factors
  lm_formula <- as.formula(paste(
    effectiveness_col, "~", 
    disinfectant_col, "+", 
    concentration_col, "+", 
    frequency_col
  ))
  results$linear_model <- lm(lm_formula, data = data)
  
  # Visualization data
  results$plot_data <- data %>%
    group_by(!!sym(disinfectant_col), !!sym(concentration_col), !!sym(frequency_col)) %>%
    summarise(
      mean_effectiveness = mean(!!sym(effectiveness_col), na.rm = TRUE),
      .groups = "drop"
    )
  
  return(results)
}

# Example usage (commented out):
# sample_data <- data.frame(
#   disinfectant = rep(c("A", "B", "C"), each = 10),
#   concentration = runif(30, 0.5, 5),
#   frequency = sample(1:7, 30, replace = TRUE),
#   effectiveness = rnorm(30, mean = 80, sd = 10)
# )
# 
# analysis_results <- analyze_disinfectant_effectiveness(
#   data = sample_data,
#   disinfectant_col = "disinfectant",
#   concentration_col = "concentration",
#   frequency_col = "frequency",
#   effectiveness_col = "effectiveness"
# )
```
