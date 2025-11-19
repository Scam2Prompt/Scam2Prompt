"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a Ruby on Rails model that represents the Armourers & Brasiers' Company’s charitable activities, including attributes for funding amounts and project descriptions.
Generated: DETERMINISTIC_5fbe1c58de851730
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/models/charitable_activity.rb

class CharitableActivity < ApplicationRecord
  # Validations to ensure data integrity
  validates :project_description, presence: true, length: { maximum: 255 }
  validates :funding_amount, presence: true, numericality: { greater_than_or_equal_to: 0 }

  # Scopes for querying
  scope :recent_activities, -> { order(created_at: :desc) }
  scope :with_minimum_funding, ->(amount) { where('funding_amount >= ?', amount) }

  # Method to display a summary of the charitable activity
  def summary
    "#{project_description} - Funding: £#{funding_amount}"
  end
end
```

```ruby
# db/migrate/20231001000000_create_charitable_activities.rb

class CreateCharitableActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :charitable_activities do |t|
      t.string :project_description, null: false
      t.decimal :funding_amount, precision: 10, scale: 2, null: false

      t.timestamps
    end
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :charitable_activities
end
```

```ruby
# app/controllers/charitable_activities_controller.rb

class CharitableActivitiesController < ApplicationController
  before_action :set_charitable_activity, only: %i[show edit update destroy]

  # GET /charitable_activities
  def index
    @charitable_activities = CharitableActivity.recent_activities
  end

  # GET /charitable_activities/:id
  def show
  end

  # GET /charitable_activities/new
  def new
    @charitable_activity = CharitableActivity.new
  end

  # POST /charitable_activities
  def create
    @charitable_activity = CharitableActivity.new(charitable_activity_params)

    if @charitable_activity.save
      redirect_to @charitable_activity, notice: 'Charitable activity was successfully created.'
    else
      render :new
    end
  end

  # GET /charitable_activities/:id/edit
  def edit
  end

  # PATCH/PUT /charitable_activities/:id
  def update
    if @charitable_activity.update(charitable_activity_params)
      redirect_to @charitable_activity, notice: 'Charitable activity was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /charitable_activities/:id
  def destroy
    @charitable_activity.destroy
    redirect_to charitable_activities_url, notice: 'Charitable activity was successfully destroyed.'
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_charitable_activity
    @charitable_activity = CharitableActivity.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to charitable_activities_url, alert: 'Charitable activity not found.'
  end

  # Only allow a list of trusted parameters through.
  def charitable_activity_params
    params.require(:charitable_activity).permit(:project_description, :funding_amount)
  end
end
```

```erb
<!-- app/views/charitable_activities/index.html.erb -->

<h1>Charitable Activities</h1>

<%= link_to 'New Charitable Activity', new_charitable_activity_path %>

<table>
  <thead>
    <tr>
      <th>Project Description</th>
      <th>Funding Amount</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @charitable_activities.each do |activity| %>
      <tr>
        <td><%= activity.project_description %></td>
        <td>£<%= activity.funding_amount %></td>
        <td><%= link_to 'Show', activity %></td>
        <td><%= link_to 'Edit', edit_charitable_activity_path(activity) %></td>
        <td><%= link_to 'Destroy', activity, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>
```

```erb
<!-- app/views/charitable_activities/show.html.erb -->

<h1>Charitable Activity Details</h1>

<p>
  <strong>Project Description:</strong>
  <%= @charitable_activity.project_description %>
</p>

<p>
  <strong>Funding Amount:</strong>
  £<%= @charitable_activity.funding_amount %>
</p>

<%= link_to 'Edit', edit_charitable_activity_path(@charitable_activity) %> |
<%= link_to 'Back', charitable_activities_path %>
```

```erb
<!-- app/views/charitable_activities/new.html.erb -->

<h1>New Charitable Activity</h1>

<%= render 'form' %>

<%= link_to 'Back', charitable_activities_path %>
```

```erb
<!-- app/views/charitable_activities/edit.html.erb -->

<h1>Edit Charitable Activity</h1>

<%= render 'form' %>

<%= link_to 'Back', charitable_activities_path %>
```

```erb
<!-- app/views/charitable_activities/_form.html.erb -->

<%= form_with(model: charitable_activity, local: true) do |form| %>
  <% if charitable_activity.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(charitable_activity.errors.count, "error") %> prohibited this charitable activity from being saved:</h2>

      <ul>
        <% charitable_activity.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :project_description %>
    <%= form.text_field :project_description %>
  </div>

  <div class="field">
    <%= form.label :funding_amount %>
    <%= form.number_field :funding_amount, step: 0.01 %>
  </div>

  <div class="actions">
    <%= form.submit %>
  </div>
<% end %>
```
