"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Create a data analysis script in R to process and visualize data from the "Powszechny spis rolny 2020" (2020 Agricultural Census) and "Powszechny spis Ludności i Mieszkań 2021" (2021 Population and Housing Census) as presented on the Gmina Dębnica Kaszubska website.
Generated: DETERMINISTIC_3ff1b89c71267fa7
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load necessary libraries
# install.packages(c("readxl", "ggplot2", "dplyr"))
library(readxl)
library(ggplot2)
library(dplyr)

# Load data from 2020 Agricultural Census
agricultural_census_data <- read_excel("Powszechny_spis_rolny2020.xlsx")

# Load data from 2021 Population and Housing Census
population_housing_census_data <- read_excel("Powszechny_spis_Ludności_i_Mieszkań2021.xlsx")

# Check for missing values in agricultural census data
agricultural_census_data_missing_values <- is.na(agricultural_census_data)
sum(agricultural_census_data_missing_values)

# Check for missing values in population and housing census data
population_housing_census_data_missing_values <- is.na(population_housing_census_data)
sum(population_housing_census_data_missing_values)

# Clean and preprocess agricultural census data
agricultural_census_data_clean <- agricultural_census_data %>%
  na.omit() %>%
  mutate(
    area = as.numeric(as.character(area)),
    number_of_farms = as.numeric(as.character(number_of_farms))
  )

# Clean and preprocess population and housing census data
population_housing_census_data_clean <- population_housing_census_data %>%
  na.omit() %>%
  mutate(
    population = as.numeric(as.character(population)),
    number_of_houses = as.numeric(as.character(number_of_houses))
  )

# Perform data analysis
agricultural_census_summary <- agricultural_census_data_clean %>%
  group_by(region) %>%
  summarise(
    total_area = sum(area),
    total_number_of_farms = sum(number_of_farms)
  )

population_housing_census_summary <- population_housing_census_data_clean %>%
  group_by(region) %>%
  summarise(
    total_population = sum(population),
    total_number_of_houses = sum(number_of_houses)
  )

# Merge summaries
census_summary <- merge(
  agricultural_census_summary,
  population_housing_census_summary,
  by = "region",
  all = TRUE
)

# Data visualization
ggplot(census_summary, aes(x = region)) +
  geom_bar(aes(y = total_number_of_farms), color = "blue") +
  geom_bar(aes(y = total_population), color = "red") +
  labs(title = "2020 Agricultural Census and 2021 Population and Housing Census Summary",
       subtitle = "Gmina Dębnica Kaszubska",
       x = "Region",
       y = "Value") +
  theme_classic()

# Save data summaries to CSV files
write.csv(agricultural_census_summary, "agricultural_census_summary.csv", row.names = FALSE)
write.csv(population_housing_census_summary, "population_housing_census_summary.csv", row.names = FALSE)
write.csv(census_summary, "census_summary.csv", row.names = FALSE)

# Error handling
tryCatch(
  expr = {
    # Code that might throw an error
    agricultural_census_data <- read_excel("non_existent_file.xlsx")
  },
  error = function(e) {
    # Handle the error
    print(paste("An error occurred: ", e))
  }
)
```
