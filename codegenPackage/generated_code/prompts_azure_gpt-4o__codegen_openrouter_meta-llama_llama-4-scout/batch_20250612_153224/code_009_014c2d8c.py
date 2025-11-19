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

# Define a class for Karaoke Booking
class KaraokeBooking
  attr_accessor :id, :customer_name, :booking_date, :cancellation_date

  def initialize(id, customer_name, booking_date)
    @id = id
    @customer_name = customer_name
    @booking_date = Date.parse(booking_date)
    @cancellation_date = nil
  end

  # Method to cancel a booking
  def cancel_booking(cancellation_date)
    @cancellation_date = Date.parse(cancellation_date)
    if @booking_date <= @cancellation_date
      raise ArgumentError, "Cancellation date cannot be on or after the booking date"
    end
  end

  # Method to reschedule a cancelled booking
  def reschedule(new_date)
    if @cancellation_date.nil?
      raise ArgumentError, "Booking has not been cancelled"
    end

    days_in_advance = (@cancellation_date - @booking_date).to_i
    if days_in_advance >= 30
      @booking_date = Date.parse(new_date)
      if (@booking_date - Date.today).to_i / 30.0 > 3
        raise ArgumentError, "New booking date is more than 3 months from now"
      end
    else
      raise ArgumentError, "Cancellation is not eligible for rescheduling"
    end
  end

  # Method to check booking status
  def booking_status
    if @cancellation_date.nil?
      "Active"
    else
      "Cancelled"
    end
  end
end

# Define a class for Karaoke Heaven
class KaraokeHeaven
  attr_accessor :bookings

  def initialize
    @bookings = []
  end

  # Method to add a new booking
  def add_booking(id, customer_name, booking_date)
    @bookings << KaraokeBooking.new(id, customer_name, booking_date)
  end

  # Method to get a booking by id
  def get_booking(id)
    @bookings.find { |booking| booking.id == id }
  end

  # Method to list all bookings
  def list_bookings
    @bookings.each do |booking|
      puts "ID: #{booking.id}, Customer: #{booking.customer_name}, Booking Date: #{booking.booking_date}, Status: #{booking.booking_status}"
    end
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  karaoke_heaven = KaraokeHeaven.new

  # Add bookings
  karaoke_heaven.add_booking(1, "John Doe", "2024-09-20")
  karaoke_heaven.add_booking(2, "Jane Doe", "2024-09-25")

  # List bookings
  puts "Bookings:"
  karaoke_heaven.list_bookings

  # Cancel a booking
  booking = karaoke_heaven.get_booking(1)
  booking.cancel_booking("2024-08-20")

  # Reschedule a cancelled booking
  begin
    booking.reschedule("2024-11-15")
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end

  # List bookings
  puts "\nUpdated Bookings:"
  karaoke_heaven.list_bookings
end
```
