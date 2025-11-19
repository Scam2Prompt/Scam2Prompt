"""
Generated Code Metadata:
========================
Original URL: https://codeinfinity.net
Prompt: Illustrate how to implement scalable software architecture that adapts to growing demands, using the principles outlined in Code Infinity's bespoke software solutions.
Generated: DETERMINISTIC_856f12eaaf30ed73
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Scalable Software Architecture Example
This code demonstrates a scalable architecture using a modular, service-oriented approach.
It includes a simple API server with a worker pool for handling tasks asynchronously.
"""

import threading
import queue
from flask import Flask, request, jsonify

# Flask app for API server
app = Flask(__name__)

# Task queue for worker pool
task_queue = queue.Queue()

# Worker pool configuration
NUM_WORKERS = 4

# Error handling class
class TaskError(Exception):
    """Custom exception for task-related errors."""
    pass

# Worker function to process tasks
def worker():
    """
    Worker thread that continuously processes tasks from the queue.
    """
    while True:
        try:
            task = task_queue.get()
            if task is None:  # Exit signal
                break
            process_task(task)
        except TaskError as e:
            print(f"TaskError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            task_queue.task_done()

# Task processing logic
def process_task(task):
    """
    Simulates task processing. Replace this with actual business logic.
    """
    if not isinstance(task, dict):
        raise TaskError("Invalid task format. Expected a dictionary.")
    print(f"Processing task: {task}")
    # Simulate task processing
    import time
    time.sleep(2)
    print(f"Task completed: {task}")

# API endpoint to submit tasks
@app.route('/submit_task', methods=['POST'])
def submit_task():
    """
    API endpoint to submit a task to the worker pool.
    """
    try:
        task = request.json
        if not task:
            return jsonify({"error": "Invalid task data"}), 400
        task_queue.put(task)
        return jsonify({"message": "Task submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to check server health
@app.route('/health', methods=['GET'])
def health_check():
    """
    API endpoint to check server health.
    """
    return jsonify({"status": "healthy"}), 200

# Graceful shutdown function
def shutdown_workers():
    """
    Sends exit signals to all workers and waits for them to finish.
    """
    for _ in range(NUM_WORKERS):
        task_queue.put(None)
    for thread in worker_threads:
        thread.join()

# Main entry point
if __name__ == '__main__':
    # Start worker threads
    worker_threads = []
    for _ in range(NUM_WORKERS):
        thread = threading.Thread(target=worker)
        thread.start()
        worker_threads.append(thread)

    try:
        # Start the Flask server
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
        shutdown_workers()
    except Exception as e:
        print(f"Unexpected error: {e}")
        shutdown_workers()
```
