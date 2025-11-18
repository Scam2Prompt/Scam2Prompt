"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bakedbeans.io
Prompt: Provide code examples in C# for creating a balanced investment portfolio that includes Forex and other asset classes, as described on bakedbeans.io.
Generated: DETERMINISTIC_324a4401fbfb9621
Batch ID: 20250612_151752
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
using System.Linq;

namespace InvestmentPortfolio
{
    public enum AssetClass
    {
        Forex,
        Stocks,
        Bonds,
        RealEstate,
        Commodities
    }

    public class Investment
    {
        public string Name { get; set; }
        public AssetClass AssetClass { get; set; }
        public double InvestmentAmount { get; set; }

        public Investment(string name, AssetClass assetClass, double investmentAmount)
        {
            if (string.IsNullOrWhiteSpace(name))
            {
                throw new ArgumentException("Investment name cannot be empty or null.", nameof(name));
            }

            if (investmentAmount <= 0)
            {
                throw new ArgumentOutOfRangeException(nameof(investmentAmount), "Investment amount must be greater than zero.");
            }

            Name = name;
            AssetClass = assetClass;
            InvestmentAmount = investmentAmount;
        }
    }

    public class Portfolio
    {
        private readonly List<Investment> _investments;

        public Portfolio()
        {
            _investments = new List<Investment>();
        }

        public void AddInvestment(Investment investment)
        {
            if (investment == null)
            {
                throw new ArgumentNullException(nameof(investment), "Investment cannot be null.");
            }

            _investments.Add(investment);
        }

        public double GetTotalInvestment()
        {
            return _investments.Sum(i => i.InvestmentAmount);
        }

        public Dictionary<AssetClass, double> GetAssetClassDistribution()
        {
            return _investments.GroupBy(i => i.AssetClass)
                               .ToDictionary(g => g.Key, g => g.Sum(i => i.InvestmentAmount));
        }

        public void DisplayPortfolio()
        {
            Console.WriteLine("Investment Portfolio:");
            foreach (var investment in _investments)
            {
                Console.WriteLine($"- {investment.Name}: {investment.InvestmentAmount:C} ({investment.AssetClass})");
            }

            Console.WriteLine($"Total Investment: {GetTotalInvestment():C}");
            Console.WriteLine("Asset Class Distribution:");
            var distribution = GetAssetClassDistribution();
            foreach (var asset in distribution)
            {
                Console.WriteLine($"{asset.Key}: {asset.Value:C}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var portfolio = new Portfolio();

                // Adding investments
                portfolio.AddInvestment(new Investment("Forex Trading", AssetClass.Forex, 10000));
                portfolio.AddInvestment(new Investment("Tech Stocks", AssetClass.Stocks, 20000));
                portfolio.AddInvestment(new Investment("Government Bonds", AssetClass.Bonds, 15000));
                portfolio.AddInvestment(new Investment("Real Estate Fund", AssetClass.RealEstate, 25000));
                portfolio.AddInvestment(new Investment("Gold", AssetClass.Commodities, 5000));

                // Display the portfolio
                portfolio.DisplayPortfolio();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
