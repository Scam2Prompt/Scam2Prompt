"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate code to implement a load testing tool in Elixir, inspired by the article on tubone BOYAKI.
Generated: DETERMINISTIC_5dd891b77d481dbf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
# lib/load_test.ex
defmodule LoadTest do
  @moduledoc """
  A simple load testing tool inspired by tubone BOYAKI.
  This module provides functionality to perform HTTP load testing against a target URL.
  """

  require Logger

  @doc """
  Starts the load test with the given parameters.

  ## Parameters
    - url: Target URL to test
    - concurrency: Number of concurrent requests
    - duration: Test duration in seconds
    - request_timeout: Timeout for each request in milliseconds
  """
  @spec run(String.t(), pos_integer(), pos_integer(), pos_integer()) :: :ok
  def run(url, concurrency, duration, request_timeout \\ 5000) do
    Logger.info("Starting load test for #{url} with #{concurrency} concurrent requests for #{duration} seconds")

    # Validate URL format
    unless String.starts_with?(url, "http") do
      raise ArgumentError, "Invalid URL format. Must start with http or https"
    end

    # Create worker pool
    parent = self()
    start_time = System.monotonic_time(:second)
    end_time = start_time + duration

    workers =
      for _ <- 1..concurrency do
        spawn_link(fn -> worker_loop(url, request_timeout, parent, end_time) end)
      end

    # Collect results
    results = collect_results(length(workers), %{
      total: 0,
      success: 0,
      errors: 0,
      response_times: []
    })

    # Print summary
    print_summary(results, duration)
  end

  defp worker_loop(url, timeout, parent, end_time) do
    if System.monotonic_time(:second) >= end_time do
      send(parent, {:done, self()})
    else
      start_time = System.monotonic_time(:millisecond)

      result =
        case HTTPoison.get(url, [], timeout: timeout) do
          {:ok, %HTTPoison.Response{status_code: code}} when code in 200..299 ->
            {:success, System.monotonic_time(:millisecond) - start_time}
          {:ok, %HTTPoison.Response{status_code: code}} ->
            {:error, "HTTP #{code}"}
          {:error, reason} ->
            {:error, inspect(reason)}
        end

      send(parent, {:result, result})
      worker_loop(url, timeout, parent, end_time)
    end
  end

  defp collect_results(remaining, acc) when remaining > 0 do
    receive do
      {:result, {:success, time}} ->
        collect_results(remaining, %{
          acc |
          total: acc.total + 1,
          success: acc.success + 1,
          response_times: [time | acc.response_times]
        })

      {:result, {:error, _reason}} ->
        collect_results(remaining, %{
          acc |
          total: acc.total + 1,
          errors: acc.errors + 1
        })

      {:done, _pid} ->
        collect_results(remaining - 1, acc)
    end
  end

  defp collect_results(0, acc), do: acc

  defp print_summary(results, duration) do
    avg_time = if length(results.response_times) > 0 do
      Enum.sum(results.response_times) / length(results.response_times)
    else
      0
    end

    Logger.info("""
    Load Test Summary:
    =================
    Total Requests: #{results.total}
    Successful: #{results.success}
    Errors: #{results.errors}
    Requests/sec: #{results.total / duration}
    Avg Response Time: #{avg_time} ms
    """)
  end
end

# mix.exs
defmodule LoadTest.MixProject do
  use Mix.Project

  def project do
    [
      app: :load_test,
      version: "0.1.0",
      elixir: "~> 1.12",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger]
    ]
  end

  defp deps do
    [
      {:httpoison, "~> 1.8"}
    ]
  end
end
```
