"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Generate code in R to visualize the distribution of loans across different sectors, such as agriculture, SMEs, and general loans, using data from the Development Bank of Mauritius.
Generated: DETERMINISTIC_fc8fb802ea51d61b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load necessary libraries
# install.packages(c("ggplot2", "dplyr"))
library(ggplot2)
library(dplyr)

# Sample data from the Development Bank of Mauritius
# Replace with actual data source
dbm_loans <- data.frame(
  Sector = c("Agriculture", "SMEs", "General", "Agriculture", "SMEs", "General", 
             "Agriculture", "SMEs", "General", "Agriculture", "SMEs", "General"),
  Loan_Amount = c(100000, 50000, 200000, 80000, 60000, 250000, 
                  120000, 70000, 220000, 90000, 55000, 210000),
  Year = c(2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022, 2023, 2023, 2023)
)

# Group data by sector and calculate total loan amount
sector_loans <- dbm_loans %>%
  group_by(Sector) %>%
  summarise(Total_Loan_Amount = sum(Loan_Amount))

# Visualize distribution of loans across sectors
ggplot(sector_loans, aes(x = Sector, y = Total_Loan_Amount, fill = Sector)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribution of Loans Across Sectors",
       subtitle = "Development Bank of Mauritius",
       x = "Sector",
       y = "Total Loan Amount") +
  theme_classic() +
  theme(legend.position = "none")

# Visualize distribution of loans across sectors over years
sector_year_loans <- dbm_loans %>%
  group_by(Year, Sector) %>%
  summarise(Total_Loan_Amount = sum(Loan_Amount))

ggplot(sector_year_loans, aes(x = Year, y = Total_Loan_Amount, fill = Sector)) +
  geom_bar(stat = "identity", position = position_dodge()) +
  labs(title = "Distribution of Loans Across Sectors Over Years",
       subtitle = "Development Bank of Mauritius",
       x = "Year",
       y = "Total Loan Amount") +
  theme_classic()

# Error handling example
tryCatch(
  expr = {
    # Code that might throw an error
    invalid_data <- data.frame(Sector = c("A", "B", "C"))
    ggplot(invalid_data, aes(x = Sector)) +
      geom_bar()
  },
  error = function(e) {
    # Handle error
    print(paste("An error occurred: ", e$message))
  }
)
```
