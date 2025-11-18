"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Write a script in Ruby to automate the generation of certificates of attendance for conference participants, ensuring the certificates are available at the conference desk as described on Conferences Global.
Generated: DETERMINISTIC_1c10c8010d6b2040
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'erb'
require 'fileutils'
require 'csv'

# Conference details
CONFERENCE_NAME = "Conferences Global 2023"
CERTIFICATE_TEMPLATE = <<-HTML
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 50px;
    }
    .certificate {
      border: 5px solid #000;
      padding: 20px;
      margin: 20px auto;
      width: 80%;
    }
    h1 {
      font-size: 24px;
    }
    p {
      font-size: 18px;
    }
    .participant-name {
      font-weight: bold;
      font-size: 22px;
    }
  </style>
</head>
<body>
  <div class="certificate">
    <h1>Certificate of Attendance</h1>
    <p>This is to certify that</p>
    <p class="participant-name"><%= name %></p>
    <p>has attended <strong><%= conference_name %></strong>.</p>
    <p>Date: <%= date %></p>
  </div>
</body>
</html>
HTML

# Paths for input and output
PARTICIPANTS_FILE = 'participants.csv' # Input CSV file containing participant names
OUTPUT_FOLDER = 'certificates' # Folder where certificates will be generated

# Ensure the output folder exists
FileUtils.mkdir_p(OUTPUT_FOLDER)

# Error handling for input file
unless File.exist?(PARTICIPANTS_FILE)
  abort("Error: Participants file '#{PARTICIPANTS_FILE}' not found.")
end

begin
  # Load participants from the CSV file
  participants = CSV.read(PARTICIPANTS_FILE, headers: true)
rescue StandardError => e
  abort("Error reading participants file: #{e.message}")
end

# Generate certificates for each participant
participants.each do |row|
  name = row['Name']
  if name.nil? || name.strip.empty?
    puts "Warning: Skipping empty or invalid participant name."
    next
  end

  # Render certificate content using ERB
  erb_template = ERB.new(CERTIFICATE_TEMPLATE)
  certificate_content = erb_template.result_with_hash(
    name: name.strip,
    conference_name: CONFERENCE_NAME,
    date: Time.now.strftime('%B %d, %Y')
  )

  # Write the certificate to an HTML file
  certificate_file = File.join(OUTPUT_FOLDER, "#{name.strip.gsub(/[^0-9A-Za-z]/, '_')}_certificate.html")
  begin
    File.write(certificate_file, certificate_content)
  rescue StandardError => e
    puts "Error writing certificate for '#{name}': #{e.message}"
    next
  end

  puts "Generated certificate for '#{name}' at #{certificate_file}"
end

puts "All certificates have been generated in the '#{OUTPUT_FOLDER}' folder."
```
