"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write a code snippet in R to analyze the impact of COVID-19 on the mental health of the population in Oruro, Bolivia, using data from the Colegio de Psicologos de Oruro's support services.
Generated: DETERMINISTIC_818ef5ba2bbf3215
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(tidyverse)
library(lubridate)
library(ggplot2)
library(ggthemes)
library(scales)

# Function to load and preprocess data
load_and_preprocess_data <- function(file_path) {
  tryCatch({
    # Read data
    data <- read_csv(file_path, 
                    col_types = cols(
                      fecha = col_date(format = "%Y-%m-%d"),
                      edad = col_integer(),
                      genero = col_factor(),
                      motivo_consulta = col_factor(),
                      severidad = col_factor(levels = c("leve", "moderado", "grave"))
                    ))
    
    # Data cleaning
    data_clean <- data %>%
      filter(!is.na(fecha), 
             between(edad, 10, 100),
             !is.na(motivo_consulta)) %>%
      mutate(
        mes = floor_date(fecha, "month"),
        pandemia = if_else(fecha >= as.Date("2020-03-01"), "Post-Pandemia", "Pre-Pandemia")
      )
    
    return(data_clean)
  }, error = function(e) {
    message("Error loading or processing data: ", e$message)
    return(NULL)
  })
}

# Function to analyze trends
analyze_trends <- function(data) {
  if (is.null(data)) return(NULL)
  
  tryCatch({
    # Monthly consultation trends
    monthly_trends <- data %>%
      group_by(mes, pandemia) %>%
      summarise(
        total_consultas = n(),
        .groups = "drop"
      )
    
    # Reasons for consultation
    reason_analysis <- data %>%
      group_by(pandemia, motivo_consulta) %>%
      summarise(
        count = n(),
        percentage = n() / nrow(data) * 100,
        .groups = "drop"
      )
    
    # Severity analysis
    severity_analysis <- data %>%
      group_by(pandemia, severidad) %>%
      summarise(
        count = n(),
        .groups = "drop"
      )
    
    return(list(
      monthly_trends = monthly_trends,
      reason_analysis = reason_analysis,
      severity_analysis = severity_analysis
    ))
  }, error = function(e) {
    message("Error analyzing trends: ", e$message)
    return(NULL)
  })
}

# Function to visualize results
visualize_results <- function(analysis_results) {
  if (is.null(analysis_results)) return(NULL)
  
  tryCatch({
    # Monthly trends plot
    p1 <- ggplot(analysis_results$monthly_trends, 
                aes(x = mes, y = total_consultas, color = pandemia)) +
      geom_line(size = 1) +
      geom_point() +
      scale_x_date(date_labels = "%b %Y", date_breaks = "3 months") +
      scale_y_continuous(labels = comma) +
      labs(title = "Tendencias Mensuales de Consultas Psicológicas en Oruro",
           subtitle = "Antes y después de la pandemia de COVID-19",
           x = "Mes",
           y = "Número de consultas",
           color = "Período") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    
    # Reasons for consultation plot
    p2 <- ggplot(analysis_results$reason_analysis, 
                aes(x = reorder(motivo_consulta, -count), y = count, fill = pandemia)) +
      geom_bar(stat = "identity", position = "dodge") +
      labs(title = "Motivos de Consulta Psicológica en Oruro",
           x = "Motivo de consulta",
           y = "Número de casos",
           fill = "Período") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    
    # Severity plot
    p3 <- ggplot(analysis_results$severity_analysis, 
                aes(x = severidad, y = count, fill = pandemia)) +
      geom_bar(stat = "identity", position = "dodge") +
      labs(title = "Severidad de los Casos Psicológicos en Oruro",
           x = "Nivel de severidad",
           y = "Número de casos",
           fill = "Período") +
      theme_minimal()
    
    return(list(monthly_trends_plot = p1, 
                reasons_plot = p2, 
                severity_plot = p3))
  }, error = function(e) {
    message("Error creating visualizations: ", e$message)
    return(NULL)
  })
}

# Main analysis function
analyze_mental_health_impact <- function(file_path) {
  # Load and preprocess data
  data <- load_and_preprocess_data(file_path)
  
  if (is.null(data)) {
    message("Analysis stopped due to data loading issues.")
    return(NULL)
  }
  
  # Analyze trends
  analysis_results <- analyze_trends(data)
  
  if (is.null(analysis_results)) {
    message("Analysis stopped due to processing issues.")
    return(NULL)
  }
  
  # Visualize results
  plots <- visualize_results(analysis_results)
  
  return(list(
    data = data,
    analysis = analysis_results,
    plots = plots
  ))
}

# Example usage (comment out in production)
# result <- analyze_mental_health_impact("path/to/your/data.csv")
# print(result$plots$monthly_trends_plot)
# print(result$plots$reasons_plot)
# print(result$plots$severity_plot)
```
