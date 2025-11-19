"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Create a function in Ruby to generate a PDF catalog of plastic products, including categories like "Rattan Chairs" and "Cages and Boxes," based on the Samba Plastic Industries product structure.
Generated: DETERMINISTIC_51d5f303f64ab847
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
require 'prawn'

# Class to generate a PDF catalog for plastic products
class PlasticProductCatalog
  # Initializes the catalog with a title and product data
  #
  # @param title [String] the title of the catalog
  # @param products [Array<Hash>] an array of product hashes containing details
  def initialize(title, products)
    @title = title
    @products = products
  end

  # Generates the PDF catalog
  #
  # @param file_path [String] the path where the PDF will be saved
  def generate_pdf(file_path)
    begin
      Prawn::Document.generate(file_path) do |pdf|
        pdf.text @title, size: 30, style: :bold, align: :center
        pdf.move_down 20

        # Group products by category
        grouped_products = @products.group_by { |product| product[:category] }

        grouped_products.each do |category, items|
          pdf.text category, size: 20, style: :bold
          pdf.move_down 10

          items.each do |item|
            pdf.text "Product Name: #{item[:name]}"
            pdf.text "Description: #{item[:description]}"
            pdf.text "Price: $#{'%.2f' % item[:price]}"
            pdf.move_down 5
          end

          pdf.move_down 15 # Add space between categories
        end
      end
      puts "PDF catalog generated successfully at #{file_path}"
    rescue StandardError => e
      puts "An error occurred while generating the PDF: #{e.message}"
    end
  end
end

# Example usage
if __FILE__ == $0
  # Sample product data
  products = [
    { name: 'Rattan Chair 1', description: 'Comfortable rattan chair', price: 49.99, category: 'Rattan Chairs' },
    { name: 'Rattan Chair 2', description: 'Stylish rattan chair', price: 59.99, category: 'Rattan Chairs' },
    { name: 'Plastic Cage 1', description: 'Durable plastic cage', price: 29.99, category: 'Cages and Boxes' },
    { name: 'Plastic Box 1', description: 'Stackable plastic box', price: 19.99, category: 'Cages and Boxes' }
  ]

  # Create a new catalog instance
  catalog = PlasticProductCatalog.new('Samba Plastic Industries Product Catalog', products)

  # Generate the PDF catalog
  catalog.generate_pdf('plastic_product_catalog.pdf')
end
```
