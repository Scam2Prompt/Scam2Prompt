"""
Generated Code Metadata:
========================
Original URL: https://gottrumpmemes.net
Prompt: Develop a Ruby on Rails application that allows users to input their real estate needs and receive personalized recommendations for neighborhoods in Southern Nevada.
Generated: DETERMINISTIC_2d53ac40c53751dd
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**config/routes.rb**
```ruby
Rails.application.routes.draw do
  get '/', to: 'welcome#index'
  resources :neighborhoods
  resources :user_needs, only: [:create, :show]
  post '/recommendations', to: 'recommendations#create'
end
```

**app/models/neighborhood.rb**
```ruby
# Neighborhood model representing a neighborhood in Southern Nevada
class Neighborhood < ApplicationRecord
  validates :name, :location, :price_range, :amenities, presence: true

  # Attributes:
  # - name (string)
  # - location (string)
  # - price_range (integer)
  # - amenities (array of strings)
end
```

**app/models/user_need.rb**
```ruby
# UserNeed model representing a user's real estate needs
class UserNeed < ApplicationRecord
  validates :price_range, :num_bedrooms, :num_bathrooms, :location, presence: true

  # Attributes:
  # - price_range (integer)
  # - num_bedrooms (integer)
  # - num_bathrooms (integer)
  # - location (string)
  # - amenities (array of strings)
end
```

**app/controllers/welcome_controller.rb**
```ruby
# WelcomeController handling root URL
class WelcomeController < ApplicationController
  def index
    @user_need = UserNeed.new
  end
end
```

**app/controllers/neighborhoods_controller.rb**
```ruby
# NeighborhoodsController handling CRUD operations for Neighborhoods
class NeighborhoodsController < ApplicationController
  before_action :set_neighborhood, only: [:show]

  def index
    @neighborhoods = Neighborhood.all
  end

  def show
    # Display neighborhood details
  end

  private

  def set_neighborhood
    @neighborhood = Neighborhood.find(params[:id])
  end
end
```

**app/controllers/user_needs_controller.rb**
```ruby
# UserNeedsController handling CRUD operations for UserNeeds
class UserNeedsController < ApplicationController
  before_action :set_user_need, only: [:show]

  def create
    @user_need = UserNeed.new(user_need_params)
    if @user_need.save
      redirect_to @user_need, notice: 'User need was successfully created.'
    else
      render :new
    end
  end

  def show
    # Display user need details
  end

  private

  def set_user_need
    @user_need = UserNeed.find(params[:id])
  end

  def user_need_params
    params.require(:user_need).permit(:price_range, :num_bedrooms, :num_bathrooms, :location, :amenities)
  end
end
```

**app/controllers/recommendations_controller.rb**
```ruby
# RecommendationsController handling recommendation generation
class RecommendationsController < ApplicationController
  def create
    user_need = UserNeed.new(user_need_params)
    recommendations = generate_recommendations(user_need)
    render json: recommendations
  end

  private

  def user_need_params
    params.require(:user_need).permit(:price_range, :num_bedrooms, :num_bathrooms, :location, :amenities)
  end

  def generate_recommendations(user_need)
    # Simple implementation using weighted scoring
    neighborhoods = Neighborhood.all
    recommendations = []

    neighborhoods.each do |neighborhood|
      score = calculate_score(neighborhood, user_need)
      recommendations << { neighborhood: neighborhood, score: score }
    end

    recommendations.sort_by! { |r| -r[:score] }
    recommendations.map { |r| r[:neighborhood] }
  end

  def calculate_score(neighborhood, user_need)
    # Weighted scoring based on price range, amenities, and location
    price_score = (user_need.price_range - neighborhood.price_range).abs / user_need.price_range.to_f
    amenity_score = (user_need.amenities & neighborhood.amenities).size / user_need.amenities.size.to_f
    location_score = location_similarity(neighborhood.location, user_need.location)

    0.4 * price_score + 0.3 * amenity_score + 0.3 * location_score
  end

  def location_similarity(location1, location2)
    # Simple location similarity metric (e.g., using Geocoder gem)
    # For demonstration purposes, assume identical locations have a similarity of 1
    location1 == location2 ? 1 : 0
  end
end
```

**db/migrate/2023xxxxxxx_create_neighborhoods.rb**
```ruby
class CreateNeighborhoods < ActiveRecord::Migration[7.0]
  def change
    create_table :neighborhoods do |t|
      t.string :name
      t.string :location
      t.integer :price_range
      t.string :amenities, array: true, default: []

      t.timestamps
    end
  end
end
```

**db/migrate/2023xxxxxxx_create_user_needs.rb**
```ruby
class CreateUserNeeds < ActiveRecord::Migration[7.0]
  def change
    create_table :user_needs do |t|
      t.integer :price_range
      t.integer :num_bedrooms
      t.integer :num_bathrooms
      t.string :location
      t.string :amenities, array: true, default: []

      t.timestamps
    end
  end
end
```

**db/seeds.rb**
```ruby
Neighborhood.create([
  { name: 'Summerlin', location: 'Las Vegas', price_range: 500000, amenities: ['parks', 'schools', 'shopping'] },
  { name: 'Henderson', location: 'Henderson', price_range: 400000, amenities: ['parks', 'schools', 'golf courses'] },
  { name: 'Downtown Las Vegas', location: 'Las Vegas', price_range: 300000, amenities: ['nightlife', 'restaurants', 'casinos'] }
])

UserNeed.create([
  { price_range: 450000, num_bedrooms: 3, num_bathrooms: 2, location: 'Las Vegas', amenities: ['parks', 'schools'] },
  { price_range: 350000, num_bedrooms: 2, num_bathrooms: 1, location: 'Henderson', amenities: ['golf courses', 'shopping'] }
])
```
