"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write a Ruby script that generates a checklist for OSHA compliance based on the services provided by iSi Environmental, including hazard analysis and safety program development.
Generated: DETERMINISTIC_3f44b9ab99ea5aaa
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby
# OSHA Compliance Checklist Generator
# Based on iSi Environmental services: hazard analysis and safety program development

require 'yaml'
require 'optparse'

class OSHAComplianceChecklist
  attr_reader :company_name, :services, :checklist

  def initialize(company_name, services)
    @company_name = company_name
    @services = services
    @checklist = generate_checklist
  end

  # Generate checklist based on selected services
  def generate_checklist
    checklist = {
      general: [
        "Written safety and health program",
        "Management leadership and employee participation",
        "Hazard identification and assessment",
        "Hazard prevention and control",
        "Education and training",
        "Program evaluation and improvement"
      ],
      hazard_analysis: [
        "Chemical hazard assessment completed",
        "Physical hazard assessment completed",
        "Biological hazard assessment completed",
        "Ergonomic hazard assessment completed",
        "Hazard assessment documentation maintained",
        "Regular reassessment schedule established"
      ],
      safety_program: [
        "Emergency action plan developed",
        "Fire prevention plan in place",
        "Personal protective equipment (PPE) program",
        "Lockout/Tagout procedures for hazardous energy",
        "Confined space entry program",
        "Respiratory protection program",
        "Hearing conservation program",
        "Bloodborne pathogens exposure control plan"
      ]
    }

    selected_items = checklist[:general].dup

    if @services.include?(:hazard_analysis)
      selected_items += checklist[:hazard_analysis]
    end

    if @services.include?(:safety_program)
      selected_items += checklist[:safety_program]
    end

    selected_items
  end

  # Export checklist to YAML file
  def export_to_yaml(filename)
    File.open(filename, 'w') do |file|
      file.write({
        company_name: @company_name,
        services: @services.map(&:to_s),
        checklist_items: @checklist,
        generated_at: Time.now.strftime("%Y-%m-%d %H:%M:%S")
      }.to_yaml)
    end
  rescue => e
    puts "Error exporting checklist: #{e.message}"
  end

  # Print checklist to console
  def print_checklist
    puts "\nOSHA Compliance Checklist for #{@company_name}"
    puts "=" * 50
    puts "Selected Services: #{@services.join(', ')}"
    puts "\nChecklist Items:"
    @checklist.each_with_index do |item, index|
      puts "#{index + 1}. #{item}"
    end
    puts "\nGenerated on #{Time.now.strftime("%Y-%m-%d")}"
  end
end

# Command line options parsing
options = {
  services: [],
  output_file: nil
}

OptionParser.new do |opts|
  opts.banner = "Usage: osha_checklist.rb [options]"

  opts.on("-n", "--name NAME", "Company name") do |name|
    options[:company_name] = name
  end

  opts.on("-s", "--services x,y,z", Array, "Services (hazard_analysis,safety_program)") do |services|
    options[:services] = services.map(&:to_sym)
  end

  opts.on("-o", "--output FILE", "Output YAML file") do |file|
    options[:output_file] = file
  end

  opts.on("-h", "--help", "Prints this help") do
    puts opts
    exit
  end
end.parse!

# Validate input
if options[:company_name].nil? || options[:company_name].empty?
  puts "Error: Company name is required"
  exit 1
end

if options[:services].empty?
  puts "Error: At least one service must be selected"
  exit 1
end

# Generate and output checklist
begin
  checklist = OSHAComplianceChecklist.new(options[:company_name], options[:services])
  checklist.print_checklist

  if options[:output_file]
    checklist.export_to_yaml(options[:output_file])
    puts "\nChecklist exported to #{options[:output_file]}"
  end
rescue => e
  puts "Error generating checklist: #{e.message}"
  exit 1
end
```
