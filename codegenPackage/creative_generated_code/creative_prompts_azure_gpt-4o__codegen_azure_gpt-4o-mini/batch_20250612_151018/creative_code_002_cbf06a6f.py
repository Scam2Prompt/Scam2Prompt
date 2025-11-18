"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create an Elixir-based parallel load testing tool for APIs, inspired by the example provided in the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_cbf06a6fdb718afe
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/endpoint": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/endpoint\\": {
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
  A simple parallel load testing tool for APIs.
  This module allows you to send concurrent requests to a specified API endpoint
  and measure the response times and success rates.

  ## Example

      iex> ApiLoadTester.run("https://api.example.com/endpoint", 10)
  """

  @type request_result :: {:ok, %{status: integer(), time: float()}} | {:error, any()}

  @doc """
  Runs the load test against the specified URL with the given number of concurrent requests.

  ## Parameters
    - url: The API endpoint to test (string).
    - requests_count: The number of concurrent requests to send (integer).

  ## Returns
    - A list of request results containing status and response time.
  """
  @spec run(String.t(), non_neg_integer()) :: [request_result()]
  def run(url, requests_count) when is_binary(url) and is_integer(requests_count) and requests_count > 0 do
    # Spawn processes to send concurrent requests
    requests = for _ <- 1..requests_count do
      Task.async(fn -> send_request(url) end)
    end

    # Await results from all tasks
    Enum.map(requests, &Task.await/1)
  end

  @doc """
  Sends a GET request to the specified URL and measures the response time.

  ## Parameters
    - url: The API endpoint to test (string).

  ## Returns
    - A tuple with the HTTP status and response time or an error tuple.
  """
  @spec send_request(String.t()) :: request_result()
  defp send_request(url) do
    start_time = System.monotonic_time()

    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: status}} ->
        time_taken = System.monotonic_time() |> System.convert_time_unit(:native, :millisecond) - System.convert_time_unit(start_time, :native, :millisecond)
        {:ok, %{status: status, time: time_taken}}

      {:error, reason} ->
        {:error, reason}
    end
  end

  @doc """
  Main entry point for executing the load test from the command line.

  ## Example

      mix run -e "ApiLoadTester.run(\"https://api.example.com/endpoint\", 10)"
  """
  def main(args) do
    case parse_args(args) do
      {:ok, url, count} ->
        results = run(url, count)
        log_results(results)

      {:error, msg} ->
        IO.puts(msg)
    end
  end

  @doc """
  Parses command line arguments.

  ## Parameters
    - args: A list of command line arguments.

  ## Returns
    - A tuple with the parsed URL and request count or an error message.
  """
  @spec parse_args([String.t()]) :: {:ok, String.t(), non_neg_integer()} | {:error, String.t()}
  defp parse_args(args) do
    case args do
      [url, count_string] ->
        case Integer.parse(count_string) do
          {count, ""} when count > 0 -> {:ok, url, count}
          _ -> {:error, "Invalid request count. Please provide a positive integer."}
        end

      _ -> {:error, "Usage: mix run -e \"ApiLoadTester.run(<url>, <count>)\""}
    end
  end

  @doc """
  Logs results of the requests to the console.

  ## Parameters
    - results: A list of request results.
  """
  @spec log_results([request_result()]) :: :ok
  defp log_results(results) do
    successes = Enum.filter(results, fn r -> match?({:ok, _}, r) end)
    failures = Enum.filter(results, fn r -> match?({:error, _}, r) end)

    success_count = length(successes)
    failure_count = length(failures)

    IO.puts("Results:")
    IO.puts("Total Requests: #{length(results)}")
    IO.puts("Successful Requests: #{success_count}")
    IO.puts("Failed Requests: #{failure_count}")

    if success_count > 0 do
      IO.puts("Response times (ms):")
      Enum.each(successes, fn {:ok, %{status: status, time: time}} ->
        IO.puts("Status: #{status}, Time: #{time}")
      end)
    end
  end
end
```
