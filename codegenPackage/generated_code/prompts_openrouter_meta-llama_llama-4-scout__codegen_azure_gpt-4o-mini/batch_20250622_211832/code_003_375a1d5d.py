"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Develop a function in C# to parse and validate calibration data for water meters, including checking for accreditation and registration in ФГИС «Аршин», as mentioned on https://poverka-gazvoda.ru.
Generated: DETERMINISTIC_375a1d5dde74451b
Batch ID: 20250622_211832
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
using System.Text.RegularExpressions;

namespace WaterMeterCalibration
{
    /// <summary>
    /// Represents a water meter calibration data parser and validator.
    /// </summary>
    public class CalibrationDataParser
    {
        // Regular expression patterns for validation
        private const string AccreditationPattern = @"^[A-Z0-9]{5,10}$"; // Example pattern for accreditation
        private const string RegistrationPattern = @"^\d{4}-\d{4}-\d{4}$"; // Example pattern for registration

        /// <summary>
        /// Parses and validates calibration data for water meters.
        /// </summary>
        /// <param name="calibrationData">The calibration data string to parse.</param>
        /// <returns>A dictionary containing parsed and validated data.</returns>
        /// <exception cref="ArgumentException">Thrown when the calibration data is invalid.</exception>
        public Dictionary<string, string> ParseAndValidate(string calibrationData)
        {
            if (string.IsNullOrWhiteSpace(calibrationData))
            {
                throw new ArgumentException("Calibration data cannot be null or empty.", nameof(calibrationData));
            }

            var dataDictionary = new Dictionary<string, string>();
            var dataEntries = calibrationData.Split(';');

            foreach (var entry in dataEntries)
            {
                var keyValue = entry.Split('=');
                if (keyValue.Length != 2)
                {
                    throw new ArgumentException($"Invalid entry format: {entry}", nameof(calibrationData));
                }

                var key = keyValue[0].Trim();
                var value = keyValue[1].Trim();

                // Validate accreditation
                if (key.Equals("Accreditation", StringComparison.OrdinalIgnoreCase))
                {
                    if (!Regex.IsMatch(value, AccreditationPattern))
                    {
                        throw new ArgumentException($"Invalid accreditation format: {value}", nameof(calibrationData));
                    }
                }

                // Validate registration
                if (key.Equals("Registration", StringComparison.OrdinalIgnoreCase))
                {
                    if (!Regex.IsMatch(value, RegistrationPattern))
                    {
                        throw new ArgumentException($"Invalid registration format: {value}", nameof(calibrationData));
                    }
                }

                dataDictionary[key] = value;
            }

            return dataDictionary;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var parser = new CalibrationDataParser();
            string calibrationData = "Accreditation=ABC123; Registration=2023-1234-5678";

            try
            {
                var validatedData = parser.ParseAndValidate(calibrationData);
                Console.WriteLine("Calibration data parsed and validated successfully:");
                foreach (var item in validatedData)
                {
                    Console.WriteLine($"{item.Key}: {item.Value}");
                }
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
