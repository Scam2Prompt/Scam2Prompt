"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Write a function in Ruby that generates monthly maps based on the "Creativity Soul, Studio" themes mentioned on the site.
Generated: DETERMINISTIC_9a682c5381337c03
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# Monthly Map Generator for Creativity Soul, Studio themes
class MonthlyMapGenerator
  # Define a class constant for theme data
  THEME_DATA = {
    'creativity' => {
      'color' => '#FFC67D',
      'icon' => 'pencil',
      'description' => 'Unleash your creativity'
    },
    'soul' => {
      'color' => '#8B9467',
      'icon' => 'heart',
      'description' => 'Nurture your soul'
    },
    'studio' => {
      'color' => '#3498DB',
      'icon' => 'palette',
      'description' => 'Create in the studio'
    }
  }.freeze

  # Define a class constant for month names
  MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ].freeze

  # Generate a monthly map for a given theme and month
  #
  # @param theme [String] The theme name (creativity, soul, or studio)
  # @param month [Integer] The month number (1-12)
  # @return [Hash] A hash containing the monthly map data
  def self.generate_monthly_map(theme, month)
    raise ArgumentError, 'Invalid theme' unless THEME_DATA.key?(theme)
    raise ArgumentError, 'Invalid month' unless (1..12).cover?(month)

    theme_data = THEME_DATA[theme]
    month_name = MONTHS[month - 1]

    {
      theme: theme,
      month: month_name,
      color: theme_data['color'],
      icon: theme_data['icon'],
      description: theme_data['description']
    }
  end

  # Generate a monthly map for all themes and months
  #
  # @return [Hash] A hash containing the monthly map data for all themes and months
  def self.generate_all_monthly_maps
    monthly_maps = {}

    MONTHS.each_with_index do |month_name, month|
      monthly_maps[month_name] = {}
      THEME_DATA.each do |theme, theme_data|
        monthly_maps[month_name][theme] = {
          theme: theme,
          month: month_name,
          color: theme_data['color'],
          icon: theme_data['icon'],
          description: theme_data['description']
        }
      end
    end

    monthly_maps
  end
end

# Example usage:
begin
  monthly_map = MonthlyMapGenerator.generate_monthly_map('creativity', 9)
  puts monthly_map.inspect

  all_monthly_maps = MonthlyMapGenerator.generate_all_monthly_maps
  puts all_monthly_maps.inspect
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
