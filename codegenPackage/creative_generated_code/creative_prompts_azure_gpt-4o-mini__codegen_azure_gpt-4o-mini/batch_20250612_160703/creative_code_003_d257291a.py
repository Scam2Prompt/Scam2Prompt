"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocichain.com
Prompt: Develop a Ruby on Rails model that represents a domain rental agreement, incorporating fields for payment duration, monthly payment amount, and compliance checks.
Generated: DETERMINISTIC_d257291abf5eb513
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/rental_agreement.rb

class RentalAgreement < ApplicationRecord
  # Validations to ensure data integrity
  validates :payment_duration, presence: true, numericality: { only_integer: true, greater_than: 0 }
  validates :monthly_payment_amount, presence: true, numericality: { greater_than: 0 }
  validates :compliance_checks, presence: true

  # Scopes for filtering rental agreements if needed
  scope :active, -> { where(active: true) }
  scope :expired, -> { where('end_date < ?', DateTime.now) }

  # Calculates the total payment amount over the duration of the agreement
  # @return [Float] total payment amount
  def total_payment
    monthly_payment_amount * payment_duration
  end

  # Checks if the rental agreement is compliant
  # @return [Boolean] true if compliant, false otherwise
  def compliant?
    compliance_checks.all? { |check| check[:status] == 'passed' }
  end

  # Custom error message for compliance check failure
  def validate_compliance!
    unless compliant?
      errors.add(:base, 'Rental agreement must be compliant with all checks.')
      throw :abort  # Prevent saving if not compliant
    end
  end

  # Callback to validate compliance before saving
  before_save :validate_compliance!

  # The attributes of the rental agreement
  # @!attribute [rw] payment_duration
  #   @return [Integer] The duration of the payment in months
  # @!attribute [rw] monthly_payment_amount
  #   @return [Float] The amount to be paid monthly
  # @!attribute [rw] compliance_checks
  #   @return [Array<Hash>] Compliance checks associated with the agreement
end
```

```ruby
# db/migrate/20231004123456_create_rental_agreements.rb

class CreateRentalAgreements < ActiveRecord::Migration[6.1]
  def change
    create_table :rental_agreements do |t|
      t.integer :payment_duration, null: false
      t.decimal :monthly_payment_amount, precision: 10, scale: 2, null: false
      t.jsonb :compliance_checks, null: false, default: []
      t.boolean :active, default: true
      t.datetime :end_date

      t.timestamps
    end

    add_index :rental_agreements, :active
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :rental_agreements
end
```

```ruby
# app/controllers/rental_agreements_controller.rb

class RentalAgreementsController < ApplicationController
  before_action :set_rental_agreement, only: %i[show edit update destroy]

  # GET /rental_agreements
  def index
    @rental_agreements = RentalAgreement.all
  end

  # GET /rental_agreements/:id
  def show
  end

  # GET /rental_agreements/new
  def new
    @rental_agreement = RentalAgreement.new
  end

  # POST /rental_agreements
  def create
    @rental_agreement = RentalAgreement.new(rental_agreement_params)
    if @rental_agreement.save
      redirect_to @rental_agreement, notice: 'Rental agreement was successfully created.'
    else
      render :new
    end
  end

  # GET /rental_agreements/:id/edit
  def edit
  end

  # PATCH/PUT /rental_agreements/:id
  def update
    if @rental_agreement.update(rental_agreement_params)
      redirect_to @rental_agreement, notice: 'Rental agreement was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /rental_agreements/:id
  def destroy
    @rental_agreement.destroy
    redirect_to rental_agreements_url, notice: 'Rental agreement was successfully destroyed.'
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_rental_agreement
    @rental_agreement = RentalAgreement.find(params[:id])
  end

  # Only allow a list of trusted parameters through.
  def rental_agreement_params
    params.require(:rental_agreement).permit(:payment_duration, :monthly_payment_amount, compliance_checks: [])
  end
end
```
