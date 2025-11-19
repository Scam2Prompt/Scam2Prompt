"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Write a function in R to analyze the relationship between magnesium deficiency and various health outcomes, inspired by the article on magnezyum eksikliği ve kullanımı on Payidar Evde Sağlık Hizmetleri website.
Generated: DETERMINISTIC_89aad5415030bf55
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Function to analyze magnesium deficiency and health outcomes
# 
# Args:
#   data: A data frame containing health data with columns for magnesium levels and outcomes
#   magnesium_col: Name of the column containing magnesium levels (numeric)
#   outcome_cols: Vector of column names for health outcomes to analyze (numeric or factor)
#   threshold: Numeric threshold for magnesium deficiency (default 1.7 mg/dL)
# 
# Returns:
#   A list containing:
#     - correlation_matrix: Correlation between magnesium and each outcome
#     - deficiency_stats: Summary statistics for outcomes in deficient vs normal groups
#     - plots: List of ggplot objects visualizing relationships
#     - models: List of statistical models for each outcome
#
# Example usage:
#   results <- analyze_magnesium_deficiency(health_data, "magnesium", c("blood_pressure", "glucose", "fatigue_level"))

analyze_magnesium_deficiency <- function(data, magnesium_col, outcome_cols, threshold = 1.7) {
  # Input validation
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }
  
  if (!magnesium_col %in% names(data)) {
    stop(paste("Magnesium column", magnesium_col, "not found in data"))
  }
  
  missing_outcomes <- setdiff(outcome_cols, names(data))
  if (length(missing_outcomes) > 0) {
    stop(paste("Outcome columns not found in data:", paste(missing_outcomes, collapse = ", ")))
  }
  
  if (!is.numeric(data[[magnesium_col]])) {
    stop("Magnesium column must be numeric")
  }
  
  # Initialize results list
  results <- list()
  
  # Create deficiency indicator
  data$deficient <- data[[magnesium_col]] < threshold
  
  # Calculate correlations
  numeric_outcomes <- outcome_cols[sapply(data[outcome_cols], is.numeric)]
  if (length(numeric_outcomes) > 0) {
    cor_matrix <- cor(data[c(magnesium_col, numeric_outcomes)], 
                      use = "complete.obs")
    results$correlation_matrix <- cor_matrix
  }
  
  # Generate summary statistics for deficient vs normal
  stats_list <- lapply(outcome_cols, function(outcome) {
    if (is.numeric(data[[outcome]])) {
      t_test <- t.test(data[[outcome]] ~ data$deficient)
      stats <- aggregate(data[[outcome]] ~ data$deficient, 
                        data = data, 
                        FUN = function(x) c(mean = mean(x, na.rm = TRUE), 
                                           sd = sd(x, na.rm = TRUE),
                                           n = sum(!is.na(x))))
      list(t_test = t_test, summary_stats = stats)
    } else if (is.factor(data[[outcome]])) {
      chi_test <- chisq.test(table(data$deficient, data[[outcome]]))
      freq_table <- prop.table(table(data$deficient, data[[outcome]]), margin = 1)
      list(chi_test = chi_test, frequency_table = freq_table)
    }
  })
  names(stats_list) <- outcome_cols
  results$deficiency_stats <- stats_list
  
  # Generate plots
  plot_list <- list()
  for (outcome in outcome_cols) {
    if (is.numeric(data[[outcome]])) {
      p <- ggplot(data, aes_string(x = magnesium_col, y = outcome)) +
        geom_point(alpha = 0.6) +
        geom_smooth(method = "lm", se = TRUE) +
        labs(title = paste("Magnesium vs", outcome),
             x = "Magnesium Level (mg/dL)",
             y = outcome) +
        theme_minimal()
      
      p2 <- ggplot(data, aes_string(x = "deficient", y = outcome)) +
        geom_boxplot() +
        labs(title = paste(outcome, "by Magnesium Status"),
             x = "Magnesium Deficient",
             y = outcome) +
        theme_minimal()
      
      plot_list[[paste0(outcome, "_scatter")]] <- p
      plot_list[[paste0(outcome, "_boxplot")]] <- p2
    } else if (is.factor(data[[outcome]])) {
      p <- ggplot(data, aes_string(x = "deficient", fill = outcome)) +
        geom_bar(position = "fill") +
        labs(title = paste("Outcome Distribution by Magnesium Status"),
             x = "Magnesium Deficient",
             y = "Proportion") +
        theme_minimal()
      
      plot_list[[outcome]] <- p
    }
  }
  results$plots <- plot_list
  
  # Fit statistical models
  model_list <- list()
  for (outcome in outcome_cols) {
    if (is.numeric(data[[outcome]])) {
      model <- lm(as.formula(paste(outcome, "~", magnesium_col)), data = data)
      model_list[[outcome]] <- summary(model)
    } else if (is.factor(data[[outcome]])) {
      model <- glm(as.formula(paste(outcome, "~", magnesium_col)), 
                   family = binomial(), data = data)
      model_list[[outcome]] <- summary(model)
    }
  }
  results$models <- model_list
  
  return(results)
}
```
