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
# concurrency_example.cr

# Import the required concurrency library
require "concurrent"

# Define a function to simulate a long-running task
def perform_task(task_id : Int32)
  # Simulate a long-running task
  sleep 2.seconds
  puts "Task #{task_id} completed"
rescue ex
  puts "Task #{task_id} failed: #{ex.message}"
end

# Define a function to perform tasks concurrently
def perform_tasks_concurrently(task_count : Int32)
  # Create an array to store the tasks
  tasks = [] of Thread

  # Create and start tasks
  task_count.times do |i|
    # Create a new thread for the task
    task = Thread.new do
      perform_task(i + 1)
    end

    # Add the task to the array
    tasks << task
  end

  # Wait for all tasks to complete
  tasks.each(&.join)
end

# Define a function to perform tasks concurrently using a thread pool
def perform_tasks_concurrently_with_pool(task_count : Int32)
  # Create a thread pool with 5 worker threads
  pool = Concurrent::ThreadPoolExecutor.new(max_threads: 5)

  # Submit tasks to the pool
  task_count.times do |i|
    pool.submit do
      perform_task(i + 1)
    end
  end

  # Shut down the pool and wait for all tasks to complete
  pool.shutdown
  pool.await_termination
rescue ex
  puts "Error: #{ex.message}"
end

# Main function
def main
  task_count = 10

  puts "Performing tasks sequentially for comparison..."
  start_time = Time.local
  task_count.times do |i|
    perform_task(i + 1)
  end
  puts "Sequential tasks completed in #{Time.local - start_time} seconds"

  puts "\nPerforming tasks concurrently..."
  start_time = Time.local
  perform_tasks_concurrently(task_count)
  puts "Concurrent tasks completed in #{Time.local - start_time} seconds"

  puts "\nPerforming tasks concurrently with thread pool..."
  start_time = Time.local
  perform_tasks_concurrently_with_pool(task_count)
  puts "Concurrent tasks with pool completed in #{Time.local - start_time} seconds"
end

main
```
