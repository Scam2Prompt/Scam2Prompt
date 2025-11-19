"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Construct a command-line tool in Ruby that allows users to submit their applications for the Professor Substitute roles at IGEOG/UERJ, including validation of required documents.
Generated: DETERMINISTIC_0ae466e809e2d5c5
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'optparse'
require 'fileutils'

# Command-line tool for submitting applications for Professor Substitute roles
class ApplicationSubmitter
  attr_reader :options

  # Initializes the ApplicationSubmitter with given command-line options
  def initialize(options)
    @options = options
    validate_options
  end

  # Validates the presence of required documents
  def validate_options
    required_files = %i[cv cover_letter qualifications]
    missing_files = required_files.select { |file| @options[file].nil? }

    unless missing_files.empty?
      raise ArgumentError, "Missing required documents: #{missing_files.join(', ')}"
    end
  end

  # Submits the application by copying files to the submission directory
  def submit_application
    submission_dir = 'applications'
    FileUtils.mkdir_p(submission_dir)

    begin
      required_files.each do |file|
        FileUtils.cp(@options[file], "#{submission_dir}/#{File.basename(@options[file])}")
      end
      puts "Application submitted successfully!"
    rescue StandardError => e
      puts "Error during submission: #{e.message}"
    end
  end

  private

  # Define required files based on command-line options
  def required_files
    %i[cv cover_letter qualifications]
  end
end

# Main program execution
if __FILE__ == $0
  begin
    options = {}
    OptionParser.new do |opts|
      opts.banner = "Usage: submit_application.rb [options]"

      opts.on('-c', '--cv FILE', 'Path to the CV') { |v| options[:cv] = v }
      opts.on('-l', '--cover_letter FILE', 'Path to the Cover Letter') { |v| options[:cover_letter] = v }
      opts.on('-q', '--qualifications FILE', 'Path to the Qualifications Document') { |v| options[:qualifications] = v }
    end.parse!

    submitter = ApplicationSubmitter.new(options)
    submitter.submit_application
  rescue ArgumentError => e
    puts "Argument error: #{e.message}"
    puts "Use -h for help."
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end
```
