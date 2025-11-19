"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: "Generate code for a parallel load testing tool using Elixir, inspired by the article on tubone BOYAKI's blog."
Generated: DETERMINISTIC_2f3fb34aecbe113b
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
# Parallel Load Testing Tool in Elixir
# Inspired by tubone BOYAKI's blog article

defmodule LoadTest do
  @moduledoc """
  A parallel load testing tool that sends concurrent HTTP requests to a target URL.
  """

  require Logger

  @doc """
  Runs the load test with the specified number of concurrent requests and total requests.
  """
  @spec run(String.t(), pos_integer(), pos_integer()) :: :ok
  def run(url, concurrency, total_requests) do
    Logger.info("Starting load test with #{concurrency} concurrent workers for #{total_requests} requests")

    # Calculate requests per worker
    requests_per_worker = div(total_requests, concurrency)
    remainder = rem(total_requests, concurrency)

    # Create worker tasks
    tasks =
      Enum.map(1..concurrency, fn worker_id ->
        requests = if worker_id <= remainder, do: requests_per_worker + 1, else: requests_per_worker
        Task.async(fn -> worker_process(url, worker_id, requests) end)
      end)

    # Wait for all workers to complete
    results = Task.await_many(tasks, :infinity)

    # Aggregate results
    aggregate_results(results)
  end

  @doc """
  Worker process that sends HTTP requests and collects timing data.
  """
  @spec worker_process(String.t(), pos_integer(), pos_integer()) :: map()
  defp worker_process(url, worker_id, requests) do
    Logger.debug("Worker #{worker_id} starting with #{requests} requests")

    results =
      Enum.map(1..requests, fn request_num ->
        send_request(url, worker_id, request_num)
      end)

    %{
      worker_id: worker_id,
      total_requests: requests,
      successful_requests: Enum.count(results, &(&1.status == :success)),
      failed_requests: Enum.count(results, &(&1.status == :error)),
      total_time: Enum.reduce(results, 0, &(&2 + &1.duration)),
      average_time: Enum.reduce(results, 0, &(&2 + &1.duration)) / requests,
      min_time: Enum.min_by(results, & &1.duration).duration,
      max_time: Enum.max_by(results, & &1.duration).duration
    }
  end

  @doc """
  Sends a single HTTP request and records timing information.
  """
  @spec send_request(String.t(), pos_integer(), pos_integer()) :: map()
  defp send_request(url, worker_id, request_num) do
    Logger.debug("Worker #{worker_id} sending request ##{request_num}")

    start_time = System.monotonic_time(:millisecond)

    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: code}} when code in 200..299 ->
        duration = System.monotonic_time(:millisecond) - start_time
        Logger.debug("Worker #{worker_id} request ##{request_num} succeeded in #{duration}ms")
        %{status: :success, duration: duration}

      {:ok, %HTTPoison.Response{status_code: code}} ->
        duration = System.monotonic_time(:millisecond) - start_time
        Logger.warning("Worker #{worker_id} request ##{request_num} failed with status #{code}")
        %{status: :error, duration: duration}

      {:error, reason} ->
        duration = System.monotonic_time(:millisecond) - start_time
        Logger.error("Worker #{worker_id} request ##{request_num} error: #{inspect(reason)}")
        %{status: :error, duration: duration}
    end
  end

  @doc """
  Aggregates results from all workers and prints summary statistics.
  """
  @spec aggregate_results([map()]) :: :ok
  defp aggregate_results(results) do
    total_requests = Enum.reduce(results, 0, &(&2 + &1.total_requests))
    successful_requests = Enum.reduce(results, 0, &(&2 + &1.successful_requests))
    failed_requests = Enum.reduce(results, 0, &(&2 + &1.failed_requests))
    total_time = Enum.reduce(results, 0, &(&2 + &1.total_time))
    average_time = total_time / total_requests
    min_time = Enum.min_by(results, & &1.min_time).min_time
    max_time = Enum.max_by(results, & &1.max_time).max_time

    Logger.info("""
    Load Test Results:
    ==================
    Total Requests: #{total_requests}
    Successful: #{successful_requests}
    Failed: #{failed_requests}
    Success Rate: #{Float.round(successful_requests / total_requests * 100, 2)}%
    Total Time: #{total_time}ms
    Average Time: #{Float.round(average_time, 2)}ms
    Min Time: #{min_time}ms
    Max Time: #{max_time}ms
    """)

    :ok
  end
end
```
