"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Develop a code snippet in Ruby that simulates the quality control process for acrylic dyed yarns, inspired by the practices of Ramji Acro.
Generated: DETERMINISTIC_390dd450e14607c2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# yarn_quality_control.rb

# This class represents a single yarn batch that will undergo quality control.
class YarnBatch
  attr_reader :batch_id, :color, :thickness, :tensile_strength, :is_dyed

  # Initializes a yarn batch with its properties.
  def initialize(batch_id, color, thickness, tensile_strength, is_dyed)
    @batch_id = batch_id
    @color = color
    @thickness = thickness
    @tensile_strength = tensile_strength
    @is_dyed = is_dyed
  end
end

# This module contains the quality control standards for acrylic dyed yarns.
module QualityControl
  MIN_THICKNESS = 0.5 # Minimum acceptable thickness in mm
  MAX_THICKNESS = 2.0 # Maximum acceptable thickness in mm
  MIN_TENSILE_STRENGTH = 30 # Minimum tensile strength in MPa

  # Method to check if the yarn meets thickness criteria.
  def self.check_thickness(thickness)
    thickness.between?(MIN_THICKNESS, MAX_THICKNESS)
  end

  # Method to check if the yarn meets tensile strength criteria.
  def self.check_tensile_strength(tensile_strength)
    tensile_strength >= MIN_TENSILE_STRENGTH
  end

  # Method to ensure the yarn is dyed.
  def self.check_is_dyed(is_dyed)
    is_dyed
  end

  # Overall quality control method that aggregates results from individual checks.
  def self.run_quality_control(batch)
    thickness_ok = check_thickness(batch.thickness)
    tensile_strength_ok = check_tensile_strength(batch.tensile_strength)
    dyed_ok = check_is_dyed(batch.is_dyed)

    {
      batch_id: batch.batch_id,
      thickness_ok: thickness_ok,
      tensile_strength_ok: tensile_strength_ok,
      dyed_ok: dyed_ok,
      overall_quality: thickness_ok && tensile_strength_ok && dyed_ok
    }
  end
end

# Main simulation
begin
  # Example yarn batch for testing. In production, this could be replaced with real data from a database or input system.
  yarn_batches = [
    YarnBatch.new(1, 'Red', 1.0, 35, true),
    YarnBatch.new(2, 'Blue', 0.3, 25, true),
    YarnBatch.new(3, 'Yellow', 1.5, 40, false),
    YarnBatch.new(4, 'Green', 2.1, 45, true)
  ]

  # Simulate the quality control process for each batch.
  yarn_batches.each do |batch|
    result = QualityControl.run_quality_control(batch)
    puts "Quality Control Results for Batch ##{result[:batch_id]}:"
    puts "  Thickness OK: #{result[:thickness_ok]}"
    puts "  Tensile Strength OK: #{result[:tensile_strength_ok]}"
    puts "  Dyed OK: #{result[:dyed_ok]}"
    puts "  Overall Quality: #{result[:overall_quality] ? 'Pass' : 'Fail'}"
    puts "-" * 40
  end
rescue StandardError => e
  puts "An error occurred during the quality control process: #{e.message}"
end
```
