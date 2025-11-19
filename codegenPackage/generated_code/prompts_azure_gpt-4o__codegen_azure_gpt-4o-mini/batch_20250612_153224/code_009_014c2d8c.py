"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Generate code in Ruby to handle cancellations and rescheduling for karaoke bookings at Karaoke Heaven, adhering to their policy of rescheduling within 3 months for cancellations made 30 days in advance.
Generated: DETERMINISTIC_014c2d8ce98e68dd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# karaoke_booking.rb

class KaraokeBooking
  attr_accessor :booking_date, :cancellation_date, :rescheduled_date

  # Initialize a new booking with a booking date
  def initialize(booking_date)
    @booking_date = booking_date
    @cancellation_date = nil
    @rescheduled_date = nil
  end

  # Method to cancel a booking
  def cancel_booking(cancellation_date)
    # Check if cancellation is made at least 30 days in advance
    if (cancellation_date - @booking_date).to_i >= 30
      @cancellation_date = cancellation_date
      puts "Booking cancelled successfully."
    else
      raise StandardError, "Cancellation must be made at least 30 days in advance."
    end
  end

  # Method to reschedule a booking
  def reschedule_booking(new_date)
    # Check if the booking was cancelled and rescheduling is within 3 months
    if @cancellation_date.nil?
      raise StandardError, "Cannot reschedule a booking that has not been cancelled."
    elsif (new_date - @cancellation_date).to_i > 90
      raise StandardError, "Rescheduling must be within 3 months of cancellation."
    else
      @rescheduled_date = new_date
      puts "Booking rescheduled successfully to #{new_date}."
    end
  end

  # Method to display booking details
  def display_booking_details
    puts "Original Booking Date: #{@booking_date}"
    puts "Cancellation Date: #{@cancellation_date.nil? ? 'Not cancelled' : @cancellation_date}"
    puts "Rescheduled Date: #{@rescheduled_date.nil? ? 'Not rescheduled' : @rescheduled_date}"
  end
end

# Example usage
begin
  # Create a new booking for a date 60 days from today
  booking = KaraokeBooking.new(Date.today + 60)

  # Cancel the booking 30 days in advance
  booking.cancel_booking(Date.today + 30)

  # Reschedule the booking within 3 months
  booking.reschedule_booking(Date.today + 60)

  # Display the booking details
  booking.display_booking_details
rescue StandardError => e
  puts "Error: #{e.message}"
end
```

Make sure to require the `date` library if you are running this code in an environment where it is not automatically included:

```ruby
require 'date'
```
