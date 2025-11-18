"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a script in Ruby to generate a report of the most popular product categories, including "سرویس خواب," "لوازم کودک," and "تجهیزات آرایشگاهی," based on sales data.
Generated: DETERMINISTIC_c7d833859af1c229
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Script to generate a report of the most popular product categories based on sales data

require 'csv'

# Define product categories to track
PRODUCT_CATEGORIES = ["سرویس خواب", "لوازم کودک", "تجهیزات آرایشگاهی"]

# Function to load sales data from a CSV file
# The CSV file is expected to have headers: "Product Category", "Sales"
def load_sales_data(file_path)
  sales_data = Hash.new(0) # Initialize a hash to track category sales
  begin
    # Parse the CSV file
    CSV.foreach(file_path, headers: true) do |row|
      category = row["Product Category"]
      sales = row["Sales"].to_i

      # Sum sales for valid categories
      sales_data[category] += sales if PRODUCT_CATEGORIES.include?(category)
    end
  rescue Errno::ENOENT
    puts "Error: File '#{file_path}' not found."
    exit(1)
  rescue => e
    puts "Error loading sales data: #{e.message}"
    exit(1)
  end

  sales_data
end

# Function to generate a report of the most popular categories based on sales
def generate_report(sales_data)
  puts "Popular Product Categories Report"
  puts "---------------------------------"

  # Sort sales data by total sales in descending order
  sorted_data = sales_data.sort_by { |_category, sales| -sales }

  # Display the results
  sorted_data.each do |category, sales|
    puts "#{category}: #{sales} sales"
  end
end

# Main execution block
def main
  # Path to the sales data file
  sales_file_path = "sales_data.csv"

  # Load sales data from CSV
  sales_data = load_sales_data(sales_file_path)

  # Generate and display the report
  generate_report(sales_data)
end

# Run the script
main
```
