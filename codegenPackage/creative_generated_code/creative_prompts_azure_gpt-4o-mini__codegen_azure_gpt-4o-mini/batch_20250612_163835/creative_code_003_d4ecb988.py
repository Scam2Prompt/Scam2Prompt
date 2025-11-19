"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igadvocacia.com
Prompt: Develop a Ruby on Rails application that manages client consultations for a full-service law firm, inspired by the client-focused approach of IG Advocacia.
Generated: DETERMINISTIC_d4ecb98834c0432b
Batch ID: 20250612_163835
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
  resources :clients do
    resources :consultations
  end

  root 'clients#index'
end
```

```ruby
# app/controllers/clients_controller.rb

class ClientsController < ApplicationController
  before_action :set_client, only: %i[show edit update destroy]

  # GET /clients
  def index
    @clients = Client.all
  end

  # GET /clients/:id
  def show
  end

  # GET /clients/new
  def new
    @client = Client.new
  end

  # POST /clients
  def create
    @client = Client.new(client_params)
    
    if @client.save
      redirect_to @client, notice: 'Client was successfully created.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  # GET /clients/:id/edit
  def edit
  end

  # PATCH/PUT /clients/:id
  def update
    if @client.update(client_params)
      redirect_to @client, notice: 'Client was successfully updated.'
    else
      render :edit, status: :unprocessable_entity
    end
  end

  # DELETE /clients/:id
  def destroy
    @client.destroy
    redirect_to clients_url, notice: 'Client was successfully destroyed.'
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_client
    @client = Client.find(params[:id])
  end

  # Only allow a trusted parameter "white list" through.
  def client_params
    params.require(:client).permit(:name, :email, :phone, :address)
  end
end
```

```ruby
# app/controllers/consultations_controller.rb

class ConsultationsController < ApplicationController
  before_action :set_client
  before_action :set_consultation, only: %i[show edit update destroy]

  # GET /clients/:client_id/consultations
  def index
    @consultations = @client.consultations
  end

  # GET /clients/:client_id/consultations/new
  def new
    @consultation = @client.consultations.new
  end

  # POST /clients/:client_id/consultations
  def create
    @consultation = @client.consultations.new(consultation_params)
    
    if @consultation.save
      redirect_to client_consultations_path(@client), notice: 'Consultation was successfully created.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  # GET /clients/:client_id/consultations/:id/edit
  def edit
  end

  # PATCH/PUT /clients/:client_id/consultations/:id
  def update
    if @consultation.update(consultation_params)
      redirect_to client_consultations_path(@client), notice: 'Consultation was successfully updated.'
    else
      render :edit, status: :unprocessable_entity
    end
  end

  # DELETE /clients/:client_id/consultations/:id
  def destroy
    @consultation.destroy
    redirect_to client_consultations_path(@client), notice: 'Consultation was successfully destroyed.'
  end

  private

  def set_client
    @client = Client.find(params[:client_id])
  end

  def set_consultation
    @consultation = @client.consultations.find(params[:id])
  end

  def consultation_params
    params.require(:consultation).permit(:date, :time, :details)
  end
end
```

```ruby
# app/models/client.rb

class Client < ApplicationRecord
  has_many :consultations, dependent: :destroy
  
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true
end
```

```ruby
# app/models/consultation.rb

class Consultation < ApplicationRecord
  belongs_to :client
  
  validates :date, presence: true
  validates :time, presence: true
  validates :details, presence: true
end
```

```ruby
# db/migrate/20230101000000_create_clients.rb

class CreateClients < ActiveRecord::Migration[6.1]
  def change
    create_table :clients do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.string :phone, null: false
      t.string :address

      t.timestamps
    end
  end
end
```

```ruby
# db/migrate/20230101000001_create_consultations.rb

class CreateConsultations < ActiveRecord::Migration[6.1]
  def change
    create_table :consultations do |t|
      t.references :client, null: false, foreign_key: true
      t.date :date, null: false
      t.time :time, null: false
      t.text :details, null: false

      t.timestamps
    end
  end
end
```

```ruby
# app/views/clients/index.html.erb

<h1>Clients</h1>

<%= link_to 'New Client', new_client_path %>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @clients.each do |client| %>
      <tr>
        <td><%= client.name %></td>
        <td><%= client.email %></td>
        <td>
          <%= link_to 'Show', client_path(client) %>
          <%= link_to 'Edit', edit_client_path(client) %>
          <%= link_to 'Destroy', client_path(client), method: :delete, data: { confirm: 'Are you sure?' } %>
          <%= link_to 'Consultations', client_consultations_path(client) %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>
```

```ruby
# app/views/clients/new.html.erb

<h1>New Client</h1>

<%= render 'form', client: @client %>

<%= link_to 'Back', clients_path %>
```

```ruby
# app/views/clients/_form.html.erb

<%= form_with(model: client) do |form| %>
  <% if client.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(client.errors.count, "error") %> prohibited this client from being saved:</h2>
      <ul>
        <% client.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div>
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div>
    <%= form.label :email %>
    <%= form.email_field :email %>
  </div>

  <div>
    <%= form.label :phone %>
    <%= form.telephone_field :phone %>
  </div>

  <div>
    <%= form.label :address %>
    <%= form.text_area :address %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

```ruby
# app/views/consultations/index.html.erb

<h1>Consultations for <%= @client.name %></h1>

<%= link_to 'New Consultation', new_client_consultation_path(@client) %>

<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>Time</th>
      <th>Details</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @consultations.each do |consultation| %>
      <tr>
        <td><%= consultation.date %></td>
        <td><%= consultation.time %></td>
        <td><%= consultation.details %></td>
        <td>
          <%= link_to 'Show', client_consultation_path(@client, consultation) %>
          <%= link_to 'Edit', edit_client_consultation_path(@client, consultation) %>
          <%= link_to 'Destroy', client_consultation_path(@client, consultation), method: :delete, data: { confirm: 'Are you sure?' } %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>
```

```ruby
# app/views/consultations/new.html.erb

<h1>New Consultation for <%= @client.name %></h1>

<%= render 'form', client: @client, consultation: @consultation %>

<%= link_to 'Back', client_consultations_path(@client) %>
```

```ruby
# app/views/consultations/_form.html.erb

<%= form_with(model: [client, consultation]) do |form| %>
  <% if consultation.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(consultation
