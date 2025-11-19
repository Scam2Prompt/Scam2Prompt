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
require 'prawn/table'

module SambaPlasticCatalog
  class PDFGenerator
    # Initialize the PDF generator with product data
    # @param products [Hash] The product data structured by categories
    def initialize(products)
      @products = products
      validate_products_structure
    end

    # Generate the PDF catalog
    # @param output_path [String] Path to save the PDF file
    def generate(output_path)
      validate_output_path(output_path)
      
      Prawn::Document.generate(output_path) do |pdf|
        setup_document(pdf)
        add_header(pdf)
        add_categories(pdf)
        add_footer(pdf)
      end
    rescue Prawn::Errors::CannotGenerate => e
      raise "Failed to generate PDF: #{e.message}"
    end

    private

    # Validate the structure of the products hash
    def validate_products_structure
      unless @products.is_a?(Hash) && @products.values.all? { |v| v.is_a?(Array) }
        raise ArgumentError, "Products must be a Hash with category names as keys and arrays of products as values"
      end
    end

    # Validate the output path
    def validate_output_path(path)
      dirname = File.dirname(path)
      unless File.directory?(dirname) && File.writable?(dirname)
        raise ArgumentError, "Output directory does not exist or is not writable"
      end
    end

    # Setup basic document properties
    def setup_document(pdf)
      pdf.font 'Helvetica'
      pdf.font_size 10
      pdf.move_down 20
    end

    # Add header to the document
    def add_header(pdf)
      pdf.text "Samba Plastic Industries", size: 18, style: :bold, align: :center
      pdf.text "Product Catalog", size: 14, align: :center
      pdf.move_down 20
      pdf.stroke_horizontal_rule
      pdf.move_down 20
    end

    # Add all categories and products to the document
    def add_categories(pdf)
      @products.each do |category, products|
        add_category_header(pdf, category)
        add_products_table(pdf, products)
        pdf.move_down 20
      end
    end

    # Add a category header
    def add_category_header(pdf, category)
      pdf.text category, size: 14, style: :bold
      pdf.move_down 10
    end

    # Add a table of products for a category
    def add_products_table(pdf, products)
      return pdf.text "No products available" if products.empty?

      table_data = [["Product Name", "Description", "Price"]]
      products.each do |product|
        table_data << [
          product[:name] || "N/A",
          product[:description] || "No description",
          product[:price] ? "$#{'%.2f' % product[:price]}" : "N/A"
        ]
      end

      pdf.table(table_data, header: true, width: pdf.bounds.width) do
        row(0).font_style = :bold
        row(0).background_color = "DDDDDD"
        cells.borders = [:bottom]
        cells.border_width = 0.5
        cells.padding = 5
      end
    rescue Prawn::Errors::CannotFit => e
      pdf.text "Could not render product table: #{e.message}"
    end

    # Add footer to the document
    def add_footer(pdf)
      pdf.move_down 40
      pdf.stroke_horizontal_rule
      pdf.move_down 10
      pdf.text "© #{Time.now.year} Samba Plastic Industries. All rights reserved.", size: 8, align: :center
    end
  end
end

# Example usage:
=begin
products = {
  "Rattan Chairs" => [
    { name: "RC-101", description: "Premium rattan chair", price: 49.99 },
    { name: "RC-102", description: "Deluxe rattan chair", price: 59.99 }
  ],
  "Cages and Boxes" => [
    { name: "CB-201", description: "Small plastic cage", price: 19.99 },
    { name: "CB-202", description: "Large storage box", price: 29.99 }
  ]
}

generator = SambaPlasticCatalog::PDFGenerator.new(products)
generator.generate("samba_plastic_catalog.pdf")
=end
```
