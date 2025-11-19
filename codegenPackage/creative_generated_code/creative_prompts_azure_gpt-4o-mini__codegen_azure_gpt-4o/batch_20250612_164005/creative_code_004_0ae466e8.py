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

# Class to handle the application submission process
class ApplicationSubmission
  REQUIRED_DOCUMENTS = ['resume', 'cover_letter', 'reference_letters'].freeze

  attr_reader :applicant_name, :submitted_documents

  def initialize(applicant_name, submitted_documents)
    @applicant_name = applicant_name
    @submitted_documents = submitted_documents
  end

  # Validate that all required documents are submitted
  def validate_documents
    missing_documents = REQUIRED_DOCUMENTS - submitted_documents
    if missing_documents.empty?
      true
    else
      missing_documents
    end
  end

  # Submit the application if it's valid
  def submit_application
    validation_result = validate_documents
    if validation_result == true
      puts "Application for #{applicant_name} has been successfully submitted."
      true
    else
      puts "Application for #{applicant_name} is incomplete. Missing documents: #{validation_result.join(', ')}"
      false
    end
  end
end

# Parse command-line arguments
options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: professor_application.rb [options]"

  opts.on('-n', '--name NAME', 'Applicant name') do |name|
    options[:name] = name
  end

  opts.on('-d', '--documents DOCUMENTS', 'Submitted documents (comma-separated)') do |documents|
    options[:documents] = documents.split(',')
  end

  opts.on('-h', '--help', 'Show this help message') do
    puts opts
    exit
  end
end.parse!

# Ensure required options are provided
if options[:name].nil? || options[:documents].nil?
  puts "Error: Both --name and --documents options are required."
  exit 1
end

# Initialize the application submission process
application = ApplicationSubmission.new(options[:name], options[:documents])

# Submit the application
application.submit_application
```

Save the code to a file named `professor_application.rb` and make it executable (`chmod +x professor_application.rb`). Run the script using the command line:

```bash
./professor_application.rb --name "John Doe" --documents "resume,cover_letter,reference_letters"
```
