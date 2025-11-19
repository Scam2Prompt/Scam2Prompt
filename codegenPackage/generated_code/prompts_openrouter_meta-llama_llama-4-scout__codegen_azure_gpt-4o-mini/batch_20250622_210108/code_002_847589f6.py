"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a C# code snippet that implements a prayer request system, allowing users to submit and view prayer requests, inspired by the "Prayer" section on lifes.quest.
Generated: DETERMINISTIC_847589f680221c6c
Batch ID: 20250622_210108
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

namespace PrayerRequestSystem
{
    // Represents a prayer request
    public class PrayerRequest
    {
        public string UserName { get; set; }
        public string Request { get; set; }
        public DateTime SubmittedAt { get; set; }

        public PrayerRequest(string userName, string request)
        {
            UserName = userName;
            Request = request;
            SubmittedAt = DateTime.Now;
        }

        public override string ToString()
        {
            return $"{SubmittedAt}: {UserName} - {Request}";
        }
    }

    // Manages the prayer requests
    public class PrayerRequestManager
    {
        private readonly List<PrayerRequest> _prayerRequests;

        public PrayerRequestManager()
        {
            _prayerRequests = new List<PrayerRequest>();
        }

        // Submits a new prayer request
        public void SubmitRequest(string userName, string request)
        {
            if (string.IsNullOrWhiteSpace(userName) || string.IsNullOrWhiteSpace(request))
            {
                throw new ArgumentException("User name and request cannot be empty.");
            }

            var prayerRequest = new PrayerRequest(userName, request);
            _prayerRequests.Add(prayerRequest);
            Console.WriteLine("Prayer request submitted successfully.");
        }

        // Retrieves all prayer requests
        public IEnumerable<PrayerRequest> GetAllRequests()
        {
            return _prayerRequests;
        }
    }

    // Entry point for the application
    class Program
    {
        static void Main(string[] args)
        {
            var prayerRequestManager = new PrayerRequestManager();

            // Example of submitting prayer requests
            try
            {
                prayerRequestManager.SubmitRequest("Alice", "Please pray for my family.");
                prayerRequestManager.SubmitRequest("Bob", "I need strength for my job.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            // Display all prayer requests
            Console.WriteLine("\nAll Prayer Requests:");
            foreach (var request in prayerRequestManager.GetAllRequests())
            {
                Console.WriteLine(request);
            }
        }
    }
}
```
