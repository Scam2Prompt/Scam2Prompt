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
# app/models/domain_rental_agreement.rb
class DomainRentalAgreement < ApplicationRecord
  # Validations to ensure required fields are present and properly formatted
  validates :payment_duration, presence: true, numericality: { only_integer: true, greater_than: 0 }
  validates :monthly_payment_amount, presence: true, numericality: { greater_than: 0 }
  validates :is_compliant, inclusion: { in: [true, false] }

  # Callbacks
  before_save :ensure_compliance

  # Custom method to calculate total payment amount based on duration and monthly payment
  def total_payment_amount
    payment_duration * monthly_payment_amount
  end

  private

  # Callback method to enforce compliance checks
  def ensure_compliance
    # In a real-world scenario, this method would include business logic
    # for checking compliance based on specific rules
    self.is_compliant = compliance_check_logic
  end

  # Stub for compliance check logic
  def compliance_check_logic
    # Placeholder for actual compliance validation logic
    true
  end
end
```

```ruby
# db/migrate/xxxxxx_create_domain_rental_agreements.rb
class CreateDomainRentalAgreements < ActiveRecord::Migration[6.1]
  def change
    create_table :domain_rental_agreements do |t|
      t.integer :payment_duration, null: false  # Duration of payment in months
      t.decimal :monthly_payment_amount, precision: 10, scale: 2, null: false  # Monthly payment amount
      t.boolean :is_compliant, default: true  # Compliance status (true/false)

      t.timestamps  # Automatically adds created_at and updated_at fields
    end

    # Adding an index to optimize queries on compliance
    add_index :domain_rental_agreements, :is_compliant
  end
end
```

```ruby
# spec/models/domain_rental_agreement_spec.rb (RSpec test for the model)
require 'rails_helper'

RSpec.describe DomainRentalAgreement, type: :model do
  describe 'validations' do
    it { should validate_presence_of(:payment_duration) }
    it { should validate_numericality_of(:payment_duration).only_integer.is_greater_than(0) }
    it { should validate_presence_of(:monthly_payment_amount) }
    it { should validate_numericality_of(:monthly_payment_amount).is_greater_than(0) }
    it { should validate_inclusion_of(:is_compliant).in_array([true, false]) }
  end

  describe '#total_payment_amount' do
    it 'calculates the total payment correctly' do
      agreement = DomainRentalAgreement.new(payment_duration: 12, monthly_payment_amount: 100.0)
      expect(agreement.total_payment_amount).to eq(1200.0)
    end
  end
end
```
