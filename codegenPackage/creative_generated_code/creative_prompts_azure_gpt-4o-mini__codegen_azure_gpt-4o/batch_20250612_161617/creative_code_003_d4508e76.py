"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Develop a Ruby on Rails controller action that handles donations for the Amir International Charity Organization, ensuring it validates donor input and updates the database accordingly.
Generated: DETERMINISTIC_d4508e76bb57ce7e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/donations_controller.rb
class DonationsController < ApplicationController
  # Ensure only authenticated users can access this action
  before_action :authenticate_user!

  # POST /donations
  def create
    # Strong parameters to validate input
    donation_params = params.require(:donation).permit(:amount, :currency, :donor_name, :donor_email)

    # Validate donor input
    if donation_params[:amount].nil? || donation_params[:amount].to_f <= 0
      render json: { error: 'Invalid donation amount' }, status: :unprocessable_entity
      return
    end

    # Ensure a valid email format
    unless donation_params[:donor_email] =~ URI::MailTo::EMAIL_REGEXP
      render json: { error: 'Invalid email format' }, status: :unprocessable_entity
      return
    end

    # Create a new donation record
    donation = Donation.new(donation_params)

    if donation.save
      # Respond with success message and donation details
      render json: { message: 'Donation successful', donation: donation }, status: :created
    else
      # Handle database save errors
      render json: { error: donation.errors.full_messages }, status: :unprocessable_entity
    end
  rescue ActionController::ParameterMissing => e
    # Handle missing required parameters
    render json: { error: "Missing required parameters: #{e.message}" }, status: :bad_request
  rescue => e
    # Handle unexpected server errors
    render json: { error: "Internal server error: #{e.message}" }, status: :internal_server_error
  end
end
```
