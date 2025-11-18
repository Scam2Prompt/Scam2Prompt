"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Write a script in Ruby on Rails to implement a "Refund & Return Policy" system for an e-commerce store selling Travis Scott merchandise.
Generated: DETERMINISTIC_0ea7bbab0d267eeb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/refund_policy.rb
class RefundPolicy < ApplicationRecord
  # Validations for refund policy fields
  validates :policy_title, presence: true
  validates :description, presence: true
  validates :return_window_days, numericality: { only_integer: true, greater_than: 0 }

  # Associations if necessary (e.g., belongs_to a store)
  # belongs_to :store

  # Method to check if an item is eligible for a return
  def eligible_for_return?(purchase_date)
    return false if purchase_date.nil?

    # Check if the current date is within the return window
    (Date.today - purchase_date).to_i <= return_window_days
  end
end

# app/controllers/refund_policies_controller.rb
class RefundPoliciesController < ApplicationController
  before_action :set_refund_policy, only: [:show, :edit, :update, :destroy]

  # GET /refund_policies
  def index
    @refund_policies = RefundPolicy.all
  end

  # GET /refund_policies/:id
  def show
  end

  # GET /refund_policies/new
  def new
    @refund_policy = RefundPolicy.new
  end

  # POST /refund_policies
  def create
    @refund_policy = RefundPolicy.new(refund_policy_params)

    if @refund_policy.save
      redirect_to @refund_policy, notice: 'Refund policy was successfully created.'
    else
      render :new
    end
  end

  # GET /refund_policies/:id/edit
  def edit
  end

  # PATCH/PUT /refund_policies/:id
  def update
    if @refund_policy.update(refund_policy_params)
      redirect_to @refund_policy, notice: 'Refund policy was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /refund_policies/:id
  def destroy
    @refund_policy.destroy
    redirect_to refund_policies_url, notice: 'Refund policy was successfully destroyed.'
  end

  private

  # Set the refund policy for actions that require it
  def set_refund_policy
    @refund_policy = RefundPolicy.find(params[:id])
  rescue ActiveRecord::RecordNotFound => e
    redirect_to refund_policies_url, alert: 'Refund policy not found.'
  end

  # Strong parameters for refund policy
  def refund_policy_params
    params.require(:refund_policy).permit(:policy_title, :description, :return_window_days)
  end
end

# app/views/refund_policies/index.html.erb
<h1>Refund Policies</h1>
<%= link_to 'New Refund Policy', new_refund_policy_path %>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Return Window (Days)</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @refund_policies.each do |policy| %>
      <tr>
        <td><%= policy.policy_title %></td>
        <td><%= policy.description %></td>
        <td><%= policy.return_window_days %></td>
        <td><%= link_to 'Show', policy %></td>
        <td><%= link_to 'Edit', edit_refund_policy_path(policy) %></td>
        <td><%= link_to 'Destroy', policy, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

# app/views/refund_policies/show.html.erb
<h1><%= @refund_policy.policy_title %></h1>
<p><%= @refund_policy.description %></p>
<p>Return Window: <%= @refund_policy.return_window_days %> days</p>

<%= link_to 'Edit', edit_refund_policy_path(@refund_policy) %> |
<%= link_to 'Back', refund_policies_path %>

# app/views/refund_policies/new.html.erb
<h1>New Refund Policy</h1>
<%= render 'form', refund_policy: @refund_policy %>
<%= link_to 'Back', refund_policies_path %>

# app/views/refund_policies/edit.html.erb
<h1>Edit Refund Policy</h1>
<%= render 'form', refund_policy: @refund_policy %>
<%= link_to 'Back', refund_policies_path %>

# app/views/refund_policies/_form.html.erb
<%= form_with(model: refund_policy, local: true) do |form| %>
  <% if refund_policy.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(refund_policy.errors.count, "error") %> prohibited this refund policy from being saved:</h2>
      <ul>
        <% refund_policy.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :policy_title %>
    <%= form.text_field :policy_title %>
  </div>

  <div class="field">
    <%= form.label :description %>
    <%= form.text_area :description %>
  </div>

  <div class="field">
    <%= form.label :return_window_days %>
    <%= form.number_field :return_window_days %>
  </div>

  <div class="actions">
    <%= form.submit %>
  </div>
<% end %>
```
