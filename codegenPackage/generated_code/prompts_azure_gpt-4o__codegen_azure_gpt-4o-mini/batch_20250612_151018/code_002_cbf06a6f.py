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
defmodule LoadTester do
  @moduledoc """
  A simple parallel load testing tool for APIs.
  
  This module allows you to send concurrent requests to a specified API endpoint
  and measure the response times and success rates.
  """

  require Logger

  @default_concurrency 10
  @default_requests 100

  @doc """
  Starts the load testing process.

  ## Parameters
  - url: The API endpoint to test.
  - concurrency: The number of concurrent requests to send (default: 10).
  - total_requests: The total number of requests to send (default: 100).
  """
  def start_load_test(url, concurrency \\ @default_concurrency, total_requests \\ @default_requests) do
    Logger.info("Starting load test on #{url} with #{total_requests} requests at #{concurrency} concurrency level.")

    # Create a list of tasks for concurrent execution
    tasks = for _ <- 1..total_requests do
      Task.async(fn -> send_request(url) end)
    end

    # Await results from all tasks
    results = Enum.map(tasks, &Task.await/1)

    # Analyze results
    analyze_results(results)
  end

  @doc """
  Sends a single HTTP request to the specified URL and returns the response time.

  ## Parameters
  - url: The API endpoint to test.

  ## Returns
  - A tuple containing the response time in milliseconds and the status code.
  """
  defp send_request(url) do
    start_time = System.monotonic_time()

    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: status_code}} ->
        response_time = System.monotonic_time() |> System.convert_time_unit(:native, :millisecond)
        {response_time, status_code}

      {:error, %HTTPoison.Error{reason: reason}} ->
        Logger.error("Request failed: #{reason}")
        {nil, :error}
    end
    |> handle_response_time(start_time)
  end

  @doc """
  Handles the response time calculation.

  ## Parameters
  - {response_time, status_code}: The response time and status code tuple.
  - start_time: The time when the request was initiated.

  ## Returns
  - A tuple containing the response time and status code.
  """
  defp handle_response_time({response_time, status_code}, start_time) do
    elapsed_time = System.monotonic_time() |> System.convert_time_unit(:native, :millisecond) - System.convert_time_unit(start_time, :native, :millisecond)
    {elapsed_time, status_code}
  end

  @doc """
  Analyzes the results of the load test and logs the summary.

  ## Parameters
  - results: A list of tuples containing response times and status codes.
  """
  defp analyze_results(results) do
    total_requests = length(results)
    successful_requests = Enum.count(results, fn {_, status} -> status == 200 end)
    failed_requests = total_requests - successful_requests
    average_response_time = Enum.reduce(results, 0, fn {time, _}, acc -> acc + (time || 0) end) / total_requests

    Logger.info("Load test completed.")
    Logger.info("Total requests: #{total_requests}")
    Logger.info("Successful requests: #{successful_requests}")
    Logger.info("Failed requests: #{failed_requests}")
    Logger.info("Average response time: #{average_response_time} ms")
  end
end
```

Make sure to include the `:httpoison` dependency in your `mix.exs` file to use the HTTP client:

```elixir
defp deps do
  [
    {:httpoison, "~> 1.8"}
  ]
end
```
