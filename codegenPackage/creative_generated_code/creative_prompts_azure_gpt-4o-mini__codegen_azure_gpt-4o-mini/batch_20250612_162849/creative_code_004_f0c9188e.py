"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xr9sw.eth-drop.top
Prompt: What libraries are recommended for working with Google Gmail API in a Ruby on Rails project?
Generated: DETERMINISTIC_f0c9188e60769b6e
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile

# Adding the required gem for interacting with Google APIs
gem 'google-api-client', '~> 0.53.0' # Ensure you have the latest stable version

# After modifying the Gemfile, run `bundle install` to install the gem
```

```ruby
# app/controllers/gmail_controller.rb

class GmailController < ApplicationController
  require 'google/apis/gmail_v1'
  require 'googleauth'

  # Initialize Gmail API service
  def initialize
    @service = Google::Apis::GmailV1::GmailService.new
    @service.authorization = authorize
  end

  # Authorizes the user and returns a Google Auth object
  def authorize
    client_id = Google::Auth::ClientId.from_file('path/to/your/client_secret.json')
    scope = Google::Apis::GmailV1::AUTH_GMAIL_READONLY # Change to appropriate scope as needed
    authorizer = Google::Auth::UserAuthorizer.new(client_id, scope, token_store)
    
    user_id = 'user@example.com' # Replace with the user's email
    credentials = authorizer.get_credentials(user_id)

    # If credentials already exist, return them; otherwise, prompt for authorization
    if credentials.nil?
      url = authorizer.get_authorization_url(base_url: OobUrl)
      puts "Open the following URL in your browser and authorize the application: #{url}"
      # Handle the redirect and obtain the code from the user, then exchange it for credentials
      code = gets.chomp
      credentials = authorizer.get_and_store_credentials_from_code(user_id: user_id, code: code)
    end

    credentials
  end

  # Method to list user's Gmail labels
  def list_labels
    begin
      response = @service.list_user_labels('me')
      puts 'Labels:'
      puts 'No labels found' if response.labels.empty?
      response.labels.each { |label| puts "- #{label.name}" }
    rescue Google::Apis::ClientError => e
      Rails.logger.error("An error occurred: #{e.message}")
      flash[:error] = "An error occurred while fetching labels."
    end
  end

  private

  # Initialize a token store for user credentials
  def token_store
    # This is a placeholder. Implement your own token storage solution.
    # For example, using a database or file storage.
    Google::Auth::Stores::FileTokenStore.new(file: 'path/to/token.yaml')
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Define a route for listing Gmail labels
  get 'gmail/labels', to: 'gmail#list_labels'
end
```

```ruby
# config/initializers/google_api.rb

# Configure Google API client settings, if needed
Google::Apis.logger.level = Logger::DEBUG # Change to Logger::INFO in production
```

```bash
# Command to install necessary libraries
bundle install
```

```ruby
# Note:
# 1. Replace 'path/to/your/client_secret.json' and 'path/to/token.yaml' with the actual paths to your files.
# 2. Ensure that OAuth credentials are correctly set up in the Google Cloud Console.
```
