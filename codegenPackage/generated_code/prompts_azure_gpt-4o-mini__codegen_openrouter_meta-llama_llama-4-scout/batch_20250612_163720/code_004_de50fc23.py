"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write a Ruby on Rails controller action to handle the submission of a form for a supercrescimento bacteriano test, including error handling for invalid inputs.
Generated: DETERMINISTIC_de50fc2310e81add
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/supercrescimento_bacteriano_controller.rb

class SupercrescimentoBacterianoController < ApplicationController
  # POST /supercrescimento_bacteriano
  def create
    @supercrescimento_bacteriano = SupercrescimentoBacteriano.new(supercrescimento_bacteriano_params)

    if @supercrescimento_bacteriano.valid?
      @supercrescimento_bacteriano.save!
      render json: @supercrescimento_bacteriano, status: :created
    else
      render json: { errors: @supercrescimento_bacteriano.errors }, status: :unprocessable_entity
    end
  rescue ActiveRecord::RecordNotSaved => e
    render json: { error: 'Failed to save supercrescimento bacteriano' }, status: :internal_server_error
  rescue StandardError => e
    render json: { error: 'An unexpected error occurred' }, status: :internal_server_error
  end

  private

  # Only allow a trusted parameter "white list" through.
  def supercrescimento_bacteriano_params
    params.require(:supercrescimento_bacteriano).permit(
      :initial_bacteria_count,
      :growth_rate,
      :time_elapsed,
      :nutrient_level
    )
  end
end
```

```ruby
# app/models/supercrescimento_bacteriano.rb

class SupercrescimentoBacteriano < ApplicationRecord
  validates :initial_bacteria_count, presence: true, numericality: { greater_than: 0 }
  validates :growth_rate, presence: true, numericality: { greater_than_or_equal_to: 0 }
  validates :time_elapsed, presence: true, numericality: { greater_than_or_equal_to: 0 }
  validates :nutrient_level, presence: true, numericality: { greater_than_or_equal_to: 0, less_than_or_equal_to: 100 }
end
```

```ruby
# db/migrate/xxxxxxxxxxxxxx_create_supercrescimento_bacteriano.rb

class CreateSupercrescimentoBacteriano < ActiveRecord::Migration[7.0]
  def change
    create_table :supercrescimento_bacteriano do |t|
      t.float :initial_bacteria_count, null: false
      t.float :growth_rate, null: false
      t.float :time_elapsed, null: false
      t.float :nutrient_level, null: false

      t.timestamps
    end
  end
end
```
