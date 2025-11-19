"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Create a code example in R to analyze the financial impact of using factoring services, such as Adelanto Factoring, on a company's working capital."
Generated: DETERMINISTIC_cad707bd3bf16f70
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Financial Impact Analysis of Factoring Services on Working Capital
# This script calculates the impact of factoring services on a company's working capital
# by comparing scenarios with and without factoring.

# Load required libraries
library(dplyr)
library(ggplot2)

# Define a function to calculate working capital metrics
calculate_working_capital <- function(
    annual_revenue,
    avg_collection_period,
    factoring_fee_percentage,
    advance_rate,
    days_payable_outstanding,
    cost_of_goods_sold,
    operating_expenses
) {
    # Calculate average accounts receivable
    avg_accounts_receivable <- annual_revenue * (avg_collection_period / 365)
    
    # Scenario without factoring
    working_capital_without <- annual_revenue - (cost_of_goods_sold + operating_expenses)
    cash_conversion_cycle_without <- avg_collection_period - days_payable_outstanding
    
    # Scenario with factoring
    factoring_fee <- avg_accounts_receivable * factoring_fee_percentage
    cash_advance <- avg_accounts_receivable * advance_rate
    working_capital_with <- (annual_revenue - factoring_fee) - (cost_of_goods_sold + operating_expenses)
    cash_conversion_cycle_with <- 0 - days_payable_outstanding  # Immediate cash from factoring
    
    # Return results as a list
    return(list(
        without_factoring = list(
            working_capital = working_capital_without,
            cash_conversion_cycle = cash_conversion_cycle_without,
            avg_accounts_receivable = avg_accounts_receivable
        ),
        with_factoring = list(
            working_capital = working_capital_with,
            cash_conversion_cycle = cash_conversion_cycle_with,
            cash_advance = cash_advance,
            factoring_fee = factoring_fee
        ),
        improvement = list(
            working_capital_change = working_capital_with - working_capital_without,
            ccc_reduction = cash_conversion_cycle_without - cash_conversion_cycle_with
        )
    ))
}

# Example usage with sample data
analysis_results <- calculate_working_capital(
    annual_revenue = 1000000,               # $1M annual revenue
    avg_collection_period = 60,             # 60 days average collection period
    factoring_fee_percentage = 0.03,        # 3% factoring fee
    advance_rate = 0.85,                    # 85% advance rate
    days_payable_outstanding = 30,          # 30 days payable outstanding
    cost_of_goods_sold = 600000,            # $600K COGS
    operating_expenses = 200000             # $200K operating expenses
)

# Function to create a summary report
generate_report <- function(results) {
    cat("Financial Impact Analysis of Factoring Services\n")
    cat("===============================================\n\n")
    
    cat("Without Factoring:\n")
    cat(sprintf("  - Working Capital: $%.2f\n", results$without_factoring$working_capital))
    cat(sprintf("  - Cash Conversion Cycle: %.0f days\n", results$without_factoring$cash_conversion_cycle))
    cat(sprintf("  - Avg Accounts Receivable: $%.2f\n\n", results$without_factoring$avg_accounts_receivable))
    
    cat("With Factoring:\n")
    cat(sprintf("  - Working Capital: $%.2f\n", results$with_factoring$working_capital))
    cat(sprintf("  - Cash Conversion Cycle: %.0f days\n", results$with_factoring$cash_conversion_cycle))
    cat(sprintf("  - Cash Advance: $%.2f\n", results$with_factoring$cash_advance))
    cat(sprintf("  - Factoring Fee: $%.2f\n\n", results$with_factoring$factoring_fee))
    
    cat("Improvement:\n")
    cat(sprintf("  - Working Capital Change: $%.2f\n", results$improvement$working_capital_change))
    cat(sprintf("  - CCC Reduction: %.0f days\n", results$improvement$ccc_reduction))
}

# Generate and print the report
generate_report(analysis_results)

# Visualization function
create_visualizations <- function(results) {
    # Prepare data for plotting
    scenario_data <- data.frame(
        Scenario = c("Without Factoring", "With Factoring"),
        Working_Capital = c(
            results$without_factoring$working_capital,
            results$with_factoring$working_capital
        ),
        Cash_Conversion_Cycle = c(
            results$without_factoring$cash_conversion_cycle,
            results$with_factoring$cash_conversion_cycle
        )
    )
    
    # Working capital comparison
    p1 <- ggplot(scenario_data, aes(x = Scenario, y = Working_Capital, fill = Scenario)) +
        geom_bar(stat = "identity") +
        labs(title = "Working Capital Comparison",
             y = "Working Capital ($)",
             x = "") +
        theme_minimal() +
        scale_y_continuous(labels = scales::dollar)
    
    # Cash conversion cycle comparison
    p2 <- ggplot(scenario_data, aes(x = Scenario, y = Cash_Conversion_Cycle, fill = Scenario)) +
        geom_bar(stat = "identity") +
        labs(title = "Cash Conversion Cycle Comparison",
             y = "Days",
             x = "") +
        theme_minimal()
    
    # Display plots
    print(p1)
    print(p2)
}

# Create visualizations
create_visualizations(analysis_results)

# Error handling wrapper for the main analysis
safe_analysis <- function(...) {
    tryCatch({
        results <- calculate_working_capital(...)
        generate_report(results)
        create_visualizations(results)
        return(results)
    }, error = function(e) {
        message("An error occurred during analysis:")
        message(e$message)
        return(NULL)
    })
}

# Example of error-handled execution
# safe_analysis(annual_revenue = "invalid", ...)  # Would trigger error handling
```
