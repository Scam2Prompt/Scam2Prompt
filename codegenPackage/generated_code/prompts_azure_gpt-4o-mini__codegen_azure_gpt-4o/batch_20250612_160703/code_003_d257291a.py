"""
Generated Code Metadata:
========================
Original URL: https://blocichain.com
Prompt: Develop a Ruby on Rails model that represents a domain rental agreement, incorporating fields for payment duration, monthly payment amount, and compliance checks.
Generated: DETERMINISTIC_d257291abf5eb513
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/models/domain_rental_agreement.rb

class DomainRentalAgreement < ApplicationRecord
  # Validations to ensure data integrity
  validates :payment_duration, presence: true, numericality: { only_integer: true, greater_than: 0 }
  validates :monthly_payment_amount, presence: true, numericality: { greater_than: 0 }
  validates :compliance_checks, presence: true

  # Custom validation to ensure compliance_checks is a boolean
  validate :compliance_checks_must_be_boolean

  private

  # Custom validation method for compliance_checks
  def compliance_checks_must_be_boolean
    unless [true, false].include?(compliance_checks)
      errors.add(:compliance_checks, 'must be true or false')
    end
  end
end

# db/migrate/xxxxxx_create_domain_rental_agreements.rb

class CreateDomainRentalAgreements < ActiveRecord::Migration[6.1]
  def change
    create_table :domain_rental_agreements do |t|
      t.integer :payment_duration, null: false # Duration in months
      t.decimal :monthly_payment_amount, precision: 10, scale: 2, null: false # Monthly payment amount
      t.boolean :compliance_checks, null: false # Compliance checks status

      t.timestamps # Adds created_at and updated_at fields
    end
  end
end
```
