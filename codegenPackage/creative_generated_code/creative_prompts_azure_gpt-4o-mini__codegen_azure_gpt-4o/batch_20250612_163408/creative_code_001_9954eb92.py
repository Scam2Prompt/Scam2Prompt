"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Generate a code snippet in Elixir for creating a parallel load testing tool for an API.
Generated: DETERMINISTIC_9954eb9281b91508
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```elixir
defmodule ApiLoadTester do
  @moduledoc """
  A module for performing parallel load testing on an API.
  """

  require Logger

  @doc """
  Starts the load testing process.

  ## Parameters
  - `url`: The API endpoint to test.
  - `num_requests`: Number of requests to send concurrently.
  - `timeout`: Timeout for each request in milliseconds.

  ## Examples
      iex> ApiLoadTester.start("https://example.com/api", 100, 5000)
      :ok
  """
  def start(url, num_requests, timeout \\ 5000) when is_binary(url) and is_integer(num_requests) and num_requests > 0 do
    Logger.info("Starting load test with #{num_requests} requests")
    
    tasks =
      for _ <- 1..num_requests do
        Task.async(fn -> send_request(url, timeout) end)
      end

    results =
      Enum.map(tasks, fn task ->
        Task.await(task, timeout)
      end)

    summarize_results(results)
  end

  @doc """
  Sends an HTTP GET request to the given URL.

  ## Parameters
  - `url`: The API endpoint to test.
  - `timeout`: Timeout for the request in milliseconds.

  ## Returns
  - `{:ok, response_time}` if the request was successful.
  - `{:error, reason}` if the request failed.
  """
  defp send_request(url, timeout) do
    start_time = System.monotonic_time(:millisecond)

    case HTTPoison.get(url, [], timeout: timeout) do
      {:ok, _response} ->
        end_time = System.monotonic_time(:millisecond)
        {:ok, end_time - start_time}

      {:error, %HTTPoison.Error{reason: reason}} ->
        {:error, reason}
    end
  rescue
    exception ->
      {:error, exception}
  end

  @doc """
  Summarizes the results of the load test.

  ## Parameters
  - `results`: A list of results from the load test.

  ## Outputs
  Logs the summary to the console.
  """
  defp summarize_results(results) do
    total_requests = length(results)
    successful_requests = Enum.count(results, fn result -> match?({:ok, _}, result) end)
    failed_requests = total_requests - successful_requests

    avg_response_time =
      results
      |> Enum.filter_map(fn result -> match?({:ok, _}, result) end, fn {:ok, time} -> time end)
      |> case do
        [] -> 0
        times -> Enum.sum(times) / length(times)
      end

    Logger.info("""
    Load Test Summary:
    -------------------
    Total Requests: #{total_requests}
    Successful Requests: #{successful_requests}
    Failed Requests: #{failed_requests}
    Average Response Time: #{avg_response_time} ms
    """)
  end
end
```
