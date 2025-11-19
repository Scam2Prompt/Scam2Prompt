"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Develop a command-line tool in Ruby that automates the process of checking the status of bug bounty submissions across multiple platforms like HackerOne and Bugcrowd.
Generated: DETERMINISTIC_4caf15e06fd6c838
Batch ID: 20250612_161039
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.hackerone.com/v1/submissions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://tracker.bugcrowd.com/api/submissions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hackerone.com/v1/submissions`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://tracker.bugcrowd.com/api/submissions`": {
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

require 'net/http'
require 'json'
require 'optparse'

# A command-line tool to check the status of bug bounty submissions across multiple platforms.
# Supports HackerOne and Bugcrowd.

class BugBountyChecker
  # Initialize the checker with API credentials
  def initialize(options)
    @hackerone_api_key = options[:hackerone_api_key]
    @bugcrowd_api_key = options[:bugcrowd_api_key]
  end

  # Check submission status for HackerOne
  def check_hackerone_status
    return unless @hackerone_api_key

    puts "Checking HackerOne submissions..."
    url = URI("https://api.hackerone.com/v1/submissions")
    request = Net::HTTP::Get.new(url)
    request['Authorization'] = "Bearer #{@hackerone_api_key}"

    response = Net::HTTP.start(url.hostname, url.port, use_ssl: true) do |http|
      http.request(request)
    end

    if response.code.to_i == 200
      data = JSON.parse(response.body)
      puts "HackerOne submissions:"
      data['submissions'].each do |submission|
        puts "ID: #{submission['id']}, Title: #{submission['title']}, Status: #{submission['state']}"
      end
    else
      puts "Error fetching HackerOne submissions: #{response.message}"
    end
  end

  # Check submission status for Bugcrowd
  def check_bugcrowd_status
    return unless @bugcrowd_api_key

    puts "Checking Bugcrowd submissions..."
    url = URI("https://tracker.bugcrowd.com/api/submissions")
    request = Net::HTTP::Get.new(url)
    request['Authorization'] = "Token #{@bugcrowd_api_key}"

    response = Net::HTTP.start(url.hostname, url.port, use_ssl: true) do |http|
      http.request(request)
    end

    if response.code.to_i == 200
      data = JSON.parse(response.body)
      puts "Bugcrowd submissions:"
      data['submissions'].each do |submission|
        puts "ID: #{submission['id']}, Title: #{submission['title']}, Status: #{submission['state']}"
      end
    else
      puts "Error fetching Bugcrowd submissions: #{response.message}"
    end
  end

  # Main method to run the tool
  def run
    check_hackerone_status
    check_bugcrowd_status
  end
end

# Parse command-line options
options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: bug_bounty_checker.rb [options]"

  opts.on("--hackerone-api-key KEY", "HackerOne API Key") do |key|
    options[:hackerone_api_key] = key
  end

  opts.on("--bugcrowd-api-key KEY", "Bugcrowd API Key") do |key|
    options[:bugcrowd_api_key] = key
  end
end.parse!

# Validate options
if options.empty?
  puts "Error: API keys are required."
  puts "Run 'bug_bounty_checker.rb --help' for usage information."
  exit(1)
end

# Run the Bug Bounty Checker tool
checker = BugBountyChecker.new(options)
checker.run
```

### Notes:
1. Replace `https://api.hackerone.com/v1/submissions` and `https://tracker.bugcrowd.com/api/submissions` with the actual API endpoints if they differ.
2. Ensure you have valid API keys for HackerOne and Bugcrowd to run this script.
3. This tool is designed to check submission statuses for platforms that provide APIs for access; update headers and authentication methods as required for production use.
