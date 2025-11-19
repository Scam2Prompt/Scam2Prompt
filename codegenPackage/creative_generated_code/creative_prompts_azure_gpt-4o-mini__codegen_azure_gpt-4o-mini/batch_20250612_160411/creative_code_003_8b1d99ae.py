"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthfuned.com
Prompt: Develop a C# application that allows users to select a plan from Wealthfuned.com and calculates the total return based on their investment amount.
Generated: DETERMINISTIC_8b1d99ae46ce8b83
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;

namespace WealthFundInvestmentCalculator
{
    // Represents an investment plan with a name and expected return rate
    public class InvestmentPlan
    {
        public string Name { get; set; }
        public double ReturnRate { get; set; } // Expected return rate as a percentage

        public InvestmentPlan(string name, double returnRate)
        {
            Name = name;
            ReturnRate = returnRate;
        }
    }

    class Program
    {
        // List of available investment plans
        private static List<InvestmentPlan> investmentPlans = new List<InvestmentPlan>
        {
            new InvestmentPlan("Plan A", 5.0), // 5% return
            new InvestmentPlan("Plan B", 7.5), // 7.5% return
            new InvestmentPlan("Plan C", 10.0) // 10% return
        };

        static void Main(string[] args)
        {
            try
            {
                // Display available plans
                DisplayInvestmentPlans();

                // User selects a plan
                int selectedPlanIndex = GetUserPlanSelection();
                
                // Get investment amount from the user
                double investmentAmount = GetUserInvestmentAmount();

                // Calculate total return
                double totalReturn = CalculateTotalReturn(investmentAmount, investmentPlans[selectedPlanIndex].ReturnRate);

                // Display the total return
                Console.WriteLine($"Your total return from {investmentPlans[selectedPlanIndex].Name} will be: ${totalReturn:F2}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        // Displays the investment plans to the user
        private static void DisplayInvestmentPlans()
        {
            Console.WriteLine("Available Investment Plans:");
            for (int i = 0; i < investmentPlans.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {investmentPlans[i].Name} - Expected Return Rate: {investmentPlans[i].ReturnRate}%");
            }
        }

        // Gets user's selection of the investment plan
        private static int GetUserPlanSelection()
        {
            Console.Write("Please select a plan by entering the corresponding number: ");
            if (int.TryParse(Console.ReadLine(), out int selection) && selection > 0 && selection <= investmentPlans.Count)
            {
                return selection - 1; // Adjust for zero-based index
            }
            else
            {
                throw new ArgumentOutOfRangeException("Selection must be a valid plan number.");
            }
        }

        // Gets the investment amount from the user
        private static double GetUserInvestmentAmount()
        {
            Console.Write("Enter your investment amount: $");
            if (double.TryParse(Console.ReadLine(), out double amount) && amount > 0)
            {
                return amount;
            }
            else
            {
                throw new ArgumentException("Investment amount must be a positive number.");
            }
        }

        // Calculates the total return based on investment amount and return rate
        private static double CalculateTotalReturn(double investmentAmount, double returnRate)
        {
            return investmentAmount * (1 + returnRate / 100);
        }
    }
}
```
