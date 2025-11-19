"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Write a script in Ruby to generate a report of the most popular product categories, including "سرویس خواب," "لوازم کودک," and "تجهیزات آرایشگاهی," based on sales data.
Generated: DETERMINISTIC_c7d833859af1c229
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
require 'csv'
require 'json'

class SalesReportGenerator
  def initialize(sales_data_file, output_file = 'popular_categories_report.json')
    @sales_data_file = sales_data_file
    @output_file = output_file
    @categories_of_interest = ['سرویس خواب', 'لوازم کودک', 'تجهیزات آرایشگاهی']
  end

  def generate_report
    sales_data = load_sales_data
    categorized_sales = categorize_sales(sales_data)
    popular_categories = calculate_popularity(categorized_sales)
    save_report(popular_categories)
  rescue Errno::ENOENT => e
    puts "Error: Sales data file not found - #{e.message}"
  rescue CSV::MalformedCSVError => e
    puts "Error: Invalid CSV format - #{e.message}"
  rescue StandardError => e
    puts "Error: #{e.message}"
  end

  private

  def load_sales_data
    CSV.read(@sales_data_file, headers: true, encoding: 'UTF-8')
  end

  def categorize_sales(sales_data)
    categorized = Hash.new(0)

    sales_data.each do |row|
      category = row['category']
      next unless @categories_of_interest.include?(category)

      quantity = row['quantity'].to_i
      price = row['price'].to_f
      categorized[category] += quantity * price
    end

    categorized
  end

  def calculate_popularity(categorized_sales)
    total_sales = categorized_sales.values.sum.to_f
    categorized_sales.map do |category, sales|
      {
        category: category,
        total_sales: sales.round(2),
        percentage: ((sales / total_sales) * 100).round(2)
      }
    end.sort_by { |cat| -cat[:total_sales] }
  end

  def save_report(report_data)
    File.open(@output_file, 'w:UTF-8') do |file|
      file.write(JSON.pretty_generate(report_data))
    end
    puts "Report generated successfully: #{@output_file}"
  end
end

# Example usage:
# report_generator = SalesReportGenerator.new('sales_data.csv')
# report_generator.generate_report
```
