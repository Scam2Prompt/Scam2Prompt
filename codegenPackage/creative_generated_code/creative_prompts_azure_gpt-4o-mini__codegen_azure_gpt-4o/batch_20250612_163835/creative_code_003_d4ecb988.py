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
# Ruby on Rails Application: Consultation Management System

# Generate a new Rails application
# Command: rails new law_firm_consultations

# Navigate into the application directory
# Command: cd law_firm_consultations

# Generate necessary models and controllers
# Command: rails generate model Client name:string email:string phone:string
# Command: rails generate model Consultation client_id:integer consultation_date:datetime notes:text
# Command: rails generate controller Clients
# Command: rails generate controller Consultations

# Example code for the models, controllers, and views.

## app/models/client.rb
class Client < ApplicationRecord
  # Associations
  has_many :consultations, dependent: :destroy

  # Validations
  validates :name, presence: true, length: { maximum: 100 }
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true, length: { maximum: 15 }
end

## app/models/consultation.rb
class Consultation < ApplicationRecord
  # Associations
  belongs_to :client

  # Validations
  validates :consultation_date, presence: true
  validates :notes, length: { maximum: 1000 }
end

## app/controllers/clients_controller.rb
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
    redirect_to clients_url, notice: 'Client was successfully deleted.'
  end

  private

  def set_client
    @client = Client.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to clients_url, alert: 'Client not found.'
  end

  def client_params
    params.require(:client).permit(:name, :email, :phone)
  end
end

## app/controllers/consultations_controller.rb
class ConsultationsController < ApplicationController
  before_action :set_consultation, only: %i[show edit update destroy]
  before_action :set_client, only: %i[new create]

  # GET /consultations
  def index
    @consultations = Consultation.all.includes(:client)
  end

  # GET /consultations/:id
  def show
  end

  # GET /clients/:client_id/consultations/new
  def new
    @consultation = @client.consultations.new
  end

  # POST /clients/:client_id/consultations
  def create
    @consultation = @client.consultations.new(consultation_params)
    if @consultation.save
      redirect_to @client, notice: 'Consultation was successfully created.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  # GET /consultations/:id/edit
  def edit
  end

  # PATCH/PUT /consultations/:id
  def update
    if @consultation.update(consultation_params)
      redirect_to @consultation.client, notice: 'Consultation was successfully updated.'
    else
      render :edit, status: :unprocessable_entity
    end
  end

  # DELETE /consultations/:id
  def destroy
    client = @consultation.client
    @consultation.destroy
    redirect_to client, notice: 'Consultation was successfully deleted.'
  end

  private

  def set_consultation
    @consultation = Consultation.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to consultations_url, alert: 'Consultation not found.'
  end

  def set_client
    @client = Client.find(params[:client_id])
  rescue ActiveRecord::RecordNotFound
    redirect_to clients_url, alert: 'Client not found.'
  end

  def consultation_params
    params.require(:consultation).permit(:consultation_date, :notes)
  end
end

## app/views/clients/index.html.erb
<h1>Clients</h1>
<%= link_to 'New Client', new_client_path %>
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Phone</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @clients.each do |client| %>
      <tr>
        <td><%= client.name %></td>
        <td><%= client.email %></td>
        <td><%= client.phone %></td>
        <td>
          <%= link_to 'Show', client_path(client) %>
          <%= link_to 'Edit', edit_client_path(client) %>
          <%= link_to 'Delete', client_path(client), method: :delete, data: { confirm: 'Are you sure?' } %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>

## app/views/consultations/index.html.erb
<h1>Consultations</h1>
<%= link_to 'New Consultation', new_client_consultation_path(@client) %>
<table>
  <thead>
    <tr>
      <th>Client</th>
      <th>Date</th>
      <th>Notes</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @consultations.each do |consultation| %>
      <tr>
        <td><%= consultation.client.name %></td>
        <td><%= consultation.consultation_date.strftime('%B %d, %Y %H:%M') %></td>
        <td><%= consultation.notes %></td>
        <td>
          <%= link_to 'Show', consultation_path(consultation) %>
          <%= link_to 'Edit', edit_consultation_path(consultation) %>
          <%= link_to 'Delete', consultation_path(consultation), method: :delete, data: { confirm: 'Are you sure?' } %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>

# Run migrations
# Command: rails db:migrate

# Start the Rails server
# Command: rails server
```
