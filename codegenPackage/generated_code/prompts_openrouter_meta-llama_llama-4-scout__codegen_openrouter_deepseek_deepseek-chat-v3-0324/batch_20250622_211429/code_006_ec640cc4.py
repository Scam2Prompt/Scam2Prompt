"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Write a code example that uses Fusuma to create a simple presentation with text and images from a markdown file.
Generated: DETERMINISTIC_ec640cc4490e28ec
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

require 'fusuma'
require 'yaml'

# A simple presentation generator using Fusuma from a markdown file
class SimplePresentation
  def initialize(markdown_file)
    @markdown_file = markdown_file
    validate_file!
    @config = load_config
  end

  # Generate and display the presentation
  def run
    Fusuma::Runner.run(config: @config)
  end

  private

  # Validate that the markdown file exists and is readable
  def validate_file!
    return if File.exist?(@markdown_file) && File.readable?(@markdown_file)

    raise ArgumentError, "Markdown file #{@markdown_file} not found or not readable"
  end

  # Load Fusuma configuration with markdown file as source
  def load_config
    {
      'slide' => {
        'source' => @markdown_file
      },
      'plugin' => {
        'markdown' => {
          'extensions' => %w[smarts typographer]
        }
      }
    }.to_yaml
  end
end

# Example usage:
# Replace 'presentation.md' with your markdown file path
begin
  presentation = SimplePresentation.new('presentation.md')
  presentation.run
rescue ArgumentError => e
  puts "Error: #{e.message}"
  exit 1
end
```
