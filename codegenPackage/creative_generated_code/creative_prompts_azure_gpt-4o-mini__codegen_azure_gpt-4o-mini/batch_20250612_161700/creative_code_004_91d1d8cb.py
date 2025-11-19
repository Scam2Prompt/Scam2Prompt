"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conseil-consultatif-femme.cg
Prompt: Construct a Ruby on Rails application that displays a gallery of images from the Conseil Consultatif de la Femme's activities, highlighting their efforts in promoting women's rights.
Generated: DETERMINISTIC_91d1d8cb31a02774
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'galleries#index'

  resources :galleries, only: [:index, :show]
end
```

```ruby
# app/controllers/galleries_controller.rb
class GalleriesController < ApplicationController
  # Display all galleries
  def index
    @galleries = Gallery.all
  end

  # Show a specific gallery
  def show
    @gallery = Gallery.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to galleries_path, alert: "Gallery not found."
  end
end
```

```ruby
# app/models/gallery.rb
class Gallery < ApplicationRecord
  # Validations for ensuring data integrity
  validates :title, presence: true
  validates :description, presence: true
  validates :image_url, presence: true
end
```

```ruby
# db/migrate/20231001000000_create_galleries.rb
class CreateGalleries < ActiveRecord::Migration[6.1]
  def change
    create_table :galleries do |t|
      t.string :title, null: false
      t.text :description, null: false
      t.string :image_url, null: false

      t.timestamps
    end
  end
end
```

```erb
<!-- app/views/galleries/index.html.erb -->
<h1>Gallery of Activities</h1>

<% @galleries.each do |gallery| %>
  <div class="gallery-item">
    <h2><%= gallery.title %></h2>
    <img src="<%= gallery.image_url %>" alt="<%= gallery.title %>" />
    <p><%= gallery.description %></p>
    <%= link_to 'View Details', gallery_path(gallery) %>
  </div>
<% end %>
```

```erb
<!-- app/views/galleries/show.html.erb -->
<h1><%= @gallery.title %></h1>
<img src="<%= @gallery.image_url %>" alt="<%= @gallery.title %>" />
<p><%= @gallery.description %></p>

<%= link_to 'Back to Gallery', galleries_path %>
```

```scss
/* app/assets/stylesheets/application.scss */
body {
  font-family: Arial, sans-serif;
}

.gallery-item {
  border: 1px solid #ccc;
  margin: 10px;
  padding: 10px;
}

.gallery-item img {
  max-width: 100%;
  height: auto;
}
```

```bash
# .env
DATABASE_URL=postgres://user:password@localhost:5432/your_database_name
```

```bash
# Run the following commands in your terminal to setup the application
rails db:create
rails db:migrate
rails server
```

```ruby
# Gemfile
gem 'rails', '~> 6.1.0'
gem 'pg' # For Postgres
gem 'dotenv-rails' # For environment variable management
```

Make sure to run `bundle install` after updating your Gemfile.
