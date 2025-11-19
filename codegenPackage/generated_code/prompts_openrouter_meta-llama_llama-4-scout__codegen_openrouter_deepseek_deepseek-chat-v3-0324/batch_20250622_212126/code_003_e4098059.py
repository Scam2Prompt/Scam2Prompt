"""
Generated Code Metadata:
========================
Original URL: https://new-school-day-1.pages.dev
Prompt: Create a code snippet in C# that can be used to generate a random alphanumeric string with a specified length, taking into account the character patterns seen on this webpage.
Generated: DETERMINISTIC_e4098059936f0b00
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Linq;
using System.Security.Cryptography;

/// <summary>
/// Utility class for generating random alphanumeric strings.
/// </summary>
public static class RandomStringGenerator
{
    // Define character sets
    private const string LowerCaseChars = "abcdefghijklmnopqrstuvwxyz";
    private const string UpperCaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private const string NumericChars = "0123456789";
    
    // Combined alphanumeric character set
    private static readonly char[] AlphanumericChars = 
        (LowerCaseChars + UpperCaseChars + NumericChars).ToCharArray();

    /// <summary>
    /// Generates a cryptographically secure random alphanumeric string.
    /// </summary>
    /// <param name="length">Desired length of the random string</param>
    /// <returns>Random alphanumeric string</returns>
    /// <exception cref="ArgumentOutOfRangeException">Thrown when length is less than 1</exception>
    public static string Generate(int length)
    {
        if (length < 1)
        {
            throw new ArgumentOutOfRangeException(nameof(length), "Length must be at least 1");
        }

        using (var rng = RandomNumberGenerator.Create())
        {
            var bytes = new byte[length * 4]; // Using 4 bytes per char to ensure uniform distribution
            rng.GetBytes(bytes);
            
            var result = new char[length];
            for (int i = 0; i < length; i++)
            {
                // Convert bytes to an index within the alphanumeric character array
                uint num = BitConverter.ToUInt32(bytes, i * 4);
                result[i] = AlphanumericChars[num % AlphanumericChars.Length];
            }
            
            return new string(result);
        }
    }
}
```
