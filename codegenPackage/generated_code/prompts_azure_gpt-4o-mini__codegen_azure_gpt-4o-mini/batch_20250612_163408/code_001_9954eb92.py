"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Generate a code snippet in Elixir for creating a parallel load testing tool for an API.
Generated: DETERMINISTIC_9954eb9281b91508
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/endpoint": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```elixir
defmodule LoadTester do
  @moduledoc """
  A simple parallel load testing tool for an API.
  This module allows you to send multiple requests to a specified API endpoint
  concurrently and collect the results.
  """

  @type request_result :: {:ok, any()} | {:error, any()}

  @doc """
  Sends a specified number of requests to the given URL in parallel.

  ## Parameters
  - url: The API endpoint to test.
  - num_requests: The number of requests to send.

  ## Returns
  A list of results for each request.
  """
  def run_load_test(url, num_requests) when is_binary(url) and is_integer(num_requests) and num_requests > 0 do
    # Create a list of tasks for concurrent execution
    tasks = for _ <- 1..num_requests do
      Task.async(fn -> send_request(url) end)
    end

    # Await the results of all tasks
    Enum.map(tasks, &Task.await/1)
  end

  @doc """
  Sends a single GET request to the specified URL.

  ## Parameters
  - url: The API endpoint to test.

  ## Returns
  A tuple indicating the result of the request.
  """
  defp send_request(url) do
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: status_code, body: body}} ->
        {:ok, %{status_code: status_code, body: body}}

      {:error, %HTTPoison.Error{reason: reason}} ->
        {:error, reason}
    end
  end
end

# Example usage:
# LoadTester.run_load_test("https://api.example.com/endpoint", 100)
```

Make sure to include the `:httpoison` dependency in your `mix.exs` file to use the HTTPoison library for making HTTP requests:

```elixir
defp deps do
  [
    {:httpoison, "~> 1.8"}
  ]
end
```
