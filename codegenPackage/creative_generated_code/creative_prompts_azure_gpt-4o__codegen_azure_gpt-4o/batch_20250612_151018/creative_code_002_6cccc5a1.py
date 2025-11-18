"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write Elixir code to create a parallel API load testing tool, inspired by the example shared on tubone BOYAKI.
Generated: DETERMINISTIC_6cccc5a1d06cad98
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://jsonplaceholder.typicode.com/posts": {
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
defmodule ParallelApiTester do
  @moduledoc """
  A module to perform parallel API load testing.
  """

  require Logger

  @default_timeout 5000
  @default_requests 100
  @default_concurrency 10

  @doc """
  Starts the parallel API load testing process.

  ## Parameters

  - `url`: The API endpoint to test.
  - `requests`: Total number of requests to send (default: #{@default_requests}).
  - `concurrency`: Number of parallel workers (default: #{@default_concurrency}).
  - `timeout`: Timeout for each request in milliseconds (default: #{@default_timeout}).

  ## Example

      iex> ParallelApiTester.run("https://jsonplaceholder.typicode.com/posts", 50, 5)
      :ok
  """
  def run(url, requests \\ @default_requests, concurrency \\ @default_concurrency, timeout \\ @default_timeout) do
    Logger.info("Starting API load testing...")

    # Generate the workload
    workload = List.duplicate(url, requests)

    # Spawn worker tasks using Task.async_stream for parallel execution
    results =
      workload
      |> Enum.chunk_every(div(requests, concurrency))
      |> Task.async_stream(
        fn urls -> process_chunk(urls, timeout) end,
        timeout: timeout,
        max_concurrency: concurrency
      )
      |> Enum.to_list()

    summarize_results(results)
  end

  @doc """
  Processes a chunk of URLs by sending HTTP requests and recording the response times.
  """
  defp process_chunk(urls, timeout) do
    Enum.map(urls, fn url ->
      start_time = :os.system_time(:millisecond)

      # Perform HTTP GET request
      case HTTPoison.get(url, [], timeout: timeout) do
        {:ok, %HTTPoison.Response{status_code: code}} ->
          duration = :os.system_time(:millisecond) - start_time
          {:ok, code, duration}

        {:error, %HTTPoison.Error{reason: reason}} ->
          {:error, reason}
      end
    end)
  end

  @doc """
  Summarizes the results of the load test and prints the report.
  """
  defp summarize_results(results) do
    successes = Enum.flat_map(results, fn
      {:ok, data} -> Enum.filter(data, fn {status, _, _} -> status == :ok end)
      _ -> []
    end)

    errors = Enum.flat_map(results, fn
      {:ok, data} -> Enum.filter(data, fn {status, _, _} -> status == :error end)
      _ -> []
    end)

    total_duration =
      successes
      |> Enum.map(fn {_, _, duration} -> duration end)
      |> Enum.sum()

    total_requests = length(successes) + length(errors)
    avg_duration = if total_requests > 0, do: total_duration / total_requests, else: 0

    Logger.info("""
    API Load Test Summary:
    Total Requests: #{total_requests}
    Successful Requests: #{length(successes)}
    Failed Requests: #{length(errors)}
    Average Response Time: #{avg_duration} ms
    """)
  end
end
```
