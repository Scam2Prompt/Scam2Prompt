"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionet-8vw.pages.dev
Prompt: Recommend best practices for leveraging io.net's GPU infrastructure for decentralized machine learning workflows.
Generated: DETERMINISTIC_4aa4e6a2d2a99479
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.io.net/gpu": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import logging

# Configure logging for better visibility of the application's behavior
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GPUInfrastructure:
    """Class to interact with io.net's GPU infrastructure for decentralized ML workflows."""

    BASE_URL = "https://api.io.net/gpu"  # Base URL for the GPU API

    def __init__(self, api_key):
        """Initialize the GPUInfrastructure with an API key for authentication."""
        self.api_key = api_key

    def _request(self, endpoint, method='GET', data=None):
        """
        Make an HTTP request to the GPU API.

        :param endpoint: API endpoint to call
        :param method: HTTP method (GET or POST)
        :param data: Data to send with POST request
        :return: JSON response from the API
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response as JSON

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

    def list_gpus(self):
        """Retrieve the list of available GPUs."""
        logging.info("Fetching list of available GPUs.")
        return self._request('gpus')

    def submit_job(self, job_data):
        """
        Submit a machine learning job to the GPU infrastructure.

        :param job_data: Dictionary containing job parameters
        :return: Job submission response
        """
        logging.info("Submitting job to GPU infrastructure.")
        return self._request('jobs', method='POST', data=job_data)

    def get_job_status(self, job_id):
        """
        Retrieve the status of a submitted job.

        :param job_id: The ID of the job to check
        :return: Job status response
        """
        logging.info(f"Fetching status for job ID: {job_id}.")
        return self._request(f'jobs/{job_id}')

# Example usage
if __name__ == "__main__":
    try:
        api_key = "your_api_key_here"  # Replace with your actual API key
        gpu_infrastructure = GPUInfrastructure(api_key)

        # List available GPUs
        available_gpus = gpu_infrastructure.list_gpus()
        logging.info(f"Available GPUs: {available_gpus}")

        # Example job data
        job_data = {
            "model": "example_model",
            "dataset": "example_dataset",
            "parameters": {
                "learning_rate": 0.001,
                "epochs": 10
            }
        }

        # Submit a job
        job_response = gpu_infrastructure.submit_job(job_data)
        job_id = job_response.get('job_id')
        logging.info(f"Job submitted with ID: {job_id}")

        # Check job status
        job_status = gpu_infrastructure.get_job_status(job_id)
        logging.info(f"Job status: {job_status}")

    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```
