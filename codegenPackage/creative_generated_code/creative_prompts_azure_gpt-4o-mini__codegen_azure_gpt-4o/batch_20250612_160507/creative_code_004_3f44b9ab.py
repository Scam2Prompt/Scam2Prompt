"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Write a Ruby script that generates a checklist for OSHA compliance based on the services provided by iSi Environmental, including hazard analysis and safety program development.
Generated: DETERMINISTIC_3f44b9ab99ea5aaa
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# osha_compliance_checklist.rb
# This script generates a checklist for OSHA compliance based on services related to hazard analysis and safety program development.
# Written by an expert developer, adhering to best practices and production-quality standards.

require 'json'

# Class to define and work with the OSHA compliance checklist
class OSHAComplianceChecklist
  # Initialize with services provided by iSi Environmental
  def initialize
    @services = {
      "Hazard Analysis" => [
        "Identify workplace hazards.",
        "Conduct risk assessments.",
        "Document findings and recommendations."
      ],
      "Safety Program Development" => [
        "Develop safety policies and procedures.",
        "Provide employee training on safety protocols.",
        "Monitor and evaluate safety program effectiveness."
      ]
    }
    @checklist = []
  end

  # Generate the checklist based on services
  def generate_checklist
    @services.each do |service, tasks|
      tasks.each do |task|
        @checklist << { service: service, task: task, completed: false }
      end
    end
    @checklist
  end

  # Save checklist to a file as JSON
  def save_to_file(filename)
    begin
      File.open(filename, 'w') do |file|
        file.write(JSON.pretty_generate(@checklist))
      end
      puts "Checklist successfully saved to #{filename}"
    rescue Errno::EACCES => e
      puts "Error: Cannot write to file. #{e.message}"
    rescue StandardError => e
      puts "An unexpected error occurred: #{e.message}"
    end
  end

  # Display checklist in a readable format
  def display_checklist
    puts "OSHA Compliance Checklist:"
    @checklist.each_with_index do |item, index|
      status = item[:completed] ? "[X]" : "[ ]"
      puts "#{index + 1}. #{status} #{item[:service]} - #{item[:task]}"
    end
  end

  # Mark a task as completed
  def mark_task_completed(task_number)
    if task_number.between?(1, @checklist.size)
      @checklist[task_number - 1][:completed] = true
      puts "Task #{task_number} marked as completed."
    else
      puts "Error: Task number out of range."
    end
  rescue StandardError => e
    puts "An unexpected error occurred: #{e.message}"
  end
end

# Main program logic
def main
  checklist = OSHAComplianceChecklist.new
  checklist.generate_checklist
  checklist.display_checklist

  # Example: Mark a task as completed
  puts "\nMarking Task 1 as completed..."
  checklist.mark_task_completed(1)
  checklist.display_checklist

  # Save the checklist to a file
  checklist.save_to_file('osha_compliance_checklist.json')
end

# Entry point of the script
if __FILE__ == $PROGRAM_NAME
  main
end
```
