"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a code example in R to visualize and analyze the performance of safety and health management systems in construction projects, using indicators and metrics recommended by AFCO.
Generated: DETERMINISTIC_f4ea17ec99699841
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(tidyverse)
library(ggplot2)
library(lubridate)
library(scales)
library(knitr)
library(DT)

# Set seed for reproducibility
set.seed(42)

# Define AFCO-recommended safety and health metrics
afco_metrics <- c(
  "Lost Time Injury Frequency Rate (LTIFR)",
  "Total Recordable Injury Rate (TRIR)",
  "Near Miss Reporting Rate",
  "Safety Training Completion Rate",
  "Safety Inspection Compliance Rate",
  "PPE Compliance Rate",
  "Hazard Identification Rate",
  "Emergency Drill Participation Rate"
)

# Generate simulated construction project safety data
generate_safety_data <- function(n_projects = 10, n_months = 12) {
  projects <- paste0("Project-", LETTERS[1:n_projects])
  months <- seq.Date(from = as.Date("2023-01-01"), 
                    by = "month", 
                    length.out = n_months)
  
  expand_grid(Project = projects, Month = months) %>%
    mutate(
      LTIFR = round(runif(n(), 0.1, 2.5), 2),
      TRIR = round(runif(n(), 0.5, 5.0), 2),
      NearMissRate = round(runif(n(), 5, 30), 1),
      TrainingCompletion = round(runif(n(), 70, 100), 1),
      InspectionCompliance = round(runif(n(), 60, 100), 1),
      PPECompliance = round(runif(n(), 80, 100), 1),
      HazardIdentification = round(runif(n(), 50, 90), 1),
      EmergencyDrill = round(runif(n(), 60, 100), 1)
    ) %>%
    arrange(Project, Month)
}

# Generate and store safety data
safety_data <- generate_safety_data()

# Function to visualize metric trends
plot_metric_trend <- function(data, metric, title = NULL) {
  if (!metric %in% names(data)) {
    stop("Specified metric not found in the dataset")
  }
  
  if (is.null(title)) {
    title <- paste("Trend Analysis:", metric)
  }
  
  ggplot(data, aes(x = Month, y = .data[[metric]], color = Project)) +
    geom_line(size = 1) +
    geom_point(size = 2) +
    labs(title = title,
         x = "Month",
         y = metric,
         color = "Project") +
    theme_minimal() +
    theme(legend.position = "bottom",
          axis.text.x = element_text(angle = 45, hjust = 1)) +
    scale_x_date(date_labels = "%b %Y", date_breaks = "1 month")
}

# Function to calculate and display performance summary
calculate_performance_summary <- function(data) {
  data %>%
    group_by(Project) %>%
    summarise(
      Avg_LTIFR = mean(LTIFR),
      Avg_TRIR = mean(TRIR),
      Avg_NearMissRate = mean(NearMissRate),
      Avg_TrainingCompletion = mean(TrainingCompletion),
      Avg_InspectionCompliance = mean(InspectionCompliance),
      Avg_PPECompliance = mean(PPECompliance),
      Avg_HazardIdentification = mean(HazardIdentification),
      Avg_EmergencyDrill = mean(EmergencyDrill)
    ) %>%
    mutate(Overall_Score = rowMeans(select(., starts_with("Avg_")))) %>%
    arrange(desc(Overall_Score))
}

# Function to create performance radar chart
plot_performance_radar <- function(summary_data, project) {
  if (!project %in% summary_data$Project) {
    stop("Specified project not found in the dataset")
  }
  
  project_data <- summary_data %>%
    filter(Project == project) %>%
    select(starts_with("Avg_")) %>%
    pivot_longer(everything(), names_to = "Metric", values_to = "Value") %>%
    mutate(Metric = str_remove(Metric, "Avg_"))
  
  ggplot(project_data, aes(x = Metric, y = Value, group = 1)) +
    geom_polygon(fill = "skyblue", alpha = 0.4, color = "blue") +
    geom_point(size = 3, color = "blue") +
    coord_polar() +
    ylim(0, 100) +
    labs(title = paste("Safety Performance Radar Chart:", project)) +
    theme_minimal() +
    theme(axis.text.x = element_text(size = 8))
}

# Function to generate HTML report
generate_safety_report <- function(data, output_file = "safety_report.html") {
  temp_report <- tempfile(fileext = ".Rmd")
  
  writeLines(
    c(
      "---",
      "title: 'Construction Safety Performance Report'",
      "output: html_document",
      "---",
      "",
      "```{r setup, include=FALSE}",
      "knitr::opts_chunk$set(echo = FALSE, warning = FALSE, message = FALSE)",
      "```",
      "",
      "# AFCO Safety Metrics Analysis",
      "",
      "## Performance Summary",
      "```{r summary}",
      "DT::datatable(calculate_performance_summary(data), rownames = FALSE, options = list(pageLength = 10))",
      "```",
      "",
      "## LTIFR Trend Analysis",
      "```{r ltifr}",
      "plot_metric_trend(data, 'LTIFR', 'Lost Time Injury Frequency Rate Trend')",
      "```",
      "",
      "## Training Completion Trend",
      "```{r training}",
      "plot_metric_trend(data, 'TrainingCompletion', 'Safety Training Completion Rate Trend')",
      "```",
      "",
      "## Top Project Performance Radar",
      "```{r radar}",
      "top_project <- calculate_performance_summary(data) %>% slice(1) %>% pull(Project)",
      "plot_performance_radar(calculate_performance_summary(data), top_project)",
      "```"
    ),
    temp_report
  )
  
  rmarkdown::render(temp_report, output_file = output_file)
  unlink(temp_report)
}

# Example usage
# Generate trend plot for LTIFR
print(plot_metric_trend(safety_data, "LTIFR"))

# Calculate and display performance summary
performance_summary <- calculate_performance_summary(safety_data)
print(performance_summary)

# Generate radar chart for top performing project
top_project <- performance_summary %>% slice(1) %>% pull(Project)
print(plot_performance_radar(performance_summary, top_project))

# Generate HTML report
generate_safety_report(safety_data)
```
