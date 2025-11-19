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
# frozen_string_literal: true

# KaraokeBooking handles the logic for cancellations and rescheduling of karaoke bookings
# at Karaoke Heaven, adhering to their policy rules.
class KaraokeBooking
  # Policy constants
  CANCELLATION_DEADLINE = 30 # days in advance
  RESCHEDULE_WINDOW = 3 # months

  attr_reader :booking_date, :cancellation_date

  # Initializes a new KaraokeBooking instance
  # @param booking_date [Date] The date of the karaoke booking
  # @param cancellation_date [Date] The date when cancellation is requested
  def initialize(booking_date, cancellation_date)
    @booking_date = booking_date
    @cancellation_date = cancellation_date
  end

  # Checks if the cancellation is eligible for rescheduling based on policy
  # @return [Boolean] true if eligible, false otherwise
  def eligible_for_reschedule?
    return false unless cancelled_30_days_in_advance?

    max_reschedule_date <= booking_date + RESCHEDULE_WINDOW.months
  end

  # Calculates the maximum date to which the booking can be rescheduled
  # @return [Date] The maximum reschedule date
  def max_reschedule_date
    cancellation_date + RESCHEDULE_WINDOW.months
  end

  # Reschedules the booking to a new date if eligible
  # @param new_date [Date] The new booking date
  # @return [Hash] Result with status and message or error
  def reschedule(new_date)
    unless eligible_for_reschedule?
      return { success: false, error: 'Cancellation not eligible for rescheduling' }
    end

    if new_date < Date.today
      return { success: false, error: 'New date cannot be in the past' }
    end

    if new_date > max_reschedule_date
      return { success: false, error: "New date must be within #{RESCHEDULE_WINDOW} months of cancellation" }
    end

    @booking_date = new_date
    { success: true, message: 'Booking successfully rescheduled', new_booking_date: new_date }
  end

  # Cancels the booking and returns eligibility for reschedule
  # @return [Hash] Result with status and eligibility info
  def cancel
    eligible = eligible_for_reschedule?
    message = if eligible
                "Cancellation successful. You may reschedule within #{RESCHEDULE_WINDOW} months."
              else
                'Cancellation successful. Not eligible for rescheduling.'
              end

    { success: true, eligible_for_reschedule: eligible, message: message }
  end

  private

  # Checks if cancellation was made at least 30 days in advance
  # @return [Boolean] true if cancelled 30+ days in advance, false otherwise
  def cancelled_30_days_in_advance?
    (booking_date - cancellation_date).to_i >= CANCELLATION_DEADLINE
  end
end

# Example usage:
# booking = KaraokeBooking.new(Date.new(2023, 12, 25), Date.new(2023, 11, 20))
# puts booking.eligible_for_reschedule?
# puts booking.reschedule(Date.new(2024, 2, 15))
# puts booking.cancel
```
