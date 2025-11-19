"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a function in R to analyze the cost-effectiveness of hiring a licensed armourer for a film production in NSW, considering the potential costs of non-compliance with regulations.
Generated: DETERMINISTIC_e0d1fea3ba626938
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
#' Analyze Cost-Effectiveness of Hiring a Licensed Armourer for Film Production
#'
#' This function evaluates the cost-effectiveness of hiring a licensed armourer versus
#' the potential costs of non-compliance with NSW regulations for film productions.
#'
#' @param licensed_armourer_cost Numeric. Annual cost of hiring a licensed armourer.
#' @param unlicensed_risk_prob Numeric. Probability of non-compliance incident (0-1).
#' @param fine_amount Numeric. Potential fine amount for non-compliance.
#' @param production_delay_cost Numeric. Cost per day of production delay due to incident.
#' @param avg_delay_days Numeric. Average number of delay days if incident occurs.
#' @param legal_fees Numeric. Estimated legal fees if incident occurs.
#' @param insurance_increase Numeric. Annual insurance premium increase after incident.
#' @param reputation_cost Numeric. Estimated reputation damage cost.
#' @param num_productions Numeric. Number of productions per year (default 1).
#' @return A list containing cost comparison and recommendation.
#' @examples
#' result <- analyze_armourer_cost(
#'     licensed_armourer_cost = 80000,
#'     unlicensed_risk_prob = 0.2,
#'     fine_amount = 50000,
#'     production_delay_cost = 10000,
#'     avg_delay_days = 5,
#'     legal_fees = 20000,
#'     insurance_increase = 10000,
#'     reputation_cost = 50000
#' )
analyze_armourer_cost <- function(
    licensed_armourer_cost,
    unlicensed_risk_prob,
    fine_amount,
    production_delay_cost,
    avg_delay_days,
    legal_fees,
    insurance_increase,
    reputation_cost,
    num_productions = 1
) {
    # Input validation
    if (!all(sapply(list(
        licensed_armourer_cost, unlicensed_risk_prob, fine_amount,
        production_delay_cost, avg_delay_days, legal_fees,
        insurance_increase, reputation_cost, num_productions
    ), is.numeric))) {
        stop("All inputs must be numeric values")
    }
    
    if (unlicensed_risk_prob < 0 || unlicensed_risk_prob > 1) {
        stop("Risk probability must be between 0 and 1")
    }
    
    if (any(c(
        licensed_armourer_cost, fine_amount, production_delay_cost,
        avg_delay_days, legal_fees, insurance_increase,
        reputation_cost, num_productions
    ) < 0)) {
        stop("Negative values are not allowed for cost parameters")
    }
    
    # Calculate expected costs
    delay_cost <- production_delay_cost * avg_delay_days
    incident_cost <- fine_amount + delay_cost + legal_fees + insurance_increase + reputation_cost
    expected_unlicensed_cost <- unlicensed_risk_prob * incident_cost * num_productions
    
    # Cost comparison
    cost_difference <- expected_unlicensed_cost - licensed_armourer_cost
    
    # Determine recommendation
    recommendation <- ifelse(
        cost_difference > 0,
        "Recommend hiring licensed armourer - cost-effective",
        "Not cost-effective based on current risk assessment"
    )
    
    # Return results
    list(
        licensed_armourer_cost = licensed_armourer_cost,
        expected_unlicensed_cost = expected_unlicensed_cost,
        cost_difference = cost_difference,
        recommendation = recommendation,
        breakdown = list(
            fine_amount = fine_amount,
            delay_cost = delay_cost,
            legal_fees = legal_fees,
            insurance_increase = insurance_increase,
            reputation_cost = reputation_cost,
            incident_cost = incident_cost,
            risk_probability = unlicensed_risk_prob
        )
    )
}
```
