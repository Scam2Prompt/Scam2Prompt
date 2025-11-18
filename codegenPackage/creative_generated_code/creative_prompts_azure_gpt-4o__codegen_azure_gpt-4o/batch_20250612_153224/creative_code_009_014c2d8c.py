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

require 'date'

# Class to represent a karaoke booking
class KaraokeBooking
  attr_accessor :booking_date, :customer_name, :booking_id

  def initialize(booking_date, customer_name)
    @booking_date = booking_date
    @customer_name = customer_name
    @booking_id = generate_booking_id
  end

  # Generates a unique booking ID (UUID format)
  def generate_booking_id
    "#{customer_name[0..2].upcase}-#{SecureRandom.uuid}"
  end
end

# Class to handle booking operations like cancellation and rescheduling
class BookingManager
  RESCHEDULE_WINDOW = 3 * 30 # 3 months (approx.) in days
  CANCELLATION_NOTICE_PERIOD = 30 # 30 days in advance

  def initialize
    @bookings = {}
  end

  # Adds a booking
  def add_booking(booking)
    @bookings[booking.booking_id] = booking
    puts "Booking successfully added for #{booking.customer_name} on #{booking.booking_date}. Booking ID: #{booking.booking_id}"
  end

  # Handles cancellation of a booking
  def cancel_booking(booking_id)
    booking = @bookings[booking_id]
    if booking.nil?
      puts "Error: Booking ID not found."
      return
    end

    days_until_booking = (booking.booking_date - Date.today).to_i
    if days_until_booking >= CANCELLATION_NOTICE_PERIOD
      puts "Booking canceled for #{booking.customer_name}. You are eligible to reschedule within the next #{RESCHEDULE_WINDOW / 30} months."
      @bookings.delete(booking_id)
    else
      puts "Cancellation failed. Cancellations must be made at least #{CANCELLATION_NOTICE_PERIOD} days in advance."
    end
  end

  # Handles rescheduling of a booking
  def reschedule_booking(booking_id, new_date)
    booking = @bookings[booking_id]
    if booking.nil?
      puts "Error: Booking ID not found."
      return
    end

    days_until_new_date = (new_date - Date.today).to_i
    days_until_original_booking = (booking.booking_date - Date.today).to_i

    if days_until_original_booking >= CANCELLATION_NOTICE_PERIOD && days_until_new_date <= RESCHEDULE_WINDOW
      booking.booking_date = new_date
      puts "Booking successfully rescheduled for #{booking.customer_name}. New date: #{new_date}."
    else
      puts "Rescheduling failed. Ensure cancellations are made 30 days in advance and rescheduled within the next #{RESCHEDULE_WINDOW / 30} months."
    end
  end

  # List all bookings (useful for debugging and auditing)
  def list_bookings
    if @bookings.empty?
      puts "No bookings available."
      return
    end

    @bookings.each_value do |booking|
      puts "Booking ID: #{booking.booking_id}, Customer: #{booking.customer_name}, Date: #{booking.booking_date}"
    end
  end
end

# Example usage
if __FILE__ == $0
  manager = BookingManager.new

  # Create a new booking
  booking1 = KaraokeBooking.new(Date.today + 40, "Alice")
  booking2 = KaraokeBooking.new(Date.today + 20, "Bob")
  
  manager.add_booking(booking1)
  manager.add_booking(booking2)

  # Cancel a booking
  manager.cancel_booking(booking1.booking_id)

  # Reschedule a booking
  manager.reschedule_booking(booking1.booking_id, Date.today + 90)

  # List all bookings
  manager.list_bookings
end
```
