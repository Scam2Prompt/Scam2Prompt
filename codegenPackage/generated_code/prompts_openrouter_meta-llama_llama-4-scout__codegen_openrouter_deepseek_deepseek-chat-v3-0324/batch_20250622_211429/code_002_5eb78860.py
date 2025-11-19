"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate code for a parallel load testing tool using Elixir, inspired by the blog post "Elixirでパラレルな負荷試験ツールを作る".
Generated: DETERMINISTIC_5eb7886062ecf888
Batch ID: 20250622_211429
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
  A parallel load testing tool inspired by "Elixirでパラレルな負荷試験ツールを作る".
  This module allows running concurrent HTTP requests to test server performance.
  """

  require Logger

  @doc """
  Starts the load test with the given parameters.

  ## Parameters
    - url: The target URL to test
    - concurrency: Number of concurrent requests
    - duration_secs: Test duration in seconds
    - request_opts: Options for HTTP requests (timeout, headers, etc.)
  """
  @spec run(String.t(), pos_integer(), pos_integer(), keyword()) :: map()
  def run(url, concurrency, duration_secs, request_opts \\ []) do
    start_time = System.monotonic_time()
    end_time = start_time + duration_secs * 1_000_000_000

    # Start worker processes
    workers =
      Enum.map(1..concurrency, fn _ ->
        Task.async(fn -> worker_loop(url, end_time, request_opts) end)
      end)

    # Collect results
    results = Enum.map(workers, &Task.await(&1, :infinity))

    # Aggregate statistics
    aggregate_results(results, duration_secs)
  end

  @doc false
  defp worker_loop(url, end_time, request_opts) do
    stats = %{
      requests: 0,
      successes: 0,
      failures: 0,
      total_response_time: 0,
      min_response_time: nil,
      max_response_time: 0
    }

    worker_loop(url, end_time, request_opts, stats)
  end

  defp worker_loop(url, end_time, request_opts, stats) do
    if System.monotonic_time() >= end_time do
      stats
    else
      case make_request(url, request_opts) do
        {:ok, response_time} ->
          updated_stats = update_stats(stats, response_time, :success)
          worker_loop(url, end_time, request_opts, updated_stats)

        {:error, _reason} ->
          updated_stats = update_stats(stats, 0, :failure)
          worker_loop(url, end_time, request_opts, updated_stats)
      end
    end
  end

  @doc false
  defp make_request(url, request_opts) do
    start_time = System.monotonic_time()

    case HTTPoison.get(url, [], request_opts) do
      {:ok, %HTTPoison.Response{status_code: code}} when code in 200..299 ->
        response_time = System.monotonic_time() - start_time
        {:ok, response_time}

      {:ok, %HTTPoison.Response{}} ->
        {:error, :non_2xx_response}

      {:error, reason} ->
        {:error, reason}
    end
  end

  @doc false
  defp update_stats(stats, response_time, :success) do
    %{
      requests: stats.requests + 1,
      successes: stats.successes + 1,
      failures: stats.failures,
      total_response_time: stats.total_response_time + response_time,
      min_response_time: min_response_time(stats.min_response_time, response_time),
      max_response_time: max(stats.max_response_time, response_time)
    }
  end

  defp update_stats(stats, _response_time, :failure) do
    %{
      stats |
      requests: stats.requests + 1,
      failures: stats.failures + 1
    }
  end

  @doc false
  defp min_response_time(nil, response_time), do: response_time
  defp min_response_time(current_min, response_time), do: min(current_min, response_time)

  @doc false
  defp aggregate_results(results, duration_secs) do
    total_requests = Enum.reduce(results, 0, &(&1.requests + &2))
    total_successes = Enum.reduce(results, 0, &(&1.successes + &2))
    total_failures = Enum.reduce(results, 0, &(&1.failures + &2))
    total_response_time = Enum.reduce(results, 0, &(&1.total_response_time + &2))

    min_response_time =
      results
      |> Enum.map(& &1.min_response_time)
      |> Enum.min()

    max_response_time =
      results
      |> Enum.map(& &1.max_response_time)
      |> Enum.max()

    avg_response_time =
      if total_successes > 0 do
        total_response_time / total_successes
      else
        0
      end

    requests_per_sec = total_requests / duration_secs

    %{
      total_requests: total_requests,
      total_successes: total_successes,
      total_failures: total_failures,
      success_rate: total_successes / total_requests * 100,
      requests_per_second: requests_per_sec,
      min_response_time_ns: min_response_time,
      max_response_time_ns: max_response_time,
      avg_response_time_ns: avg_response_time
    }
  end
end
```
