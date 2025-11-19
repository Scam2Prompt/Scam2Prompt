"""
Generated Code Metadata:
========================
Original URL: https://apello.gg
Prompt: Generate code to list all labels in a user's Gmail account using the Gmail API in Ruby.
Generated: DETERMINISTIC_7711841c2515a8d1
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
require 'google/apis/gmail_v1'
require 'googleauth'
require 'googleauth/stores/file_token_store'
require 'fileutils'

# Configuration for the Gmail API
OOB_URI = 'urn:ietf:wg:oauth:2.0:oob'
APPLICATION_NAME = 'Gmail API Ruby Quickstart'
CLIENT_SECRETS_PATH = 'client_secret.json'
CREDENTIALS_PATH = 'token.yaml'
SCOPE = Google::Apis::GmailV1::AUTH_GMAIL_READONLY

##
# Ensure valid credentials, either by restoring from the saved credentials
# files or initiating an OAuth2 authorization. If authorization is required,
# the user's default browser will be launched to approve the request.
#
# @return [Google::Auth::UserRefreshCredentials] OAuth2 credentials
def authorize
  client_id = Google::Auth::ClientId.from_file(CLIENT_SECRETS_PATH)
  token_store = Google::Auth::Stores::FileTokenStore.new(file: CREDENTIALS_PATH)
  authorizer = Google::Auth::UserAuthorizer.new(client_id, SCOPE, token_store)
  user_id = 'default'
  credentials = authorizer.get_credentials(user_id)
  if credentials.nil?
    url = authorizer.get_authorization_url(base_url: OOB_URI)
    puts 'Open the following URL in the browser and enter the resulting code after authorization:'
    puts url
    code = gets
    credentials = authorizer.get_and_store_credentials_from_code(
      user_id: user_id, code: code, base_url: OOB_URI
    )
  end
  credentials
end

# Initialize the API
service = Google::Apis::GmailV1::GmailService.new
service.client_options.application_name = APPLICATION_NAME
service.authorization = authorize

begin
  # Fetch all labels from the user's Gmail account
  response = service.list_user_labels('me')

  # Display the labels
  puts 'Labels:'
  puts 'No labels found' if response.labels.empty?
  response.labels.each do |label|
    puts "- #{label.name}"
  end
rescue Google::Apis::ServerError, Google::Apis::ClientError, Google::Apis::AuthorizationError => e
  puts "An error occurred: #{e.message}"
end
```
