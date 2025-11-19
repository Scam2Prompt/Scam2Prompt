"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Construct a data model in Ruby on Rails to manage information about Moroccan cuisine, emphasizing popular dishes and their unique flavors.
Generated: DETERMINISTIC_0ffeebf58c84dfd7
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/dish.rb
class Dish < ApplicationRecord
  # Associations
  belongs_to :flavor

  # Validations
  validates :name, presence: true, uniqueness: true
  validates :description, presence: true, length: { maximum: 500 }
  validates :origin, presence: true

  # Scopes
  scope :popular, -> { where(popular: true) }

  # Methods
  def mark_as_popular
    update(popular: true)
  end
end

# app/models/flavor.rb
class Flavor < ApplicationRecord
  # Associations
  has_many :dishes, dependent: :destroy

  # Validations
  validates :name, presence: true, uniqueness: true
  validates :description, presence: true, length: { maximum: 300 }
end

# db/migrate/[timestamp]_create_dishes.rb
class CreateDishes < ActiveRecord::Migration[6.1]
  def change
    create_table :dishes do |t|
      t.string :name, null: false, index: { unique: true } # Dish name
      t.text :description, null: false                   # Description of the dish
      t.string :origin, null: false                      # Origin or region of the dish
      t.boolean :popular, default: false                 # Flag to mark the dish as popular
      t.references :flavor, null: false, foreign_key: true # Related flavor

      t.timestamps
    end
  end
end

# db/migrate/[timestamp]_create_flavors.rb
class CreateFlavors < ActiveRecord::Migration[6.1]
  def change
    create_table :flavors do |t|
      t.string :name, null: false, index: { unique: true } # Flavor name
      t.text :description, null: false                   # Description of the flavor

      t.timestamps
    end
  end
end

# Example seed data for Moroccan cuisine
# db/seeds.rb
# Creating some flavors
spicy = Flavor.create!(name: 'Spicy', description: 'A fiery flavor, common in many Moroccan dishes.')
sweet_savory = Flavor.create!(name: 'Sweet & Savory', description: 'A unique blend of sweetness and savory taste.')

# Creating dishes
Dish.create!(
  name: 'Tagine',
  description: 'A slow-cooked stew made with meat, vegetables, and rich spices.',
  origin: 'Morocco',
  popular: true,
  flavor: spicy
)

Dish.create!(
  name: 'Pastilla',
  description: 'A flaky pastry filled with pigeon meat, almonds, and a combination of sweet and savory spices.',
  origin: 'Morocco',
  popular: true,
  flavor: sweet_savory
)

Dish.create!(
  name: 'Harira',
  description: 'A traditional soup made with lentils, chickpeas, and tomatoes, often enjoyed during Ramadan.',
  origin: 'Morocco',
  flavor: spicy
)
```

This code defines models for managing Moroccan cuisine (`Dish` and `Flavor`) with validations, associations, and migrations. It includes seed data to populate the database with example dishes and flavors.
