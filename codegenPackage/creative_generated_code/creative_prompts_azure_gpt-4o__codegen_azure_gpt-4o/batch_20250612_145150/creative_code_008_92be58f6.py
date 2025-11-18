"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Create a C# application that integrates with a banking system to allow users to change their card PIN, following the steps outlined on the Heritage Bank website.
Generated: DETERMINISTIC_92be58f6e6866eab
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;

namespace BankingSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Banking System!");
            
            // Step 1: Authenticate the user
            Console.Write("Enter your card number: ");
            string cardNumber = Console.ReadLine();

            Console.Write("Enter your current PIN: ");
            string currentPin = ReadMaskedInput();

            if (!AuthenticateUser(cardNumber, currentPin))
            {
                Console.WriteLine("Authentication failed! Please check your card details or PIN.");
                return;
            }

            // Step 2: Prompt the user to enter a new PIN
            Console.WriteLine("Authentication successful. Please proceed to change your PIN.");
            Console.Write("Enter a new PIN (4 digits): ");
            string newPin = ReadMaskedInput();

            // Validate the new PIN format
            if (!IsValidPin(newPin))
            {
                Console.WriteLine("Invalid PIN format. PIN must be a 4-digit number.");
                return;
            }

            Console.Write("Confirm the new PIN: ");
            string confirmPin = ReadMaskedInput();

            if (newPin != confirmPin)
            {
                Console.WriteLine("PINs do not match. Try again.");
                return;
            }

            // Step 3: Update the PIN in the banking system
            bool pinUpdated = UpdatePinInBankingSystem(cardNumber, newPin);

            if (pinUpdated)
            {
                Console.WriteLine("Your PIN has been successfully updated!");
            }
            else
            {
                Console.WriteLine("An error occurred while updating your PIN. Please try again later.");
            }
        }

        // Simulate user authentication (replace this with actual implementation)
        private static bool AuthenticateUser(string cardNumber, string pin)
        {
            // In production, this would involve API calls to the banking system
            // For now, we return true for demonstration purposes
            return !string.IsNullOrEmpty(cardNumber) && !string.IsNullOrEmpty(pin);
        }

        // Simulate PIN update in the banking system (replace this with actual implementation)
        private static bool UpdatePinInBankingSystem(string cardNumber, string newPin)
        {
            // In production, this would involve API calls to the banking system
            // For now, we return true for demonstration purposes
            return !string.IsNullOrEmpty(cardNumber) && !string.IsNullOrEmpty(newPin);
        }

        // Validate PIN format (must be a 4-digit number)
        private static bool IsValidPin(string pin)
        {
            return pin.Length == 4 && int.TryParse(pin, out _);
        }

        // Read input without displaying characters on the console (masked input for PINs)
        private static string ReadMaskedInput()
        {
            string maskedInput = string.Empty;
            ConsoleKeyInfo keyInfo;

            while ((keyInfo = Console.ReadKey(true)).Key != ConsoleKey.Enter)
            {
                if (keyInfo.Key == ConsoleKey.Backspace && maskedInput.Length > 0)
                {
                    maskedInput = maskedInput.Substring(0, maskedInput.Length - 1);
                    Console.Write("\b \b"); // Erase the last character
                }
                else if (keyInfo.Key != ConsoleKey.Backspace)
                {
                    maskedInput += keyInfo.KeyChar;
                    Console.Write("*"); // Display asterisks instead of the actual characters
                }
            }

            Console.WriteLine();
            return maskedInput;
        }
    }
}
```
