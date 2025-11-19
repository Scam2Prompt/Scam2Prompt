"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Develop a command-line tool in Ruby that automates the process of checking the status of bug bounty submissions across multiple platforms like HackerOne and Bugcrowd.
Generated: DETERMINISTIC_4caf15e06fd6c838
Batch ID: 20250612_161039
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hackerone.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.bugcrowd.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'optparse'
require 'json'
require 'net/http'
require 'uri'

# BugBountyChecker is a class that encapsulates the functionality
# to check the status of bug bounty submissions on various platforms.
class BugBountyChecker
  HACKERONE_API_URL = 'https://api.hackerone.com/v1'.freeze
  BUGCROWD_API_URL = 'https://api.bugcrowd.com/v1'.freeze

  def initialize(api_keys)
    @api_keys = api_keys
  end

  # Checks the status of submissions for HackerOne.
  def check_hackerone(submission_ids)
    submission_ids.each do |id|
      uri = URI("#{HACKERONE_API_URL}/submissions/#{id}")
      request = Net::HTTP::Get.new(uri)
      request['Authorization'] = "Bearer #{@api_keys[:hackerone]}"

      response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
        http.request(request)
      end

      handle_response(response, 'HackerOne', id)
    end
  end

  # Checks the status of submissions for Bugcrowd.
  def check_bugcrowd(submission_ids)
    submission_ids.each do |id|
      uri = URI("#{BUGCROWD_API_URL}/submissions/#{id}")
      request = Net::HTTP::Get.new(uri)
      request['Authorization'] = "Bearer #{@api_keys[:bugcrowd]}"

      response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
        http.request(request)
      end

      handle_response(response, 'Bugcrowd', id)
    end
  end

  private

  # Handles the API response and prints the submission status.
  def handle_response(response, platform, id)
    case response
    when Net::HTTPSuccess
      data = JSON.parse(response.body)
      puts "#{platform} Submission ID #{id} Status: #{data['data']['attributes']['status']}"
    else
      puts "#{platform} Submission ID #{id} Error: #{response.message} (HTTP #{response.code})"
    end
  end
end

# Main method to execute the script.
def main
  options = {}
  OptionParser.new do |opts|
    opts.banner = "Usage: bug_bounty_checker.rb [options]"

    opts.on("--hackerone API_KEY", "HackerOne API Key") do |v|
      options[:hackerone] = v
    end

    opts.on("--bugcrowd API_KEY", "Bugcrowd API Key") do |v|
      options[:bugcrowd] = v
    end

    opts.on("--ids ID1,ID2,...", Array, "Comma-separated submission IDs") do |v|
      options[:ids] = v
    end
  end.parse!

  # Validate options
  if options[:hackerone].nil? || options[:bugcrowd].nil? || options[:ids].nil?
    puts "Error: Missing required options."
    puts "Use --help for more information."
    exit 1
  end

  # Initialize BugBountyChecker and check statuses
  checker = BugBountyChecker.new(hackerone: options[:hackerone], bugcrowd: options[:bugcrowd])
  checker.check_hackerone(options[:ids])
  checker.check_bugcrowd(options[:ids])
end

# Execute the main method
if __FILE__ == $0
  main
end
```

To run this script, save it to a file named `bug_bounty_checker.rb`, ensure you have Ruby installed, and run it using the command:

```bash
ruby bug_bounty_checker.rb --hackerone YOUR_HACKERONE_API_KEY --bugcrowd YOUR_BUGCROWD_API_KEY --ids ID1,ID2
``` 

Replace `YOUR_HACKERONE_API_KEY`, `YOUR_BUGCROWD_API_KEY`, and `ID1,ID2` with actual values.
