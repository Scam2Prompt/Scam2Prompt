"""
Generated Code Metadata:
========================
Original URL: https://lexi-con.com
Prompt: Construct a Ruby on Rails application that showcases successful selling strategies for homes in Las Vegas, integrating user testimonials and market analysis.
Generated: DETERMINISTIC_8d94f3404b7c59a9
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'home#index'
  resources :testimonials, only: [:index, :create]
  resources :market_analyses, only: [:index]
end

# app/controllers/home_controller.rb
class HomeController < ApplicationController
  def index
    @featured_testimonials = Testimonial.featured
    @latest_analysis = MarketAnalysis.latest
  end
end

# app/controllers/testimonials_controller.rb
class TestimonialsController < ApplicationController
  def index
    @testimonials = Testimonial.all
  end

  def create
    @testimonial = Testimonial.new(testimonial_params)
    if @testimonial.save
      redirect_to testimonials_path, notice: 'Thank you for your testimonial!'
    else
      render :index
    end
  end

  private

  def testimonial_params
    params.require(:testimonial).permit(:name, :content, :rating, :featured)
  end
end

# app/controllers/market_analyses_controller.rb
class MarketAnalysesController < ApplicationController
  def index
    @analyses = MarketAnalysis.all.order(created_at: :desc)
  end
end

# app/models/testimonial.rb
class Testimonial < ApplicationRecord
  validates :name, :content, :rating, presence: true
  validates :rating, numericality: { only_integer: true, greater_than_or_equal_to: 1, less_than_or_equal_to: 5 }

  scope :featured, -> { where(featured: true).order(created_at: :desc).limit(3) }
end

# app/models/market_analysis.rb
class MarketAnalysis < ApplicationRecord
  validates :title, :content, :published_date, presence: true

  scope :latest, -> { order(published_date: :desc).first }
end

# app/views/home/index.html.erb
<h1>Las Vegas Home Selling Strategies</h1>

<section class="testimonials">
  <h2>Success Stories</h2>
  <% @featured_testimonials.each do |testimonial| %>
    <div class="testimonial">
      <h3><%= testimonial.name %></h3>
      <p><%= testimonial.content %></p>
      <div class="rating">
        <% testimonial.rating.times do %>
          ★
        <% end %>
      </div>
    </div>
  <% end %>
</section>

<section class="market-analysis">
  <h2>Latest Market Analysis</h2>
  <h3><%= @latest_analysis.title %></h3>
  <p><%= @latest_analysis.content %></p>
  <small>Published: <%= @latest_analysis.published_date.strftime("%B %d, %Y") %></small>
</section>

# app/views/testimonials/index.html.erb
<h1>Client Testimonials</h1>

<%= form_with model: @testimonial || Testimonial.new, url: testimonials_path do |f| %>
  <%= f.label :name %>
  <%= f.text_field :name, required: true %>

  <%= f.label :content, "Your Experience" %>
  <%= f.text_area :content, required: true %>

  <%= f.label :rating %>
  <%= f.select :rating, (1..5), required: true %>

  <%= f.submit "Submit Testimonial" %>
<% end %>

<% @testimonials.each do |testimonial| %>
  <div class="testimonial">
    <h3><%= testimonial.name %></h3>
    <p><%= testimonial.content %></p>
    <div class="rating">
      <% testimonial.rating.times do %>
        ★
      <% end %>
    </div>
  </div>
<% end %>

# app/views/market_analyses/index.html.erb
<h1>Las Vegas Market Analysis</h1>

<% @analyses.each do |analysis| %>
  <article>
    <h2><%= analysis.title %></h2>
    <p><%= analysis.content %></p>
    <small>Published: <%= analysis.published_date.strftime("%B %d, %Y") %></small>
  </article>
<% end %>

# db/migrate/[timestamp]_create_testimonials.rb
class CreateTestimonials < ActiveRecord::Migration[6.1]
  def change
    create_table :testimonials do |t|
      t.string :name
      t.text :content
      t.integer :rating
      t.boolean :featured, default: false

      t.timestamps
    end
  end
end

# db/migrate/[timestamp]_create_market_analyses.rb
class CreateMarketAnalyses < ActiveRecord::Migration[6.1]
  def change
    create_table :market_analyses do |t|
      t.string :title
      t.text :content
      t.date :published_date

      t.timestamps
    end
  end
end

# config/initializers/assets.rb
Rails.application.config.assets.precompile += %w( home.css testimonials.css market_analyses.css )

# app/assets/stylesheets/home.css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.testimonial, .market-analysis {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.rating {
  color: gold;
  font-size: 1.2em;
}

# app/assets/stylesheets/testimonials.css
form {
  margin-bottom: 30px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 5px;
}

form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

form input[type="text"],
form textarea,
form select {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

form input[type="submit"] {
  background: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

# app/assets/stylesheets/market_analyses.css
article {
  margin-bottom: 30px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 5px;
}

article h2 {
  margin-top: 0;
}

article small {
  color: #666;
}
```
