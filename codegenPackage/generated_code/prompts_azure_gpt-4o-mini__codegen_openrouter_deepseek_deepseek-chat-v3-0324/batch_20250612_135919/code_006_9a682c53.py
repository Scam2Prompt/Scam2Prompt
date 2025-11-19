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

require 'date'
require 'json'

module CreativitySoulStudio
  # Generates monthly theme maps based on Creativity Soul Studio themes
  class ThemeMapGenerator
    THEMES = {
      'January'   => 'Renewal & Fresh Starts',
      'February'  => 'Love & Connection',
      'March'     => 'Growth & Transformation',
      'April'     => 'Creativity & Inspiration',
      'May'       => 'Abundance & Prosperity',
      'June'      => 'Joy & Celebration',
      'July'      => 'Freedom & Adventure',
      'August'    => 'Strength & Resilience',
      'September' => 'Balance & Harmony',
      'October'   => 'Mystery & Intuition',
      'November'  => 'Gratitude & Reflection',
      'December'  => 'Magic & Wonder'
    }.freeze

    # Generates a theme map for the current month
    # @return [Hash] containing month name and theme
    def self.current_month_theme
      month = Date.today.strftime('%B')
      { month: month, theme: THEMES[month] }
    end

    # Generates theme maps for all months
    # @return [Array<Hash>] array of month/theme hashes
    def self.all_months_themes
      THEMES.map { |month, theme| { month: month, theme: theme } }
    end

    # Generates a theme map for a specific month
    # @param month_name [String] full month name (e.g., "January")
    # @return [Hash] containing month name and theme
    # @raise [ArgumentError] if month_name is invalid
    def self.month_theme(month_name)
      month_name = month_name.capitalize
      unless THEMES.key?(month_name)
        raise ArgumentError, "Invalid month name: #{month_name}"
      end

      { month: month_name, theme: THEMES[month_name] }
    end

    # Generates a JSON representation of all themes
    # @param pretty [Boolean] whether to format JSON with indentation
    # @return [String] JSON string
    def self.themes_to_json(pretty: false)
      if pretty
        JSON.pretty_generate(all_months_themes)
      else
        all_months_themes.to_json
      end
    end
  end
end
```
