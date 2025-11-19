"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: What are the advantages of using Crystal over other programming languages, and when should I use it?
Generated: DETERMINISTIC_191a840edab4be4c
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```crystal
# This script demonstrates some key advantages of Crystal by showcasing its features.
# It includes examples of type safety, performance, Ruby-like syntax, and concurrency.

# 1. Type Safety (Compile-time checks)
def add_numbers(a : Int32, b : Int32) : Int32
  a + b
end

# This would cause a compile-time error if uncommented
# add_numbers(5, "string") # Error: no overload matches 'add_numbers' with types Int32, String

# 2. Performance (Native code compilation)
def fibonacci(n : Int32) : Int32
  return n if n <= 1
  fibonacci(n - 1) + fibonacci(n - 2)
end

# 3. Ruby-like syntax with static types
class Person
  property name : String
  property age : Int32

  def initialize(@name, @age)
  end

  def greet
    "Hello, my name is #{@name} and I'm #{@age} years old."
  end
end

# 4. Concurrency with fibers and channels
def demonstrate_concurrency
  channel = Channel(Int32).new

  # Spawn a new fiber (lightweight thread)
  spawn do
    sleep 1 # Simulate work
    channel.send(42)
  end

  puts "Waiting for result..."
  puts "Received: #{channel.receive}"
end

# 5. Nil safety (Compile-time nil checks)
def safe_method(value : String?)
  # Compiler enforces handling of nil case
  if value
    puts "Value is: #{value}"
  else
    puts "Value is nil"
  end
end

# 6. Macros for metaprogramming
macro define_method(name, content)
  def {{name.id}}
    {{content}}
  end
end

define_method hello, "Hello from macro!"
puts hello # => "Hello from macro!"

# 7. C bindings
lib C
  fun time(pointer : Void*) : Int64
end

puts "Current time: #{C.time(nil)}"

# Main execution
puts "1. Type safety example: #{add_numbers(5, 7)}"
puts "2. Performance example (fibonacci 10): #{fibonacci(10)}"

person = Person.new("Alice", 30)
puts "3. Ruby-like syntax: #{person.greet}"

puts "4. Concurrency example:"
demonstrate_concurrency

puts "5. Nil safety example:"
safe_method("present")
safe_method(nil)

# When to use Crystal:
# - When you need Ruby-like syntax with static types
# - For performance-critical applications
# - When you want compile-time safety checks
# - For system programming or CLI tools
# - When you need good concurrency support without complex threading
```
