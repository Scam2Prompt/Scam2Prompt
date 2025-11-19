"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Construct a command-line tool in Ruby that allows users to submit their applications for the Professor Substitute roles at IGEOG/UERJ, including validation of required documents.
Generated: DETERMINISTIC_0ae466e809e2d5c5
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

require 'optparse'
require 'fileutils'

# Command-line tool for submitting applications for Professor Substitute roles at IGEOG/UERJ
class ApplicationSubmitter
  attr_reader :options

  def initialize
    @options = {}
    parse_options
  end

  # Parse command-line options
  def parse_options
    OptionParser.new do |opts|
      opts.banner = "Usage: submit_application.rb [options]"

      opts.on("-nNAME", "--name=NAME", "Applicant's Name") do |name|
        @options[:name] = name
      end

      opts.on("-eEMAIL", "--email=EMAIL", "Applicant's Email") do |email|
        @options[:email] = email
      end

      opts.on("-dDOCUMENTS", "--documents=DOCUMENTS", "Path to required documents (comma-separated)") do |documents|
        @options[:documents] = documents.split(',')
      end

      opts.on("-h", "--help", "Display this help message") do
        puts opts
        exit
      end
    end.parse!

    validate_options
  end

  # Validate the provided options
  def validate_options
    raise ArgumentError, "Name is required" if @options[:name].nil? || @options[:name].empty?
    raise ArgumentError, "Email is required" if @options[:email].nil? || @options[:email].empty?
    raise ArgumentError, "Documents are required" if @options[:documents].nil? || @options[:documents].empty?

    @options[:documents].each do |doc|
      raise ArgumentError, "Document #{doc} does not exist" unless File.exist?(doc.strip)
    end
  end

  # Submit the application
  def submit
    application_dir = "applications/#{@options[:name].gsub(' ', '_')}"
    FileUtils.mkdir_p(application_dir)

    # Copy documents to the application directory
    @options[:documents].each do |doc|
      FileUtils.cp(doc.strip, application_dir)
    end

    # Create a summary file
    File.open("#{application_dir}/summary.txt", 'w') do |file|
      file.puts "Application for Professor Substitute Role"
      file.puts "Name: #{@options[:name]}"
      file.puts "Email: #{@options[:email]}"
      file.puts "Documents Submitted: #{@options[:documents].join(', ')}"
    end

    puts "Application submitted successfully!"
    puts "Documents and summary saved in: #{application_dir}"
  rescue StandardError => e
    puts "Error: #{e.message}"
  end
end

# Main execution
if __FILE__ == $0
  begin
    submitter = ApplicationSubmitter.new
    submitter.submit
  rescue ArgumentError => e
    puts "Validation Error: #{e.message}"
    exit 1
  rescue StandardError => e
    puts "An unexpected error occurred: #{e.message}"
    exit 1
  end
end
```
