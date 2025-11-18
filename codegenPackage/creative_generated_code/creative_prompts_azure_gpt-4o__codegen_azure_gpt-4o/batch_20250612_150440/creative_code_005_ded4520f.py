"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Suggest tools or libraries in Ruby that can be used to create QR codes for Bitcoin addresses with advanced customization features like logo embedding, as highlighted on btc-qr.to.
Generated: DETERMINISTIC_ded4520f05567c34
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# This script generates a QR code for a Bitcoin address with advanced customization 
# such as logo embedding using the 'rqrcode' and 'chunky_png' gems. Both libraries 
# need to be installed. Run `gem install rqrcode chunky_png` to install them.

require 'rqrcode'
require 'chunky_png'

# Function to generate a QR code for a Bitcoin address with customization options
# @param bitcoin_address [String] The Bitcoin address to encode in the QR code
# @param logo_path [String] Path to the logo file (PNG format) to embed in the QR code
# @param output_path [String] Path to save the output QR code with the embedded logo
# @param size [Integer] The size of the QR code (default: 300 pixels)
def generate_bitcoin_qr_with_logo(bitcoin_address, logo_path, output_path, size = 300)
  begin
    # Validate the input parameters
    raise ArgumentError, "Bitcoin address cannot be empty" if bitcoin_address.strip.empty?
    raise ArgumentError, "Logo file not found at: #{logo_path}" unless File.exist?(logo_path)

    # Create a QR code for the Bitcoin address using RQRCode
    qr_code = RQRCode::QRCode.new(bitcoin_address)

    # Render the QR code as a PNG
    qr_png = qr_code.as_png(
      bit_depth: 1,        # Black and white QR code
      border_modules: 4,   # Padding around the QR code
      color_mode: ChunkyPNG::COLOR_GRAYSCALE, # Grayscale color mode
      size: size / qr_code.module_count
    )

    # Load the logo image
    logo = ChunkyPNG::Image.from_file(logo_path)

    # Calculate the coordinates to center the logo on the QR code
    qr_width = qr_png.width
    logo_width = [logo.width, qr_width / 4].min # Scale logo to max 1/4 of QR code size
    logo_height = (logo_width * logo.height) / logo.width # Maintain aspect ratio
    scaled_logo = logo.resample_nearest_neighbor(logo_width, logo_height)

    logo_x = (qr_width - scaled_logo.width) / 2
    logo_y = (qr_width - scaled_logo.height) / 2

    # Overlay the logo onto the QR code
    qr_png.compose!(scaled_logo, logo_x, logo_y)

    # Save the customized QR code to the specified path
    qr_png.save(output_path)

    puts "QR code with embedded logo generated successfully: #{output_path}"
  rescue ArgumentError => e
    puts "Invalid argument: #{e.message}"
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

# Example usage:
# Provide the Bitcoin address, path to the logo, and output file path
bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
logo_path = "path_to_logo.png" # Replace with the actual path to your logo
output_path = "output_qr_code.png"

# Generate the QR code with the embedded logo
generate_bitcoin_qr_with_logo(bitcoin_address, logo_path, output_path)
```

**Note**: This code assumes that the `rqrcode` gem is used to create the QR code and `chunky_png` gem is used for image manipulation. Ensure the paths and dependencies are properly set up before running the script.
