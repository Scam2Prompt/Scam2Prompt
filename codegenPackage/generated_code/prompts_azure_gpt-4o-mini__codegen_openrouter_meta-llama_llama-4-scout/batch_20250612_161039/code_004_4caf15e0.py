"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Develop a command-line tool in Ruby that automates the process of checking the status of bug bounty submissions across multiple platforms like HackerOne and Bugcrowd.
Generated: DETERMINISTIC_4caf15e06fd6c838
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

require 'json'
require 'net/http'
require 'uri'
require 'optparse'

# Define a class for Bug Bounty platforms
class BugBountyPlatform
  attr_accessor :name, :api_url, :api_key

  def initialize(name, api_url, api_key)
    @name = name
    @api_url = api_url
    @api_key = api_key
  end

  # Method to get submissions from the platform
  def get_submissions
    uri = URI.parse(api_url)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true if uri.scheme == 'https'

    request = Net::HTTP::Get.new(uri.request_uri)
    request['Authorization'] = "Bearer #{api_key}"

    response = http.request(request)

    if response.code == '200'
      JSON.parse(response.body)
    else
      []
    end
  rescue StandardError => e
    puts "Error fetching submissions from #{name}: #{e.message}"
    []
  end
end

# Define a class for HackerOne
class HackerOne < BugBountyPlatform
  def initialize(api_url, api_key)
    super('HackerOne', api_url, api_key)
  end

  # Method to get submissions from HackerOne
  def get_submissions
    super
  end
end

# Define a class for Bugcrowd
class Bugcrowd < BugBountyPlatform
  def initialize(api_url, api_key)
    super('Bugcrowd', api_url, api_key)
  end

  # Method to get submissions from Bugcrowd
  def get_submissions
    super
  end
end

# Main function to check bug bounty submissions
def check_submissions(platforms)
  platforms.each do |platform|
    puts "Checking submissions on #{platform.name}..."
    submissions = platform.get_submissions

    if submissions.empty?
      puts "No submissions found on #{platform.name}."
    else
      puts "Submissions on #{platform.name}:"
      submissions.each do |submission|
        puts "  - ID: #{submission['id']}, Status: #{submission['status']}"
      end
    end
  end
end

# Parse command-line options
options = {}
OptionParser.new do |opts|
  opts.banner = 'Usage: bug_bounty_checker [options]'

  opts.on('-k', '--hackerone-api-key KEY', 'HackerOne API key') do |v|
    options[:hackerone_api_key] = v
  end

  opts.on('-b', '--bugcrowd-api-key KEY', 'Bugcrowd API key') do |v|
    options[:bugcrowd_api_key] = v
  end

  opts.on('-u', '--hackerone-api-url URL', 'HackerOne API URL') do |v|
    options[:hackerone_api_url] = v
  end

  opts.on('-v', '--bugcrowd-api-url URL', 'Bugcrowd API URL') do |v|
    options[:bugcrowd_api_url] = v
  end

  opts.on('-h', '--help', 'Prints this help') do
    puts opts
    exit
  end
end.parse!

# Create platforms and check submissions
platforms = []

if options[:hackerone_api_key] && options[:hackerone_api_url]
  hackerone = HackerOne.new(options[:hackerone_api_url], options[:hackerone_api_key])
  platforms << hackerone
end

if options[:bugcrowd_api_key] && options[:bugcrowd_api_url]
  bugcrowd = Bugcrowd.new(options[:bugcrowd_api_url], options[:bugcrowd_api_key])
  platforms << bugcrowd
end

if platforms.empty?
  puts 'No platforms configured.'
else
  check_submissions(platforms)
end
```
