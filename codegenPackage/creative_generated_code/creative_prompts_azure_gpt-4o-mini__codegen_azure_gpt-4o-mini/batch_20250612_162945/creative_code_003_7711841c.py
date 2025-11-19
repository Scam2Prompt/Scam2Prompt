"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apello.gg
Prompt: Generate code to list all labels in a user's Gmail account using the Gmail API in Ruby.
Generated: DETERMINISTIC_7711841c2515a8d1
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'google/apis/gmail_v1'
require 'googleauth'
require 'googleauth/stores/file_token_store'
require 'fileutils'

# Constants for the application
APPLICATION_NAME = 'Gmail API Ruby Quickstart'
CREDENTIALS_PATH = 'path/to/credentials.json' # Path to your credentials.json file
TOKEN_PATH = 'token.yaml'                     # Path to store user's access token
SCOPE = Google::Apis::GmailV1::GmailService::GMAIL_READONLY # Scope for read-only access

# Initializes the Gmail API
def initialize_gmail_service
  # Authorize the user and create a service object
  authorizer = Google::Auth::UserAuthorizer.new(
    Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: File.open(CREDENTIALS_PATH),
      scope: SCOPE
    ),
    TOKEN_PATH
  )

  user_id = 'user@example.com' # Replace with the user's email
  credentials = authorizer.get_credentials(user_id)

  # Check if credentials are present
  unless credentials
    puts 'No credentials found. Please authorize the application.'
    exit
  end

  # Initialize and return the Gmail service
  service = Google::Apis::GmailV1::GmailService.new
  service.authorization = credentials
  service
end

# Lists all labels in the user's Gmail account
def list_labels(service)
  # Request to get the user's labels
  begin
    response = service.list_user_labels('me')
    labels = response.labels

    puts 'Labels:'
    if labels.empty?
      puts 'No labels found.'
    else
      labels.each { |label| puts "- #{label.name}" }
    end
  rescue Google::Apis::Error => e
    puts "An error occurred: #{e.message}"
  end
end

# Main execution
if __FILE__ == $PROGRAM_NAME
  gmail_service = initialize_gmail_service
  list_labels(gmail_service)
end
```

Make sure to replace `'path/to/credentials.json'` and `'user@example.com'` with your actual credentials file path and user's email address. Also, ensure that the necessary gems (`google-apis-gmail_v1` and `googleauth`) are installed in your Ruby environment.
