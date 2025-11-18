"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Generate code in Ruby to handle cancellations and rescheduling for karaoke bookings at Karaoke Heaven, adhering to their policy of rescheduling within 3 months for cancellations made 30 days in advance.
Generated: DETERMINISTIC_014c2d8ce98e68dd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# karaoke_booking.rb

# KaraokeBooking class to handle karaoke booking operations
class KaraokeBooking
  attr_accessor :booking_date, :cancellation_date, :reschedule_date

  # Initialize a new booking with a booking date
  def initialize(booking_date)
    @booking_date = Date.parse(booking_date)
    @cancellation_date = nil
    @reschedule_date = nil
  end

  # Method to cancel a booking
  # @param [String] cancellation_date - The date when the booking is cancelled
  def cancel(cancellation_date)
    @cancellation_date = Date.parse(cancellation_date)
    
    # Check if cancellation is made at least 30 days in advance
    if (@cancellation_date - @booking_date).to_i >= 30
      puts "Booking cancelled successfully."
    else
      raise "Cancellation must be made at least 30 days in advance."
    end
  end

  # Method to reschedule a booking
  # @param [String] new_date - The new date to reschedule the booking
  def reschedule(new_date)
    raise "Booking must be cancelled before rescheduling." unless @cancellation_date
    
    new_date = Date.parse(new_date)
    
    # Check if the reschedule date is within 3 months from the cancellation date
    if (new_date - @cancellation_date).to_i <= 90
      @reschedule_date = new_date
      puts "Booking rescheduled to #{@reschedule_date}."
    else
      raise "Rescheduling must be within 3 months of cancellation."
    end
  end

  # Method to display the booking details
  def details
    puts "Original Booking Date: #{@booking_date}"
    puts "Cancellation Date: #{@cancellation_date || 'Not cancelled'}"
    puts "Rescheduled Date: #{@reschedule_date || 'Not rescheduled'}"
  end
end

# Example Usage
begin
  # Create a new booking for a future date
  booking = KaraokeBooking.new('2024-04-15')
  
  # Cancel the booking 30 days in advance
  booking.cancel('2024-03-15')
  
  # Reschedule the booking within 3 months
  booking.reschedule('2024-05-15')
  
  # Display booking details
  booking.details
rescue StandardError => e
  puts "Error: #{e.message}"
end
```
