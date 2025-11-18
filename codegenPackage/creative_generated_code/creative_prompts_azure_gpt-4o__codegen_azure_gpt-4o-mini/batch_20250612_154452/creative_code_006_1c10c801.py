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
require 'prawn'
require 'fileutils'

# Class to handle certificate generation
class CertificateGenerator
  # Initialize with a list of participants and output directory
  def initialize(participants, output_dir)
    @participants = participants
    @output_dir = output_dir
    create_output_directory
  end

  # Generate certificates for all participants
  def generate_certificates
    @participants.each do |participant|
      begin
        create_certificate(participant)
      rescue StandardError => e
        puts "Error generating certificate for #{participant[:name]}: #{e.message}"
      end
    end
  end

  private

  # Create output directory if it doesn't exist
  def create_output_directory
    FileUtils.mkdir_p(@output_dir) unless Dir.exist?(@output_dir)
  end

  # Create a PDF certificate for a single participant
  def create_certificate(participant)
    Prawn::Document.generate(certificate_file_path(participant[:name])) do |pdf|
      pdf.text "Certificate of Attendance", align: :center, size: 30, style: :bold
      pdf.move_down 20
      pdf.text "This certifies that", align: :center, size: 20
      pdf.move_down 10
      pdf.text participant[:name], align: :center, size: 25, style: :bold
      pdf.move_down 20
      pdf.text "has attended the conference", align: :center, size: 20
      pdf.move_down 10
      pdf.text "on #{participant[:date]}", align: :center, size: 20
      pdf.move_down 30
      pdf.text "Signature", align: :right, size: 20
    end
  end

  # Generate the file path for the participant's certificate
  def certificate_file_path(name)
    cleaned_name = name.gsub(/[^0-9A-Za-z.\-]/, '_') # Sanitize the name for file system
    File.join(@output_dir, "#{cleaned_name}_certificate.pdf")
  end
end

# Sample participants data
participants = [
  { name: "John Doe", date: "March 10, 2023" },
  { name: "Jane Smith", date: "March 10, 2023" },
  { name: "Emily Johnson", date: "March 10, 2023" }
]

# Main execution
if __FILE__ == $0
  output_directory = "certificates"
  generator = CertificateGenerator.new(participants, output_directory)
  generator.generate_certificates
  puts "Certificates have been generated and saved to #{output_directory}."
end
```
