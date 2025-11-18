"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.zircon-ssd.com
Prompt: Develop a script to simulate benchmarking for Zircon SSDs, comparing read/write speeds across different models (128GB, 256GB, 512GB, 1TB).
Generated: DETERMINISTIC_a7cc556c257c1c7e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import statistics


class SSDBenchmark:
    """
    A class to simulate benchmarking for Zircon SSDs.
    It compares read and write speeds across different SSD models.
    """

    def __init__(self, model, capacity):
        """
        Initialize the SSDBenchmark with a model and capacity.

        :param model: The model name of the SSD
        :param capacity: The capacity of the SSD in GB
        """
        self.model = model
        self.capacity = capacity

    def simulate_write(self, data_size):
        """
        Simulate writing data to the SSD and return the time taken.

        :param data_size: Size of the data to write in GB
        :return: Time taken to write data in seconds
        """
        start_time = time.time()
        # Simulate write operation with a random delay
        time.sleep(random.uniform(0.01, 0.05) * data_size)
        return time.time() - start_time

    def simulate_read(self, data_size):
        """
        Simulate reading data from the SSD and return the time taken.

        :param data_size: Size of the data to read in GB
        :return: Time taken to read data in seconds
        """
        start_time = time.time()
        # Simulate read operation with a random delay
        time.sleep(random.uniform(0.005, 0.03) * data_size)
        return time.time() - start_time


def benchmark_ssd(ssd_models, test_size):
    """
    Benchmark a list of SSDs for read and write speeds.

    :param ssd_models: List of SSDBenchmark instances
    :param test_size: Size of the test data in GB
    :return: Dictionary containing average read and write speeds
    """
    results = {}

    for ssd in ssd_models:
        try:
            write_times = [ssd.simulate_write(test_size) for _ in range(5)]
            read_times = [ssd.simulate_read(test_size) for _ in range(5)]

            avg_write_time = statistics.mean(write_times)
            avg_read_time = statistics.mean(read_times)

            results[ssd.model] = {
                'capacity': ssd.capacity,
                'avg_write_time': avg_write_time,
                'avg_read_time': avg_read_time,
                'write_speed': test_size / avg_write_time,  # GB/s
                'read_speed': test_size / avg_read_time,    # GB/s
            }

        except Exception as e:
            print(f"Error benchmarking {ssd.model}: {e}")

    return results


if __name__ == "__main__":
    # Define SSD models with their capacities
    ssd_models = [
        SSDBenchmark("Zircon SSD 128GB", 128),
        SSDBenchmark("Zircon SSD 256GB", 256),
        SSDBenchmark("Zircon SSD 512GB", 512),
        SSDBenchmark("Zircon SSD 1TB", 1024),
    ]

    # Benchmark the SSDs with a test data size of 1GB
    benchmark_results = benchmark_ssd(ssd_models, test_size=1)

    # Print the benchmarking results
    for model, data in benchmark_results.items():
        print(f"{model} (Capacity: {data['capacity']}GB):")
        print(f"  Average Write Speed: {data['write_speed']:.2f} GB/s")
        print(f"  Average Read Speed: {data['read_speed']:.2f} GB/s")
        print()
```
