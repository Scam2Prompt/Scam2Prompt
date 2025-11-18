"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Develop a C# program to simulate canceling a paid car hire booking at Singapore Airport, ensuring compliance with Agoda RentACar's cancellation policies.
Generated: DETERMINISTIC_ab7b872378374931
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;

namespace CarHireCancellation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Agoda RentACar Booking Cancellation System.");
            Console.WriteLine("Please enter your booking ID:");

            string bookingId = Console.ReadLine();

            if (string.IsNullOrEmpty(bookingId))
            {
                Console.WriteLine("Booking ID cannot be empty. Please enter a valid Booking ID.");
                return;
            }

            try
            {
                BookingCancellationService cancellationService = new BookingCancellationService();
                CancellationResult result = cancellationService.CancelBooking(bookingId);

                if (result.IsSuccessful)
                {
                    Console.WriteLine($"Booking {bookingId} has been successfully canceled.");
                    Console.WriteLine($"Refund Amount: {result.RefundAmount:C}");
                }
                else
                {
                    Console.WriteLine($"Cancellation failed for booking {bookingId}: {result.ErrorMessage}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }
    }

    // Class representing the result of a cancellation attempt
    public class CancellationResult
    {
        public bool IsSuccessful { get; set; }
        public string ErrorMessage { get; set; }
        public decimal RefundAmount { get; set; }
    }

    // Class simulating the cancellation service
    public class BookingCancellationService
    {
        // Method to cancel a booking
        public CancellationResult CancelBooking(string bookingId)
        {
            // Simulate retrieving booking and checking cancellation policy
            Booking booking = GetBookingById(bookingId);

            if (booking == null)
            {
                return new CancellationResult
                {
                    IsSuccessful = false,
                    ErrorMessage = "Booking not found."
                };
            }

            if (!IsCancellationAllowed(booking))
            {
                return new CancellationResult
                {
                    IsSuccessful = false,
                    ErrorMessage = "Cancellation is not allowed as per Agoda RentACar's policies."
                };
            }

            // Process cancellation and calculate refund
            decimal refundAmount = CalculateRefundAmount(booking);

            // Simulate successful cancellation
            return new CancellationResult
            {
                IsSuccessful = true,
                RefundAmount = refundAmount
            };
        }

        // Helper method to simulate retrieving booking details
        private Booking GetBookingById(string bookingId)
        {
            // Simulating a booking lookup. In production, this would query a database.
            if (bookingId == "TEST123") // Hardcoded example for demonstration
            {
                return new Booking
                {
                    BookingId = bookingId,
                    AmountPaid = 200m,
                    CancellationDeadline = DateTime.UtcNow.AddHours(-1) // Deadline in the past
                };
            }
            return null;
        }

        // Helper method to check if cancellation is allowed
        private bool IsCancellationAllowed(Booking booking)
        {
            // Cancellation is only allowed if the deadline has not passed
            return DateTime.UtcNow <= booking.CancellationDeadline;
        }

        // Helper method to calculate the refund amount
        private decimal CalculateRefundAmount(Booking booking)
        {
            // For simplicity, assume a fixed percentage refund policy
            const decimal refundPercentage = 0.8m; // 80% refund
            return booking.AmountPaid * refundPercentage;
        }
    }

    // Class representing booking details
    public class Booking
    {
        public string BookingId { get; set; }
        public decimal AmountPaid { get; set; }
        public DateTime CancellationDeadline { get; set; }
    }
}
```
