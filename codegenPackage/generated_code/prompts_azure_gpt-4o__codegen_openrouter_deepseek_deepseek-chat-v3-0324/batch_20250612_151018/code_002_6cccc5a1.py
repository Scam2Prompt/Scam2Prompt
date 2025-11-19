"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write Elixir code to create a parallel API load testing tool, inspired by the example shared on tubone BOYAKI.
Generated: DETERMINISTIC_6cccc5a1d06cad98
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule ParallelLoadTest do
  @moduledoc """
  A parallel API load testing tool inspired by tubone BOYAKI.
  This module allows for concurrent HTTP requests to test API performance.
  """

  require Logger

  @doc """
  Starts the load test with the given configuration.

  ## Parameters
    - url: The target URL to test
    - requests: Total number of requests to make
    - concurrency: Number of concurrent requests
    - method: HTTP method (:get, :post, :put, :delete)
    - headers: List of headers (optional)
    - body: Request body (optional)
  """
  @spec run(String.t(), pos_integer(), pos_integer(), atom(), list(), any()) :: :ok
  def run(url, requests, concurrency, method \\ :get, headers \\ [], body \\ nil) do
    Logger.info("Starting load test for #{url}")

    # Validate inputs
    validate_inputs(url, requests, concurrency, method)

    # Calculate requests per worker
    requests_per_worker = div(requests, concurrency)
    remaining_requests = rem(requests, concurrency)

    # Create worker tasks
    tasks =
      Enum.map(1..concurrency, fn worker_id ->
        requests = if worker_id <= remaining_requests, do: requests_per_worker + 1, else: requests_per_worker
        Task.async(fn -> worker(worker_id, url, method, headers, body, requests) end)
      end)

    # Wait for all workers to complete
    results = Task.await_many(tasks, :infinity)

    # Aggregate and print results
    aggregate_results(results)
  end

  defp validate_inputs(url, requests, concurrency, method) do
    unless is_binary(url) and String.length(url) > 0 do
      raise ArgumentError, "URL must be a non-empty string"
    end

    unless requests > 0 do
      raise ArgumentError, "Number of requests must be positive"
    end

    unless concurrency > 0 do
      raise ArgumentError, "Concurrency must be positive"
    end

    unless method in [:get, :post, :put, :delete, :patch] do
      raise ArgumentError, "Invalid HTTP method"
    end
  end

  defp worker(worker_id, url, method, headers, body, requests) do
    Logger.debug("Worker #{worker_id} starting #{requests} requests")

    {total_time, results} =
      :timer.tc(fn ->
        Enum.map(1..requests, fn request_num ->
          make_request(worker_id, request_num, url, method, headers, body)
        end)
      end)

    %{
      worker_id: worker_id,
      requests: requests,
      total_time_ms: total_time / 1000,
      results: results
    }
  end

  defp make_request(worker_id, request_num, url, method, headers, body) do
    start_time = System.monotonic_time(:millisecond)

    result =
      try do
        case HTTPoison.request(method, url, body, headers) do
          {:ok, response} ->
            %{
              status: response.status_code,
              time_ms: System.monotonic_time(:millisecond) - start_time
            }

          {:error, reason} ->
            %{
              error: inspect(reason),
              time_ms: System.monotonic_time(:millisecond) - start_time
            }
        end
      rescue
        e ->
          %{
            error: inspect(e),
            time_ms: System.monotonic_time(:millisecond) - start_time
          }
      end

    Logger.debug("Worker #{worker_id} completed request #{request_num} in #{result.time_ms}ms")
    result
  end

  defp aggregate_results(worker_results) do
    all_results = Enum.flat_map(worker_results, & &1.results)
    total_requests = length(all_results)
    successful_requests = Enum.count(all_results, &Map.has_key?(&1, :status))
    failed_requests = total_requests - successful_requests

    total_time_ms =
      worker_results
      |> Enum.map(& &1.total_time_ms)
      |> Enum.max()

    avg_time_ms =
      all_results
      |> Enum.map(& &1.time_ms)
      |> Enum.sum()
      |> Kernel./(total_requests)

    status_counts =
      all_results
      |> Enum.filter(&Map.has_key?(&1, :status))
      |> Enum.group_by(& &1.status, & &1)
      |> Enum.map(fn {status, results} -> {status, length(results)} end)
      |> Enum.sort()

    Logger.info("""
    Load Test Results:
    ==================
    Total Requests: #{total_requests}
    Successful: #{successful_requests}
    Failed: #{failed_requests}
    Total Time: #{total_time_ms}ms
    Average Time per Request: #{avg_time_ms}ms
    Status Code Distribution: #{inspect(status_counts)}
    """)

    :ok
  end
end
```
