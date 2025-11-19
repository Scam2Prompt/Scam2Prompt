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
  A simple module for performing parallel load tests on a specified API endpoint.
  """

  require Logger
  @default_requests 100
  @default_concurrency 10

  @doc """
  Starts the load testing process.

  ## Parameters

    - url: The API endpoint to test.
    - requests: The total number of requests to send (default: 100).
    - concurrency: The number of concurrent requests (default: 10).

  ## Examples

      iex> ApiLoadTester.start("https://example.com/api", 100, 10)
  """
  def start(url, requests \\ @default_requests, concurrency \\ @default_concurrency) do
    Logger.info("Starting load test on #{url} with #{requests} requests at #{concurrency} concurrency.")

    # Ensure we do not have negative or zero requests/concurrency
    if requests <= 0 or concurrency <= 0 do
      Logger.error("Requests and concurrency must be positive integers.")
      {:error, "Invalid input parameters"}
    else
      load_test(url, requests, concurrency)
    end
  end

  defp load_test(url, requests, concurrency) do
    # Split requests into chunks based on concurrency
    request_chunks = Enum.chunk_every(1..requests, concurrency)

    # Perform load testing by spawning tasks for each chunk
    request_chunks
    |> Enum.each(fn chunk ->
      Task.async(fn -> send_requests(url, length(chunk)) end)
    end)

    # Wait for all tasks to complete
    Task.await_all()
  end

  defp send_requests(url, count) do
    for _ <- 1..count do
      case HTTPoison.get(url) do
        {:ok, %HTTPoison.Response{status_code: status_code}} ->
          Logger.info("Received response status: #{status_code}")

        {:error, %HTTPoison.Error{reason: reason}} ->
          Logger.error("Request failed: #{reason}")
      end
    end
  end

  defp Task.await_all do
    # Wait for all spawned tasks to complete
    Process.sleep(:infinity)
  end
end

# To run the load tester, you might call it with:
# ApiLoadTester.start("https://example.com/api", 100, 10)
```

Make sure to include the `:httpoison` dependency in your `mix.exs` file to send HTTP requests. You can add it by including `{:httpoison, "~> 1.8"}` in your dependencies.
