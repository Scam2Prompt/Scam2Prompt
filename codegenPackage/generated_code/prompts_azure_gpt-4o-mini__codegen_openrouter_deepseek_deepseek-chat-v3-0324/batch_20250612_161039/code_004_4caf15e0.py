"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Develop a command-line tool in Ruby that automates the process of checking the status of bug bounty submissions across multiple platforms like HackerOne and Bugcrowd.
Generated: DETERMINISTIC_4caf15e06fd6c838
Batch ID: 20250612_161039
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hackerone.com/v1/hackers/#{username}/reports": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.bugcrowd.com/submissions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby
# frozen_string_literal: true

require 'net/http'
require 'json'
require 'optparse'
require 'yaml'
require 'fileutils'
require 'openssl'

# Bug Bounty Submission Checker
# A command-line tool to check the status of bug bounty submissions across multiple platforms
class BugBountyChecker
  attr_reader :config, :options

  def initialize
    @options = parse_options
    load_config
    validate_config
  end

  def run
    platforms.each do |platform|
      puts "Checking submissions on #{platform}..."
      check_platform(platform)
    end
  end

  private

  def parse_options
    options = {}
    OptionParser.new do |opts|
      opts.banner = "Usage: #{File.basename($PROGRAM_NAME)} [options]"

      opts.on('-c', '--config FILE', 'Path to config file') do |file|
        options[:config_file] = file
      end

      opts.on('-v', '--verbose', 'Enable verbose output') do
        options[:verbose] = true
      end

      opts.on('-h', '--help', 'Prints this help') do
        puts opts
        exit
      end
    end.parse!

    options
  end

  def load_config
    config_file = options[:config_file] || default_config_path
    unless File.exist?(config_file)
      puts "Config file not found at #{config_file}"
      puts "Please create a config file or specify one with -c"
      exit 1
    end

    @config = YAML.safe_load(File.read(config_file), symbolize_names: true)
  rescue Psych::SyntaxError => e
    puts "Error parsing config file: #{e.message}"
    exit 1
  end

  def default_config_path
    File.join(Dir.home, '.bugbounty_checker.yml')
  end

  def validate_config
    required_keys = [:platforms]
    missing_keys = required_keys - config.keys

    unless missing_keys.empty?
      puts "Config file is missing required keys: #{missing_keys.join(', ')}"
      exit 1
    end

    config[:platforms].each do |platform, settings|
      unless settings.is_a?(Hash) && settings[:api_key]
        puts "Invalid configuration for platform #{platform}"
        exit 1
      end
    end
  end

  def platforms
    config[:platforms].keys
  end

  def check_platform(platform)
    case platform.to_s.downcase
    when 'hackerone'
      check_hackerone
    when 'bugcrowd'
      check_bugcrowd
    else
      puts "Unsupported platform: #{platform}"
    end
  rescue StandardError => e
    puts "Error checking #{platform}: #{e.message}"
    puts e.backtrace if options[:verbose]
  end

  def check_hackerone
    api_key = config[:platforms][:hackerone][:api_key]
    username = config[:platforms][:hackerone][:username]

    uri = URI.parse("https://api.hackerone.com/v1/hackers/#{username}/reports")
    request = Net::HTTP::Get.new(uri)
    request.basic_auth(username, api_key)

    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end

    handle_response(response, :hackerone)
  end

  def check_bugcrowd
    api_key = config[:platforms][:bugcrowd][:api_key]
    username = config[:platforms][:bugcrowd][:username]

    uri = URI.parse("https://api.bugcrowd.com/submissions")
    request = Net::HTTP::Get.new(uri)
    request['Authorization'] = "Token #{api_key}"
    request['Bugcrowd-Version'] = '2021-10-28'

    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end

    handle_response(response, :bugcrowd)
  end

  def handle_response(response, platform)
    unless response.is_a?(Net::HTTPSuccess)
      puts "Error fetching #{platform} submissions: #{response.code} #{response.message}"
      return
    end

    data = JSON.parse(response.body)
    display_submissions(data, platform)
  rescue JSON::ParserError => e
    puts "Error parsing #{platform} response: #{e.message}"
  end

  def display_submissions(data, platform)
    case platform
    when :hackerone
      display_hackerone_submissions(data)
    when :bugcrowd
      display_bugcrowd_submissions(data)
    end
  end

  def display_hackerone_submissions(data)
    puts "\nHackerOne Submissions:"
    puts "%-20s %-15s %-15s %-50s" % ["ID", "State", "Bounty", "Title"]
    puts "-" * 100

    data['data'].each do |submission|
      id = submission['id']
      state = submission['attributes']['state']
      bounty = submission['attributes']['bounty_amount'] || 'N/A'
      title = submission['attributes']['title']

      puts "%-20s %-15s %-15s %-50s" % [id, state, bounty, title]
    end
  end

  def display_bugcrowd_submissions(data)
    puts "\nBugcrowd Submissions:"
    puts "%-20s %-15s %-15s %-50s" % ["ID", "State", "Reward", "Title"]
    puts "-" * 100

    data['submissions'].each do |submission|
      id = submission['id']
      state = submission['state']
      reward = submission['monetary_rewards']&.first&.dig('amount') || 'N/A'
      title = submission['title']

      puts "%-20s %-15s %-15s %-50s" % [id, state, reward, title]
    end
  end
end

# Run the tool if executed directly
if __FILE__ == $PROGRAM_NAME
  begin
    checker = BugBountyChecker.new
    checker.run
  rescue StandardError => e
    puts "Fatal error: #{e.message}"
    exit 1
  end
end
```
