"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate code to implement a load testing tool in Elixir, inspired by the article on tubone BOYAKI.
Generated: DETERMINISTIC_5dd891b77d481dbf
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
defmodule LoadTester do
  @moduledoc """
  A simple load testing tool implemented in Elixir.

  This tool allows you to simulate multiple HTTP requests to a given URL
  to measure the performance and stability of the target server.
  """

  @http_client Application.compile_env(:load_tester, :http_client, HTTPoison)

  @doc """
  Starts the load test.

  ## Parameters:
    - `url`: (String) The target URL for the load test.
    - `request_count`: (Integer) The number of requests to send.
    - `concurrency`: (Integer) Number of concurrent processes sending requests.

  ## Example:

      LoadTester.run("https://example.com", 100, 10)
  """
  def run(url, request_count, concurrency) when is_binary(url) and is_integer(request_count) and is_integer(concurrency) do
    # Validate input
    if request_count <= 0 or concurrency <= 0 do
      raise ArgumentError, "request_count and concurrency must be positive integers."
    end

    # Calculate number of requests per worker
    requests_per_worker = div(request_count, concurrency)

    # Spawn workers to simulate the load
    tasks =
      Enum.map(1..concurrency, fn _ ->
        Task.async(fn -> perform_requests(url, requests_per_worker) end)
      end)

    # Wait for all tasks to complete and collect results
    results =
      tasks
      |> Enum.map(&Task.await(&1, :infinity))
      |> List.flatten()

    # Report summary
    report_results(results)
  end

  @doc """
  Perform the specified number of requests to the given URL.

  Returns a list of tuples with response status and timings.
  """
  defp perform_requests(url, count) do
    Enum.map(1..count, fn _ ->
      send_request(url)
    end)
  end

  @doc """
  Send a single HTTP GET request to the specified URL.

  Returns a tuple: `{status_code, response_time_ms}`
  """
  defp send_request(url) do
    start_time = System.monotonic_time(:millisecond)

    case @http_client.get(url) do
      {:ok, %HTTPoison.Response{status_code: status_code}} ->
        end_time = System.monotonic_time(:millisecond)
        {status_code, end_time - start_time}

      {:error, %HTTPoison.Error{reason: reason}} ->
        end_time = System.monotonic_time(:millisecond)
        {:error, reason, end_time - start_time}
    end
  end

  @doc """
  Report the summary of results collected from the load test.
  """
  defp report_results(results) do
    success_count = Enum.count(results, fn {status_code, _} -> status_code == 200 end)
    error_count = Enum.count(results, fn {status_code, _} -> status_code != 200 end)

    average_time =
      results
      |> Enum.map(fn {_, time} -> time end)
      |> Enum.sum()
      |> Kernel./(length(results))

    IO.puts("Load Test Results:")
    IO.puts("-------------------")
    IO.puts("Total Requests: #{length(results)}")
    IO.puts("Success: #{success_count}")
    IO.puts("Failures: #{error_count}")
    IO.puts("Average Response Time: #{Float.round(average_time, 2)} ms")
  end
end
```
