"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Write a code snippet in R to analyze the antioxidant properties of Infusión's Mix Chicha, focusing on the role of maíz morado and other ingredients.
Generated: DETERMINISTIC_7698aaa340619f47
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(tidyverse)
library(ggplot2)
library(agricolae)

# Function to calculate antioxidant activity using DPPH assay
calculate_dpph_activity <- function(sample_concentration, absorbance_sample, absorbance_control) {
  # Calculate percentage inhibition
  inhibition_percentage <- ((absorbance_control - absorbance_sample) / absorbance_control) * 100
  
  # Calculate IC50 if possible
  if (length(sample_concentration) > 1 && length(inhibition_percentage) > 1) {
    model <- lm(inhibition_percentage ~ sample_concentration)
    ic50 <- (50 - coef(model)[1]) / coef(model)[2]
  } else {
    ic50 <- NA
  }
  
  return(list(inhibition_percentage = inhibition_percentage, ic50 = ic50))
}

# Function to analyze antioxidant properties of Infusión's Mix Chicha
analyze_antioxidant_properties <- function(data) {
  tryCatch({
    # Validate input data
    if (!all(c("sample", "concentration", "absorbance_sample", "absorbance_control") %in% names(data))) {
      stop("Input data must contain 'sample', 'concentration', 'absorbance_sample', and 'absorbance_control' columns")
    }
    
    # Calculate antioxidant activity for each sample
    results <- data %>%
      group_by(sample) %>%
      summarise(
        dpph_results = list(calculate_dpph_activity(concentration, absorbance_sample, absorbance_control)),
        .groups = 'drop'
      ) %>%
      mutate(
        mean_inhibition = map_dbl(dpph_results, ~mean(.x$inhibition_percentage)),
        ic50 = map_dbl(dpph_results, ~.x$ic50)
      )
    
    # Perform statistical analysis
    anova_result <- aov(mean_inhibition ~ sample, data = results)
    tukey_result <- HSD.test(anova_result, "sample", group = TRUE)
    
    # Prepare visualization data
    plot_data <- results %>%
      select(sample, mean_inhibition) %>%
      arrange(desc(mean_inhibition))
    
    # Create visualization
    antioxidant_plot <- ggplot(plot_data, aes(x = reorder(sample, -mean_inhibition), y = mean_inhibition, fill = sample)) +
      geom_bar(stat = "identity") +
      labs(title = "Antioxidant Activity of Infusión's Mix Chicha Ingredients",
           x = "Ingredient",
           y = "Mean Inhibition Percentage (%)",
           fill = "Ingredient") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    
    return(list(
      results = results,
      statistics = list(anova = anova_result, tukey = tukey_result),
      plot = antioxidant_plot
    ))
  }, error = function(e) {
    message("Error in antioxidant analysis: ", e$message)
    return(NULL)
  })
}

# Example usage with sample data
# sample_data <- data.frame(
#   sample = rep(c("Maíz Morado", "Clavo", "Canela", "Piña"), each = 3),
#   concentration = rep(c(10, 50, 100), 4),
#   absorbance_sample = runif(12, 0.1, 0.8),
#   absorbance_control = runif(12, 0.7, 1.2)
# )
# 
# analysis_results <- analyze_antioxidant_properties(sample_data)
# print(analysis_results$results)
# print(analysis_results$statistics$tukey)
# print(analysis_results$plot)
```
