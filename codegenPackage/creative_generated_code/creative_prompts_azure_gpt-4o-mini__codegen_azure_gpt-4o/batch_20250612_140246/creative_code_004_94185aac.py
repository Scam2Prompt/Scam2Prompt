"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ugge.cc
Prompt: Write a C# method that generates an info card for user account details, mimicking the functionality described in the system notification.
Generated: DETERMINISTIC_94185aac75f953bc
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;

namespace UserAccountInfoCard
{
    public class UserAccount
    {
        // Properties to hold user account details
        public string FullName { get; set; }
        public string Email { get; set; }
        public DateTime DateJoined { get; set; }
        public bool IsActive { get; set; }

        // Constructor
        public UserAccount(string fullName, string email, DateTime dateJoined, bool isActive)
        {
            FullName = fullName;
            Email = email;
            DateJoined = dateJoined;
            IsActive = isActive;
        }
    }

    public class InfoCardGenerator
    {
        /// <summary>
        /// Generates an information card for a user account.
        /// </summary>
        /// <param name="user">UserAccount object containing user details.</param>
        /// <returns>A formatted string representing the user account info card.</returns>
        public string GenerateInfoCard(UserAccount user)
        {
            try
            {
                if (user == null)
                {
                    throw new ArgumentNullException(nameof(user), "User account cannot be null.");
                }

                // Build the info card
                string status = user.IsActive ? "Active" : "Inactive";
                string infoCard = $@"
---------------------------------
          User Info Card
---------------------------------
Name:       {user.FullName}
Email:      {user.Email}
Date Joined:{user.DateJoined.ToString("MMMM dd, yyyy")}
Status:     {status}
---------------------------------
";
                return infoCard;
            }
            catch (ArgumentNullException ex)
            {
                // Handle null user error
                return $"Error: {ex.Message}";
            }
            catch (Exception ex)
            {
                // Handle any unexpected errors
                return $"An unexpected error occurred: {ex.Message}";
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Example usage
            var user = new UserAccount("John Doe", "john.doe@example.com", new DateTime(2022, 1, 15), true);
            var generator = new InfoCardGenerator();

            // Generate and display the info card
            string infoCard = generator.GenerateInfoCard(user);
            Console.WriteLine(infoCard);
        }
    }
}
```
