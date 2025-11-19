"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: How do I handle errors and exceptions in Crystal?
Generated: DETERMINISTIC_e4f76d694444bf7b
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```crystal
# Example of error and exception handling in Crystal

# Define a custom exception
class CustomError < Exception
end

# Method that may raise different types of exceptions
def risky_operation(value : Int32)
  if value < 0
    raise ArgumentError.new("Value must be positive")
  end

  if value > 100
    raise CustomError.new("Value is too large")
  end

  value * 2
end

begin
  # Try a valid operation
  result = risky_operation(50)
  puts "Result: #{result}"

  # Try an operation that raises ArgumentError
  risky_operation(-5)
rescue ArgumentError
  puts "Caught ArgumentError: #{$!}"
rescue CustomError
  puts "Caught CustomError: #{$!}"
rescue ex : Exception
  puts "Caught unexpected exception: #{ex.message}"
ensure
  puts "This always runs, regardless of exceptions"
end

# Using try for nilable operations
value = "123a".to_i?
if value
  puts "Parsed integer: #{value}"
else
  puts "Failed to parse integer"
end

# Using try with method chaining
class User
  property name : String?

  def initialize(@name : String? = nil)
  end
end

user = User.new
name_length = user.name.try(&.size)
puts "Name length: #{name_length || "unknown"}"

# Using expect for non-nilable operations
begin
  value = "123".to_i
  puts "Parsed integer: #{value}"
rescue ex : ArgumentError
  puts "Failed to parse integer: #{ex.message}"
end

# Using raise with custom backtrace
begin
  raise Exception.new("Error with custom backtrace"), ["custom_file.cr:10"]
rescue ex
  puts "Exception: #{ex.message}"
  puts "Backtrace: #{ex.backtrace}"
end

# Using spawn with error handling
spawn do
  begin
    risky_operation(200)
  rescue ex
    puts "Error in fiber: #{ex.message}"
  end
end

Fiber.yield
```
