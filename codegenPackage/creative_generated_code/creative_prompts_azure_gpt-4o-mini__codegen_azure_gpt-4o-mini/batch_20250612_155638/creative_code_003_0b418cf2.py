"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Develop a C# application that allows users to track their slot machine bets and winnings, referencing the "how do you win big on slot machines" tips from walletguard.pro.
Generated: DETERMINISTIC_0b418cf222822b83
Batch ID: 20250612_155638
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

namespace SlotMachineTracker
{
    /// <summary>
    /// Represents a single bet on a slot machine.
    /// </summary>
    public class SlotBet
    {
        public decimal Amount { get; set; }
        public decimal Winnings { get; set; }
        public DateTime Date { get; set; }
        
        public SlotBet(decimal amount, decimal winnings)
        {
            Amount = amount;
            Winnings = winnings;
            Date = DateTime.Now;
        }
        
        public decimal NetProfit => Winnings - Amount;
    }

    /// <summary>
    /// Manages tracking of slot machine bets and winnings.
    /// </summary>
    public class SlotMachineTracker
    {
        private List<SlotBet> bets;

        public SlotMachineTracker()
        {
            bets = new List<SlotBet>();
        }

        /// <summary>
        /// Adds a new bet to the tracker.
        /// </summary>
        /// <param name="amount">The amount bet.</param>
        /// <param name="winnings">The winnings from the bet.</param>
        public void AddBet(decimal amount, decimal winnings)
        {
            if (amount < 0 || winnings < 0)
                throw new ArgumentOutOfRangeException("Amounts cannot be negative.");

            bets.Add(new SlotBet(amount, winnings));
        }

        /// <summary>
        /// Calculates total bets placed.
        /// </summary>
        /// <returns>Total amount bet.</returns>
        public decimal GetTotalBets()
        {
            decimal total = 0;
            foreach (var bet in bets)
            {
                total += bet.Amount;
            }
            return total;
        }

        /// <summary>
        /// Calculates total winnings.
        /// </summary>
        /// <returns>Total winnings earned.</returns>
        public decimal GetTotalWinnings()
        {
            decimal total = 0;
            foreach (var bet in bets)
            {
                total += bet.Winnings;
            }
            return total;
        }

        /// <summary>
        /// Calculates total profit or loss from bets.
        /// </summary>
        /// <returns>Total net profit or loss.</returns>
        public decimal GetTotalProfit()
        {
            return GetTotalWinnings() - GetTotalBets();
        }
        
        /// <summary>
        /// Displays all bets in a user-friendly format.
        /// </summary>
        public void DisplayBets()
        {
            Console.WriteLine("Your Slot Machine Bets:");
            foreach (var bet in bets)
            {
                Console.WriteLine($"Date: {bet.Date}, Amount Bet: {bet.Amount:C}, Winnings: {bet.Winnings:C}, Net Profit: {bet.NetProfit:C}");
            }
        }
    }

    /// <summary>
    /// Main class to run the Slot Machine Tracker application.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            SlotMachineTracker tracker = new SlotMachineTracker();
            string input;

            Console.WriteLine("Welcome to the Slot Machine Tracker!");

            while (true)
            {
                try
                {
                    Console.Write("Enter your bet amount (or 'exit' to quit): ");
                    input = Console.ReadLine();
                    if (input.ToLower() == "exit") break;

                    decimal betAmount = decimal.Parse(input);
                    Console.Write("Enter your winnings: ");
                    decimal winnings = decimal.Parse(Console.ReadLine());

                    tracker.AddBet(betAmount, winnings);
                    Console.WriteLine("Bet added successfully!");
                }
                catch (FormatException)
                {
                    Console.WriteLine("Invalid input. Please enter a valid number.");
                }
                catch (ArgumentOutOfRangeException ex)
                {
                    Console.WriteLine(ex.Message);
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"An unexpected error occurred: {ex.Message}");
                }
            }

            tracker.DisplayBets();
            Console.WriteLine($"Total Bets: {tracker.GetTotalBets():C}");
            Console.WriteLine($"Total Winnings: {tracker.GetTotalWinnings():C}");
            Console.WriteLine($"Total Profit/Loss: {tracker.GetTotalProfit():C}");
        }
    }
}
```
