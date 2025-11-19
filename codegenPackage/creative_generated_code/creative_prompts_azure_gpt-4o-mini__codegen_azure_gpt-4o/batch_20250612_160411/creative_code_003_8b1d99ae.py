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

namespace WealthfundedCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Welcome to Wealthfunded.com Investment Calculator!");
                Console.WriteLine("Select a plan to proceed:");
                Console.WriteLine("1. Basic Plan (Return: 5% annually)");
                Console.WriteLine("2. Premium Plan (Return: 8% annually)");
                Console.WriteLine("3. Elite Plan (Return: 12% annually)");
                Console.WriteLine("Enter the number corresponding to your plan:");

                // Input: Plan Selection
                int planChoice = int.Parse(Console.ReadLine());
                double annualReturnRate = GetAnnualReturnRate(planChoice);

                // Input: Investment Amount
                Console.WriteLine("Enter your investment amount (USD):");
                double investmentAmount = double.Parse(Console.ReadLine());

                // Input: Investment Duration
                Console.WriteLine("Enter the number of years for the investment:");
                int years = int.Parse(Console.ReadLine());

                // Calculate Total Return
                double totalReturn = CalculateTotalReturn(investmentAmount, annualReturnRate, years);

                // Output Result
                Console.WriteLine($"Your total return after {years} years is: ${totalReturn:F2}");
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Input error: Please ensure you enter valid numeric values.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Gets the annual return rate based on the selected plan.
        /// </summary>
        /// <param name="planChoice">The plan selected by the user.</param>
        /// <returns>Annual return rate in percentage.</returns>
        static double GetAnnualReturnRate(int planChoice)
        {
            switch (planChoice)
            {
                case 1:
                    return 0.05; // Basic Plan: 5% annually
                case 2:
                    return 0.08; // Premium Plan: 8% annually
                case 3:
                    return 0.12; // Elite Plan: 12% annually
                default:
                    throw new ArgumentException("Invalid plan choice. Please select a valid plan.");
            }
        }

        /// <summary>
        /// Calculates the total return on investment.
        /// </summary>
        /// <param name="investmentAmount">The initial investment amount.</param>
        /// <param name="annualReturnRate">The annual return rate.</param>
        /// <param name="years">The number of years for the investment.</param>
        /// <returns>Total return after the specified years.</returns>
        static double CalculateTotalReturn(double investmentAmount, double annualReturnRate, int years)
        {
            // Compound interest formula: Total = Principal * (1 + Rate)^Years
            return investmentAmount * Math.Pow(1 + annualReturnRate, years);
        }
    }
}
```
