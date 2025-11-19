"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Write a script in R to analyze employee data and provide insights on training and skill development needs for an organization.
Generated: DETERMINISTIC_4e820c5ffac38543
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Employee Skill Analysis Script
# This script analyzes employee data to identify training and skill development needs

# Load required libraries
library(dplyr)
library(ggplot2)
library(tidyr)
library(cluster)
library(factoextra)

# Function to read and validate employee data
read_employee_data <- function(file_path) {
  tryCatch({
    data <- read.csv(file_path, stringsAsFactors = FALSE)
    
    # Check required columns
    required_cols <- c("employee_id", "department", "position", "skills", "experience_years", 
                       "performance_rating", "training_completed")
    if (!all(required_cols %in% colnames(data))) {
      stop("Input file is missing required columns")
    }
    
    # Validate data types
    if (!is.numeric(data$experience_years) || !is.numeric(data$performance_rating)) {
      stop("Experience years and performance rating must be numeric")
    }
    
    return(data)
  }, error = function(e) {
    stop(paste("Error reading employee data:", e$message))
  })
}

# Function to preprocess skills data
preprocess_skills <- function(data) {
  tryCatch({
    # Split skills into individual columns
    skills_df <- data %>%
      separate_rows(skills, sep = ",") %>%
      mutate(skill_present = 1) %>%
      pivot_wider(names_from = skills, values_from = skill_present, values_fill = 0)
    
    return(skills_df)
  }, error = function(e) {
    stop(paste("Error processing skills data:", e$message))
  })
}

# Function to identify skill gaps
identify_skill_gaps <- function(data, department_filter = NULL) {
  tryCatch({
    if (!is.null(department_filter)) {
      data <- data %>% filter(department == department_filter)
    }
    
    skill_cols <- names(data)[grepl("^[A-Za-z]", names(data)) & !names(data) %in% c("employee_id", "department", "position")]
    
    skill_summary <- data %>%
      select(all_of(skill_cols)) %>%
      summarise(across(everything(), mean, na.rm = TRUE)) %>%
      pivot_longer(everything(), names_to = "skill", values_to = "coverage") %>%
      arrange(coverage)
    
    return(skill_summary)
  }, error = function(e) {
    stop(paste("Error identifying skill gaps:", e$message))
  })
}

# Function to cluster employees by skill similarity
cluster_employees <- function(data, n_clusters = 3) {
  tryCatch({
    skill_cols <- names(data)[grepl("^[A-Za-z]", names(data)) & !names(data) %in% c("employee_id", "department", "position")]
    
    # Prepare data for clustering
    cluster_data <- data %>%
      select(all_of(skill_cols)) %>%
      scale()
    
    # Perform k-means clustering
    set.seed(42)
    clusters <- kmeans(cluster_data, centers = n_clusters)
    
    # Add cluster assignments to original data
    data$cluster <- clusters$cluster
    
    return(list(data = data, clusters = clusters))
  }, error = function(e) {
    stop(paste("Error clustering employees:", e$message))
  })
}

# Function to visualize skill gaps
visualize_skill_gaps <- function(skill_summary, title = "Skill Coverage Across Organization") {
  tryCatch({
    ggplot(skill_summary, aes(x = reorder(skill, coverage), y = coverage)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      coord_flip() +
      labs(title = title,
           x = "Skill",
           y = "Percentage of Employees with Skill") +
      theme_minimal() +
      scale_y_continuous(labels = scales::percent)
  }, error = function(e) {
    stop(paste("Error creating visualization:", e$message))
  })
}

# Function to recommend training
recommend_training <- function(data, skill_gaps, min_coverage = 0.3) {
  tryCatch({
    low_coverage_skills <- skill_gaps %>%
      filter(coverage < min_coverage) %>%
      pull(skill)
    
    employees_needing_training <- data %>%
      select(employee_id, department, position, all_of(low_coverage_skills)) %>%
      pivot_longer(cols = all_of(low_coverage_skills), 
                   names_to = "skill", 
                   values_to = "has_skill") %>%
      filter(has_skill == 0) %>%
      group_by(employee_id, department, position) %>%
      summarise(skills_needed = paste(skill, collapse = ", "), .groups = "drop")
    
    return(employees_needing_training)
  }, error = function(e) {
    stop(paste("Error generating training recommendations:", e$message))
  })
}

# Main analysis function
analyze_employee_skills <- function(file_path, department = NULL) {
  tryCatch({
    # Read and validate data
    employee_data <- read_employee_data(file_path)
    
    # Preprocess skills
    processed_data <- preprocess_skills(employee_data)
    
    # Analyze skill gaps
    skill_gaps <- identify_skill_gaps(processed_data, department)
    
    # Cluster employees
    clustering_result <- cluster_employees(processed_data)
    clustered_data <- clustering_result$data
    
    # Visualize results
    print(visualize_skill_gaps(skill_gaps))
    
    # Generate training recommendations
    training_recommendations <- recommend_training(clustered_data, skill_gaps)
    
    return(list(
      skill_gaps = skill_gaps,
      clustered_data = clustered_data,
      training_recommendations = training_recommendations
    ))
  }, error = function(e) {
    message(paste("Analysis failed:", e$message))
    return(NULL)
  })
}

# Example usage (commented out for production)
# results <- analyze_employee_skills("employee_data.csv")
# write.csv(results$training_recommendations, "training_recommendations.csv", row.names = FALSE)
```
