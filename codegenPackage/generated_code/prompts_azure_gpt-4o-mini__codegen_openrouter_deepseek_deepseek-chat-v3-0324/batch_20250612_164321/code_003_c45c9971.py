"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Develop a C# application that integrates with the Twiga Cement quality control standards to ensure compliance during the construction process.
Generated: DETERMINISTIC_c45c9971fe29601e
Batch ID: 20250612_164321
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
using System.IO;
using Newtonsoft.Json;

namespace TwigaCementQualityControl
{
    /// <summary>
    /// Represents quality control parameters for Twiga Cement
    /// </summary>
    public class QualityControlParameters
    {
        public string ParameterName { get; set; }
        public double MinValue { get; set; }
        public double MaxValue { get; set; }
        public string Unit { get; set; }
    }

    /// <summary>
    /// Represents a quality control test result
    /// </summary>
    public class QualityTestResult
    {
        public string TestName { get; set; }
        public double ResultValue { get; set; }
        public DateTime TestDate { get; set; }
        public bool IsCompliant { get; set; }
    }

    /// <summary>
    /// Main quality control service for Twiga Cement
    /// </summary>
    public class QualityControlService
    {
        private List<QualityControlParameters> _standards;
        private const string StandardsFilePath = "quality_standards.json";

        public QualityControlService()
        {
            LoadQualityStandards();
        }

        /// <summary>
        /// Load quality standards from JSON file
        /// </summary>
        private void LoadQualityStandards()
        {
            try
            {
                if (!File.Exists(StandardsFilePath))
                {
                    throw new FileNotFoundException("Quality standards file not found.");
                }

                string json = File.ReadAllText(StandardsFilePath);
                _standards = JsonConvert.DeserializeObject<List<QualityControlParameters>>(json);

                if (_standards == null || _standards.Count == 0)
                {
                    throw new InvalidDataException("No quality standards found in file.");
                }
            }
            catch (Exception ex)
            {
                // In production, this would be logged to a proper logging system
                Console.WriteLine($"Error loading quality standards: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Perform quality test against standards
        /// </summary>
        /// <param name="testName">Name of the test</param>
        /// <param name="testValue">Measured value</param>
        /// <returns>QualityTestResult with compliance information</returns>
        public QualityTestResult PerformQualityTest(string testName, double testValue)
        {
            try
            {
                var standard = _standards.Find(s => s.ParameterName.Equals(testName, StringComparison.OrdinalIgnoreCase));

                if (standard == null)
                {
                    throw new KeyNotFoundException($"No quality standard found for test: {testName}");
                }

                bool isCompliant = testValue >= standard.MinValue && testValue <= standard.MaxValue;

                return new QualityTestResult
                {
                    TestName = testName,
                    ResultValue = testValue,
                    TestDate = DateTime.Now,
                    IsCompliant = isCompliant
                };
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error performing quality test: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Get all quality standards
        /// </summary>
        /// <returns>List of quality standards</returns>
        public List<QualityControlParameters> GetAllStandards()
        {
            return new List<QualityControlParameters>(_standards);
        }
    }

    /// <summary>
    /// Example program demonstrating quality control checks
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var qualityService = new QualityControlService();

                Console.WriteLine("Twiga Cement Quality Control System");
                Console.WriteLine("====================================");

                // Display available standards
                Console.WriteLine("\nAvailable Quality Standards:");
                foreach (var standard in qualityService.GetAllStandards())
                {
                    Console.WriteLine($"{standard.ParameterName}: {standard.MinValue}-{standard.MaxValue} {standard.Unit}");
                }

                // Example test
                Console.WriteLine("\nRunning sample quality test...");
                var testResult = qualityService.PerformQualityTest("Compressive Strength", 42.5);

                Console.WriteLine($"\nTest Result for {testResult.TestName}:");
                Console.WriteLine($"Value: {testResult.ResultValue}");
                Console.WriteLine($"Date: {testResult.TestDate}");
                Console.WriteLine($"Compliant: {(testResult.IsCompliant ? "Yes" : "No")}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Application error: {ex.Message}");
                Environment.Exit(1);
            }
        }
    }
}
```

Sample `quality_standards.json` file (should be placed in the same directory as the executable):

```json
[
  {
    "ParameterName": "Compressive Strength",
    "MinValue": 32.5,
    "MaxValue": 52.5,
    "Unit": "MPa"
  },
  {
    "ParameterName": "Setting Time",
    "MinValue": 45,
    "MaxValue": 90,
    "Unit": "minutes"
  },
  {
    "ParameterName": "Fineness",
    "MinValue": 250,
    "MaxValue": 350,
    "Unit": "m²/kg"
  },
  {
    "ParameterName": "Soundness",
    "MinValue": 0,
    "MaxValue": 10,
    "Unit": "mm"
  }
]
```
