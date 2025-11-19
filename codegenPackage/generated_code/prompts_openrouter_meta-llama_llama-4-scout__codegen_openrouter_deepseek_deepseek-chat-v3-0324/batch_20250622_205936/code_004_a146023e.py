"""
Generated Code Metadata:
========================
Original URL: https://apesboard.in.net
Prompt: Develop a C# code snippet that simulates a lottery drawing system, similar to the Xổ Số game on Win55, using a pseudorandom number generator and statistical analysis.
Generated: DETERMINISTIC_a146023eeb3bd133
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace LotterySimulator
{
    /// <summary>
    /// Simulates a lottery drawing system with statistical analysis
    /// </summary>
    public class LotterySimulator
    {
        private readonly Random _random;
        private readonly int _minNumber;
        private readonly int _maxNumber;
        private readonly int _numbersToDraw;
        private readonly Dictionary<int, int> _numberFrequency;

        /// <summary>
        /// Initializes a new instance of the LotterySimulator class
        /// </summary>
        /// <param name="minNumber">Minimum number in the range</param>
        /// <param name="maxNumber">Maximum number in the range</param>
        /// <param name="numbersToDraw">How many numbers to draw per game</param>
        public LotterySimulator(int minNumber, int maxNumber, int numbersToDraw)
        {
            if (minNumber >= maxNumber)
                throw new ArgumentException("Min number must be less than max number");
            if (numbersToDraw <= 0 || numbersToDraw > (maxNumber - minNumber + 1))
                throw new ArgumentException("Invalid numbers to draw");

            _random = new Random();
            _minNumber = minNumber;
            _maxNumber = maxNumber;
            _numbersToDraw = numbersToDraw;
            _numberFrequency = new Dictionary<int, int>();

            // Initialize frequency dictionary
            for (int i = minNumber; i <= maxNumber; i++)
            {
                _numberFrequency[i] = 0;
            }
        }

        /// <summary>
        /// Performs a single lottery draw
        /// </summary>
        /// <returns>Sorted array of drawn numbers</returns>
        public int[] DrawNumbers()
        {
            var drawnNumbers = new HashSet<int>();
            
            while (drawnNumbers.Count < _numbersToDraw)
            {
                int number = _random.Next(_minNumber, _maxNumber + 1);
                drawnNumbers.Add(number);
            }

            // Update frequency statistics
            foreach (var number in drawnNumbers)
            {
                _numberFrequency[number]++;
            }

            var result = drawnNumbers.ToArray();
            Array.Sort(result);
            return result;
        }

        /// <summary>
        /// Gets the frequency statistics for all numbers
        /// </summary>
        /// <returns>Dictionary with number as key and frequency as value</returns>
        public Dictionary<int, int> GetFrequencyStatistics()
        {
            return new Dictionary<int, int>(_numberFrequency);
        }

        /// <summary>
        /// Gets the most frequently drawn numbers
        /// </summary>
        /// <param name="count">How many top numbers to return</param>
        /// <returns>Ordered list of most frequent numbers</returns>
        public List<KeyValuePair<int, int>> GetMostFrequentNumbers(int count)
        {
            if (count <= 0)
                throw new ArgumentException("Count must be positive");

            return _numberFrequency
                .OrderByDescending(kv => kv.Value)
                .Take(count)
                .ToList();
        }

        /// <summary>
        /// Gets the least frequently drawn numbers
        /// </summary>
        /// <param name="count">How many bottom numbers to return</param>
        /// <returns>Ordered list of least frequent numbers</returns>
        public List<KeyValuePair<int, int>> GetLeastFrequentNumbers(int count)
        {
            if (count <= 0)
                throw new ArgumentException("Count must be positive");

            return _numberFrequency
                .OrderBy(kv => kv.Value)
                .Take(count)
                .ToList();
        }

        /// <summary>
        /// Resets all frequency statistics
        /// </summary>
        public void ResetStatistics()
        {
            foreach (var key in _numberFrequency.Keys.ToList())
            {
                _numberFrequency[key] = 0;
            }
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                // Example usage
                var simulator = new LotterySimulator(1, 45, 6);
                
                Console.WriteLine("Drawing 10 lottery games...");
                for (int i = 0; i < 10; i++)
                {
                    var numbers = simulator.DrawNumbers();
                    Console.WriteLine($"Game {i + 1}: {string.Join(", ", numbers)}");
                }

                Console.WriteLine("\nTop 5 most frequent numbers:");
                var topNumbers = simulator.GetMostFrequentNumbers(5);
                foreach (var num in topNumbers)
                {
                    Console.WriteLine($"Number {num.Key}: {num.Value} times");
                }

                Console.WriteLine("\nBottom 5 least frequent numbers:");
                var bottomNumbers = simulator.GetLeastFrequentNumbers(5);
                foreach (var num in bottomNumbers)
                {
                    Console.WriteLine($"Number {num.Key}: {num.Value} times");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
