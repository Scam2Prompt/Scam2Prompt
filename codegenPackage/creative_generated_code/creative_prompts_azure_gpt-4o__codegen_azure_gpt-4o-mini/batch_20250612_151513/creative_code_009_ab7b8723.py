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
    // Enum representing the cancellation policies
    public enum CancellationPolicy
    {
        FreeCancellation,
        PartialRefund,
        NonRefundable
    }

    // Class representing a car hire booking
    public class CarHireBooking
    {
        public string BookingId { get; set; }
        public DateTime BookingDate { get; set; }
        public DateTime RentalStartDate { get; set; }
        public CancellationPolicy Policy { get; set; }
        public decimal AmountPaid { get; set; }

        public CarHireBooking(string bookingId, DateTime bookingDate, DateTime rentalStartDate, CancellationPolicy policy, decimal amountPaid)
        {
            BookingId = bookingId;
            BookingDate = bookingDate;
            RentalStartDate = rentalStartDate;
            Policy = policy;
            AmountPaid = amountPaid;
        }
    }

    // Class to handle booking cancellation
    public class BookingManager
    {
        // Method to cancel the booking
        public decimal CancelBooking(CarHireBooking booking)
        {
            // Check if the booking is eligible for cancellation based on the rental start date
            TimeSpan timeUntilRentalStart = booking.RentalStartDate - DateTime.Now;

            if (timeUntilRentalStart.TotalDays < 0)
            {
                throw new InvalidOperationException("Cannot cancel a booking that has already started.");
            }

            // Determine refund amount based on cancellation policy
            decimal refundAmount = 0;

            switch (booking.Policy)
            {
                case CancellationPolicy.FreeCancellation:
                    refundAmount = booking.AmountPaid; // Full refund
                    break;

                case CancellationPolicy.PartialRefund:
                    refundAmount = booking.AmountPaid * 0.5m; // 50% refund
                    break;

                case CancellationPolicy.NonRefundable:
                    refundAmount = 0; // No refund
                    break;

                default:
                    throw new ArgumentOutOfRangeException("Invalid cancellation policy.");
            }

            Console.WriteLine($"Booking {booking.BookingId} cancelled. Refund Amount: {refundAmount:C}");
            return refundAmount;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Creating a sample booking
                CarHireBooking booking = new CarHireBooking(
                    "BK12345",
                    DateTime.Now.AddDays(-3),
                    DateTime.Now.AddDays(2), // Rental starts in 2 days
                    CancellationPolicy.PartialRefund,
                    100m // Amount paid
                );

                // Initializing BookingManager and cancelling the booking
                BookingManager bookingManager = new BookingManager();
                decimal refund = bookingManager.CancelBooking(booking);

                Console.WriteLine($"Refund processed: {refund:C}");
            }
            catch (Exception ex)
            {
                // Handle any exceptions that occur during cancellation
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
