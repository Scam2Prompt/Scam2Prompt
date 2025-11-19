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
using System.Security.Cryptography;
using System.Text;

public class RandomStringGenerator
{
    private const string AlphanumericCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    /// <summary>
    /// Generates a random alphanumeric string with the specified length.
    /// </summary>
    /// <param name="length">The length of the string to generate.</param>
    /// <returns>A random alphanumeric string.</returns>
    public static string GenerateRandomString(int length)
    {
        if (length <= 0)
        {
            throw new ArgumentException("Length must be a positive integer.", nameof(length));
        }

        using var rng = RandomNumberGenerator.Create();
        var bytes = new byte[length];
        rng.GetBytes(bytes);

        var result = new char[length];
        for (int i = 0; i < length; i++)
        {
            result[i] = AlphanumericCharacters[bytes[i] % AlphanumericCharacters.Length];
        }

        return new string(result);
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        try
        {
            Console.WriteLine(RandomStringGenerator.GenerateRandomString(10));
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
