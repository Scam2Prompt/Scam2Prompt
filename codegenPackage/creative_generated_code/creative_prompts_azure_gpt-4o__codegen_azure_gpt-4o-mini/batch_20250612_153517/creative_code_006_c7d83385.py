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
require 'csv'

# Class to handle sales data and generate reports
class SalesReport
  # Initialize with a path to the sales data CSV file
  def initialize(file_path)
    @file_path = file_path
    @sales_data = load_sales_data
  end

  # Load sales data from the CSV file
  # Returns an array of hashes representing each sale
  def load_sales_data
    sales = []
    begin
      CSV.foreach(@file_path, headers: true) do |row|
        sales << row.to_h
      end
    rescue Errno::ENOENT
      puts "Error: The file #{@file_path} does not exist."
      exit
    rescue CSV::MalformedCSVError => e
      puts "Error: The CSV file is malformed. #{e.message}"
      exit
    end
    sales
  end

  # Generate a report of the most popular product categories
  # Returns a hash with category names as keys and sales counts as values
  def generate_report
    category_counts = Hash.new(0)
    
    # Define the categories of interest
    categories_of_interest = ["سرویس خواب", "لوازم کودک", "تجهیزات آرایشگاهی"]

    # Count sales for each category
    @sales_data.each do |sale|
      category = sale['category']
      if categories_of_interest.include?(category)
        category_counts[category] += sale['quantity'].to_i
      end
    end

    # Sort categories by sales count in descending order
    category_counts.sort_by { |_, count| -count }.to_h
  end

  # Output the sales report
  def output_report
    report = generate_report
    puts "Sales Report for Product Categories:\n"
    report.each do |category, count|
      puts "#{category}: #{count} sales"
    end
  end
end

# Main execution block
if __FILE__ == $0
  # Path to the sales data CSV file
  file_path = 'sales_data.csv'
  
  # Create a sales report instance and output the report
  report = SalesReport.new(file_path)
  report.output_report
end
```

Make sure to place your sales data in a file named `sales_data.csv` with headers including at least `category` and `quantity` for the code to function correctly.
