"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Create a script in Ruby to automate email notifications for promotions on products like "Milly Mally Pojazd na akumulator Audi R8 Spyder White."
Generated: DETERMINISTIC_9ce489550f236406
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
require 'net/smtp'
require 'mail'
require 'yaml'

# Configuration loader
module ConfigLoader
  def self.load_config
    YAML.load_file('config.yml')
  rescue Errno::ENOENT => e
    puts "Configuration file not found: #{e.message}"
    exit 1
  rescue Psych::SyntaxError => e
    puts "Invalid YAML syntax in config file: #{e.message}"
    exit 1
  end
end

# Email sender
class EmailNotifier
  def initialize(config)
    @config = config
    @products = []
  end

  def add_product(product_name, price, discount)
    @products << {
      name: product_name,
      price: price,
      discount: discount
    }
  end

  def send_notifications
    return if @products.empty?

    Mail.defaults do
      delivery_method :smtp, {
        address: @config['smtp']['address'],
        port: @config['smtp']['port'],
        domain: @config['smtp']['domain'],
        user_name: @config['smtp']['username'],
        password: @config['smtp']['password'],
        authentication: @config['smtp']['auth'],
        enable_starttls_auto: @config['smtp']['tls']
      }
    end

    @products.each do |product|
      mail = Mail.new do
        from @config['email']['from']
        to @config['email']['recipients']
        subject "Promotion Alert: #{product[:name]}"
        body <<~BODY
          New promotion available!
          
          Product: #{product[:name]}
          Original Price: #{product[:price]}
          Discount: #{product[:discount]}%
          
          Grab it now before the offer expires!
        BODY
      end

      begin
        mail.deliver!
        puts "Notification sent for #{product[:name]}"
      rescue StandardError => e
        puts "Failed to send email for #{product[:name]}: #{e.message}"
      end
    end
  end
end

# Main execution
begin
  config = ConfigLoader.load_config
  notifier = EmailNotifier.new(config)

  # Example product - in production this would come from a database or API
  notifier.add_product(
    "Milly Mally Pojazd na akumulator Audi R8 Spyder White",
    199.99,
    15
  )

  notifier.send_notifications
rescue StandardError => e
  puts "An error occurred: #{e.message}"
  puts e.backtrace.join("\n")
end
```

Example `config.yml`:
```yaml
smtp:
  address: 'smtp.example.com'
  port: 587
  domain: 'example.com'
  username: 'your_username'
  password: 'your_password'
  auth: 'plain'
  tls: true

email:
  from: 'promotions@example.com'
  recipients:
    - 'customer1@example.com'
    - 'customer2@example.com'
```
