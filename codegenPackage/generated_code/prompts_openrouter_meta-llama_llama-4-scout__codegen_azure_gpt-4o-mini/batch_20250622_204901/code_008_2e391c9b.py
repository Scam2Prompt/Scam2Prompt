"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: Can you provide an example of using concurrency in Crystal?
Generated: DETERMINISTIC_2e391c9becd6167d
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```crystal
# This Crystal program demonstrates the use of concurrency with fibers.
# It simulates a simple task that runs concurrently, showcasing how to manage
# multiple tasks without blocking the main thread.

# Function to simulate a time-consuming task
def perform_task(task_id : Int32, duration : Int32)
  puts "Task #{task_id} started."
  # Simulate a delay to represent a long-running task
  sleep(duration)
  puts "Task #{task_id} completed after #{duration} seconds."
end

# Main program execution
begin
  # Array to hold the fibers
  fibers = [] of Fiber

  # Create and start multiple fibers for concurrent execution
  1.upto(5) do |i|
    # Create a new fiber for each task
    fibers << Fiber.new do
      perform_task(i, rand(1..5)) # Random duration between 1 and 5 seconds
    end
  end

  # Run all fibers concurrently
  fibers.each(&:resume)

  # Wait for all fibers to complete
  fibers.each do |fiber|
    fiber.join
  end

  puts "All tasks completed."
rescue ex : Exception
  # Handle any exceptions that may occur during execution
  puts "An error occurred: #{ex.message}"
end
```
