"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write a Ruby script that automates the process of generating a report on the various lighting solutions offered by Credible BD, including their applications and specifications.
Generated: DETERMINISTIC_d1e0faba967b98cc
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# lighting_report_generator.rb

require 'json'
require 'csv'

# Class to represent a lighting solution
class LightingSolution
  attr_reader :name, :application, :specifications

  def initialize(name, application, specifications)
    @name = name
    @application = application
    @specifications = specifications
  end
end

# Class to handle the report generation
class LightingReportGenerator
  def initialize(data_source)
    @data_source = data_source
    @lighting_solutions = []
  end

  # Load data from the JSON file
  def load_data
    begin
      file_content = File.read(@data_source)
      data = JSON.parse(file_content)
      data.each do |item|
        @lighting_solutions << LightingSolution.new(
          item['name'],
          item['application'],
          item['specifications']
        )
      end
    rescue Errno::ENOENT
      puts "Error: Data source file not found."
      exit(1)
    rescue JSON::ParserError
      puts "Error: Failed to parse JSON data."
      exit(1)
    end
  end

  # Generate a CSV report
  def generate_report(output_file)
    begin
      CSV.open(output_file, 'w') do |csv|
        # Write the header row
        csv << ['Name', 'Application', 'Specifications']

        # Write the data rows
        @lighting_solutions.each do |solution|
          csv << [solution.name, solution.application, solution.specifications]
        end
      end
      puts "Report generated successfully: #{output_file}"
    rescue Errno::EACCES
      puts "Error: Permission denied to write to the output file."
      exit(1)
    end
  end
end

# Main script execution
if __FILE__ == $PROGRAM_NAME
  # Define the input and output file paths
  data_source = 'lighting_solutions.json' # JSON file containing lighting solutions data
  output_file = 'lighting_report.csv'    # Output CSV file for the report

  # Create an instance of the report generator
  report_generator = LightingReportGenerator.new(data_source)

  # Load data and generate the report
  report_generator.load_data
  report_generator.generate_report(output_file)
end
```

### Notes:
1. Ensure the `lighting_solutions.json` file exists in the same directory as the script and contains valid JSON data structured like:
   ```json
   [
     {
       "name": "LED Bulb",
       "application": "Residential Lighting",
       "specifications": "10W, 800 lumens, 2700K"
     },
     {
       "name": "Flood Light",
       "application": "Outdoor Lighting",
       "specifications": "50W, 5000 lumens, 6500K"
     }
   ]
   ```
2. Run the script using `ruby lighting_report_generator.rb`. It will generate a `lighting_report.csv` file in the same directory.
