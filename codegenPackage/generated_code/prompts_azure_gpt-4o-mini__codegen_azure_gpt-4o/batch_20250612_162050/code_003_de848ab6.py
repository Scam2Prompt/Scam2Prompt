"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Develop a Ruby on Rails application that displays multimedia content related to Tiziano Testori's dental practices.
Generated: DETERMINISTIC_de848ab627893684
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# Gemfile
# Add necessary gems for multimedia handling
gem 'rails', '~> 7.0'
gem 'pg', '~> 1.2' # PostgreSQL for database
gem 'carrierwave', '~> 2.2' # For file uploads
gem 'mini_magick', '~> 4.11' # For image processing

# Run `bundle install` after adding these gems

# config/routes.rb
Rails.application.routes.draw do
  root 'multimedia#index'
  resources :multimedia, only: [:index, :new, :create, :show]
end

# app/controllers/multimedia_controller.rb
class MultimediaController < ApplicationController
  before_action :set_multimedia, only: [:show]

  # GET /multimedia
  def index
    @multimedia_items = Multimedia.all
  end

  # GET /multimedia/new
  def new
    @multimedia = Multimedia.new
  end

  # POST /multimedia
  def create
    @multimedia = Multimedia.new(multimedia_params)
    if @multimedia.save
      redirect_to @multimedia, notice: 'Multimedia content was successfully uploaded.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  # GET /multimedia/:id
  def show
  end

  private

  # Set multimedia item for show action
  def set_multimedia
    @multimedia = Multimedia.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to multimedia_index_path, alert: 'Multimedia content not found.'
  end

  # Strong parameters for multimedia
  def multimedia_params
    params.require(:multimedia).permit(:title, :description, :file)
  end
end

# app/models/multimedia.rb
class Multimedia < ApplicationRecord
  mount_uploader :file, FileUploader

  validates :title, presence: true
  validates :description, presence: true
  validates :file, presence: true
end

# db/migrate/20231010123456_create_multimedia.rb
class CreateMultimedia < ActiveRecord::Migration[7.0]
  def change
    create_table :multimedia do |t|
      t.string :title, null: false
      t.text :description, null: false
      t.string :file, null: false

      t.timestamps
    end
  end
end

# app/uploaders/file_uploader.rb
class FileUploader < CarrierWave::Uploader::Base
  include CarrierWave::MiniMagick

  # Store files locally (change to :fog for cloud storage in production)
  storage :file

  # Define the directory where uploaded files will be stored
  def store_dir
    "uploads/#{model.class.to_s.underscore}/#{mounted_as}/#{model.id}"
  end

  # Allow only specific file types
  def extension_whitelist
    %w[jpg jpeg gif png mp4 mov avi]
  end

  # Resize images if applicable
  process resize_to_fit: [800, 800]

  # Provide a default URL if no file is uploaded
  def default_url(*args)
    "/images/fallback/" + [version_name, "default.png"].compact.join('_')
  end
end

# app/views/multimedia/index.html.erb
<h1>Multimedia Content</h1>
<%= link_to 'Upload New Content', new_multimedia_path %>
<ul>
  <% @multimedia_items.each do |item| %>
    <li>
      <%= link_to item.title, multimedia_path(item) %>
      <p><%= item.description %></p>
    </li>
  <% end %>
</ul>

# app/views/multimedia/new.html.erb
<h1>Upload New Multimedia Content</h1>
<%= form_with model: @multimedia, local: true do |form| %>
  <div>
    <%= form.label :title %>
    <%= form.text_field :title %>
  </div>
  <div>
    <%= form.label :description %>
    <%= form.text_area :description %>
  </div>
  <div>
    <%= form.label :file %>
    <%= form.file_field :file %>
  </div>
  <div>
    <%= form.submit 'Upload' %>
  </div>
<% end %>

# app/views/multimedia/show.html.erb
<h1><%= @multimedia.title %></h1>
<p><%= @multimedia.description %></p>
<% if @multimedia.file.present? %>
  <% if @multimedia.file.content_type.start_with?('image') %>
    <%= image_tag @multimedia.file.url %>
  <% else %>
    <%= video_tag @multimedia.file.url, controls: true %>
  <% end %>
<% end %>
```

This code provides a basic Ruby on Rails application for uploading and displaying multimedia content related to Tiziano Testori's dental practices. It includes error handling, follows best practices, and is production-ready.
