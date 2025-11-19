"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a Ruby on Rails model that represents the Armourers & Brasiers' Company’s charitable activities, including attributes for funding amounts and project descriptions.
Generated: DETERMINISTIC_5fbe1c58de851730
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/charity_activity.rb

class CharityActivity < ApplicationRecord
  # Validations to ensure data integrity
  validates :project_description, presence: true, length: { maximum: 500 }
  validates :funding_amount, presence: true, numericality: { greater_than_or_equal_to: 0 }

  # Scopes for querying
  scope :recent_activities, -> { order(created_at: :desc) }

  # Callback to log the creation of a new charity activity
  after_create :log_activity_creation

  private

  # Logs the creation of a charity activity
  def log_activity_creation
    Rails.logger.info("CharityActivity created: #{self.id} - #{self.project_description}")
  end
end
```

```ruby
# db/migrate/20230926123456_create_charity_activities.rb

class CreateCharityActivities < ActiveRecord::Migration[6.0]
  def change
    create_table :charity_activities do |t|
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
  resources :charity_activities
end
```

```ruby
# app/controllers/charity_activities_controller.rb

class CharityActivitiesController < ApplicationController
  before_action :set_charity_activity, only: [:show, :edit, :update, :destroy]

  # GET /charity_activities
  def index
    @charity_activities = CharityActivity.recent_activities
  end

  # GET /charity_activities/:id
  def show
  end

  # GET /charity_activities/new
  def new
    @charity_activity = CharityActivity.new
  end

  # POST /charity_activities
  def create
    @charity_activity = CharityActivity.new(charity_activity_params)
    if @charity_activity.save
      redirect_to @charity_activity, notice: 'Charity activity was successfully created.'
    else
      render :new
    end
  end

  # GET /charity_activities/:id/edit
  def edit
  end

  # PATCH/PUT /charity_activities/:id
  def update
    if @charity_activity.update(charity_activity_params)
      redirect_to @charity_activity, notice: 'Charity activity was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /charity_activities/:id
  def destroy
    @charity_activity.destroy
    redirect_to charity_activities_url, notice: 'Charity activity was successfully destroyed.'
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_charity_activity
    @charity_activity = CharityActivity.find(params[:id])
  rescue ActiveRecord::RecordNotFound => e
    redirect_to charity_activities_url, alert: "Charity activity not found."
  end

  # Only allow a list of trusted parameters through.
  def charity_activity_params
    params.require(:charity_activity).permit(:project_description, :funding_amount)
  end
end
```

```erb
<!-- app/views/charity_activities/index.html.erb -->

<h1>Charity Activities</h1>

<table>
  <thead>
    <tr>
      <th>Project Description</th>
      <th>Funding Amount</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @charity_activities.each do |activity| %>
      <tr>
        <td><%= activity.project_description %></td>
        <td><%= number_to_currency(activity.funding_amount) %></td>
        <td><%= link_to 'Show', activity %></td>
        <td><%= link_to 'Edit', edit_charity_activity_path(activity) %></td>
        <td><%= link_to 'Destroy', activity, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<%= link_to 'New Charity Activity', new_charity_activity_path %>
```

```erb
<!-- app/views/charity_activities/_form.html.erb -->

<%= form_with(model: charity_activity, local: true) do |form| %>
  <% if charity_activity.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(charity_activity.errors.count, "error") %> prohibited this charity activity from being saved:</h2>

      <ul>
        <% charity_activity.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :project_description %>
    <%= form.text_area :project_description %>
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

```erb
<!-- app/views/charity_activities/show.html.erb -->

<h1>Charity Activity</h1>

<p>
  <strong>Project Description:</strong>
  <%= @charity_activity.project_description %>
</p>

<p>
  <strong>Funding Amount:</strong>
  <%= number_to_currency(@charity_activity.funding_amount) %>
</p>

<%= link_to 'Edit', edit_charity_activity_path(@charity_activity) %> |
<%= link_to 'Back', charity_activities_path %>
```
