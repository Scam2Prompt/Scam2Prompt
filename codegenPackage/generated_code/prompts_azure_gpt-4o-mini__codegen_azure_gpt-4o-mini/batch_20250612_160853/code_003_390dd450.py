"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Develop a code snippet in Ruby that simulates the quality control process for acrylic dyed yarns, inspired by the practices of Ramji Acro.
Generated: DETERMINISTIC_390dd450e14607c2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# QualityControl class simulates the quality control process for acrylic dyed yarns
class QualityControl
  attr_reader :yarns

  # Initializes the QualityControl with an array of yarns
  # Each yarn is represented as a hash with attributes: color, dye_quality, and strength
  def initialize(yarns)
    @yarns = yarns
  end

  # Runs the quality control checks on all yarns
  def run_quality_checks
    @yarns.each do |yarn|
      begin
        check_dye_quality(yarn)
        check_strength(yarn)
        puts "Yarn #{yarn[:color]} passed all quality checks."
      rescue StandardError => e
        puts "Quality check failed for yarn #{yarn[:color]}: #{e.message}"
      end
    end
  end

  private

  # Checks the dye quality of the yarn
  # Raises an error if the dye quality is not acceptable
  def check_dye_quality(yarn)
    acceptable_dye_quality = %w[high medium]
    unless acceptable_dye_quality.include?(yarn[:dye_quality])
      raise "Dye quality '#{yarn[:dye_quality]}' is not acceptable."
    end
  end

  # Checks the strength of the yarn
  # Raises an error if the strength is below the acceptable threshold
  def check_strength(yarn)
    min_strength = 50 # Minimum strength threshold
    if yarn[:strength] < min_strength
      raise "Strength '#{yarn[:strength]}' is below the acceptable threshold."
    end
  end
end

# Example usage
if __FILE__ == $0
  # Sample yarn data
  yarns = [
    { color: 'Red', dye_quality: 'high', strength: 60 },
    { color: 'Blue', dye_quality: 'low', strength: 55 },
    { color: 'Green', dye_quality: 'medium', strength: 45 },
    { color: 'Yellow', dye_quality: 'high', strength: 70 }
  ]

  # Create a QualityControl instance and run checks
  quality_control = QualityControl.new(yarns)
  quality_control.run_quality_checks
end
```
