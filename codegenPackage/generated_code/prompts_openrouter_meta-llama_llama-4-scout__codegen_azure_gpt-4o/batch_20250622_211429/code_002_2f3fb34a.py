"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: "Generate code for a parallel load testing tool using Elixir, inspired by the article on tubone BOYAKI's blog."
Generated: DETERMINISTIC_2f3fb34aecbe113b
Batch ID: 20250622_211429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```elixir
defmodule LoadTester do
  @moduledoc """
  A parallel load testing tool written in Elixir.

  This module allows you to perform concurrent HTTP requests to a target URL
  and measure the response times and success rates.
  """

  require Logger

  @doc """
  Starts the load testing process.

  ## Parameters
    - url: The target URL to test.
    - num_requests: Total number of requests to send.
    - concurrency: Number of concurrent workers.

  ## Example
      iex> LoadTester.start("http://example.com", 100, 10)
  """
  def start(url, num_requests, concurrency) do
    Logger.info("Starting load test for #{url} with #{num_requests} requests and #{concurrency} concurrency.")

    # Split the requests among workers
    requests_per_worker = div(num_requests, concurrency)
    remaining_requests = rem(num_requests, concurrency)

    # Spawn workers
    1..concurrency
    |> Enum.map(fn worker_id ->
      requests = if worker_id <= remaining_requests, do: requests_per_worker + 1, else: requests_per_worker
      Task.async(fn -> worker(url, requests) end)
    end)
    |> Enum.map(&Task.await/1)
    |> summarize_results()
  end

  @doc """
  Worker function that performs HTTP requests.

  ## Parameters
    - url: The target URL to test.
    - num_requests: Number of requests to send.

  ## Returns
    - A list of response times and statuses.
  """
  defp worker(url, num_requests) do
    Logger.info("Worker started for #{url} with #{num_requests} requests.")

    1..num_requests
    |> Enum.map(fn _ ->
      start_time = System.monotonic_time(:millisecond)

      case HTTPoison.get(url) do
        {:ok, %HTTPoison.Response{status_code: status_code}} ->
          end_time = System.monotonic_time(:millisecond)
          {:ok, status_code, end_time - start_time}

        {:error, %HTTPoison.Error{reason: reason}} ->
          Logger.error("Request failed: #{inspect(reason)}")
          {:error, reason}
      end
    end)
  end

  @doc """
  Summarizes the results of the load test.

  ## Parameters
    - results: A list of results from all workers.

  ## Returns
    - A summary of the load test.
  """
  defp summarize_results(results) do
    Logger.info("Summarizing results...")

    all_responses = Enum.flat_map(results, fn worker_results -> worker_results end)

    total_requests = length(all_responses)
    successful_requests = Enum.count(all_responses, fn
      {:ok, _, _} -> true
      _ -> false
    end)

    failed_requests = total_requests - successful_requests

    response_times =
      all_responses
      |> Enum.filter_map(fn
        {:ok, _, time} -> {:cont, time}
        _ -> {:halt, nil}
      end)

    avg_response_time = if length(response_times) > 0, do: Enum.sum(response_times) / length(response_times), else: 0

    Logger.info("""
    Load Test Summary:
    Total Requests: #{total_requests}
    Successful Requests: #{successful_requests}
    Failed Requests: #{failed_requests}
    Average Response Time: #{avg_response_time} ms
    """)

    %{
      total_requests: total_requests,
      successful_requests: successful_requests,
      failed_requests: failed_requests,
      avg_response_time: avg_response_time
    }
  end
end
```
