"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create an Elixir-based parallel load testing tool for APIs, inspired by the example provided in the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_cbf06a6fdb718afe
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule APILoadTest do
  @moduledoc """
  A parallel load testing tool for APIs.
  This module allows you to test API endpoints with concurrent requests.
  """

  require Logger

  @doc """
  Runs the load test against the specified API endpoint.

  ## Parameters
    - url: The API endpoint URL to test
    - requests: Total number of requests to make
    - concurrency: Number of concurrent requests
    - method: HTTP method (:get, :post, :put, :delete, etc.)
    - headers: List of headers (optional)
    - body: Request body (optional)
  """
  @spec run(String.t(), pos_integer(), pos_integer(), atom(), list(), any()) :: map()
  def run(url, requests, concurrency, method \\ :get, headers \\ [], body \\ nil) do
    Logger.info("Starting load test with #{requests} requests (#{concurrency} concurrent)")

    start_time = System.monotonic_time()

    results =
      requests
      |> Enum.chunk_every(concurrency)
      |> Enum.flat_map(fn chunk ->
        Task.async_stream(
          chunk,
          fn _ -> make_request(url, method, headers, body) end,
          max_concurrency: concurrency,
          timeout: 30_000
        )
        |> Enum.to_list()
      end)

    end_time = System.monotonic_time()
    duration = System.convert_time_unit(end_time - start_time, :native, :millisecond)

    {success_count, failure_count, response_times} =
      Enum.reduce(results, {0, 0, []}, fn
        {:ok, {:ok, response_time}}, {success, failure, times} ->
          {success + 1, failure, [response_time | times]}

        {:ok, {:error, _}}, {success, failure, times} ->
          {success, failure + 1, times}

        {:exit, _}, {success, failure, times} ->
          {success, failure + 1, times}
      end)

    stats = calculate_stats(response_times)

    %{
      total_requests: requests,
      success: success_count,
      failures: failure_count,
      duration_ms: duration,
      requests_per_second: requests / (duration / 1000),
      response_times: stats
    }
  end

  @doc """
  Makes an HTTP request to the specified URL and measures response time.

  ## Parameters
    - url: The API endpoint URL
    - method: HTTP method
    - headers: List of headers
    - body: Request body
  """
  @spec make_request(String.t(), atom(), list(), any()) :: {:ok, integer()} | {:error, any()}
  defp make_request(url, method, headers, body) do
    start_time = System.monotonic_time()

    case HTTPoison.request(method, url, body, headers, []) do
      {:ok, %HTTPoison.Response{status_code: status}} when status in 200..299 ->
        response_time = System.convert_time_unit(System.monotonic_time() - start_time, :native, :millisecond)
        {:ok, response_time}

      {:ok, %HTTPoison.Response{status_code: status}} ->
        Logger.warning("Request failed with status #{status}")
        {:error, status}

      {:error, reason} ->
        Logger.error("Request failed: #{inspect(reason)}")
        {:error, reason}
    end
  end

  @doc """
  Calculates statistics from response times.
  """
  @spec calculate_stats(list()) :: map()
  defp calculate_stats(response_times) do
    sorted = Enum.sort(response_times)
    count = length(sorted)

    if count > 0 do
      min = Enum.min(sorted)
      max = Enum.max(sorted)
      mean = Enum.sum(sorted) / count
      median = calculate_median(sorted)

      %{
        min: min,
        max: max,
        mean: mean,
        median: median,
        p90: percentile(sorted, 90),
        p95: percentile(sorted, 95),
        p99: percentile(sorted, 99)
      }
    else
      %{
        min: 0,
        max: 0,
        mean: 0,
        median: 0,
        p90: 0,
        p95: 0,
        p99: 0
      }
    end
  end

  defp calculate_median([]), do: 0
  defp calculate_median(list) do
    len = length(list)
    mid = div(len, 2)

    if rem(len, 2) == 0 do
      (Enum.at(list, mid - 1) + Enum.at(list, mid)) / 2
    else
      Enum.at(list, mid)
    end
  end

  defp percentile([], _), do: 0
  defp percentile(list, percent) do
    index = round(percent / 100 * (length(list) - 1))
    Enum.at(list, index)
  end
end
```
