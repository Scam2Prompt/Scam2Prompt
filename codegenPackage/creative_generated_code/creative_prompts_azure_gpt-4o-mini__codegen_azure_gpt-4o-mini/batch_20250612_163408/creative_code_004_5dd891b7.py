"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate code to implement a load testing tool in Elixir, inspired by the article on tubone BOYAKI.
Generated: DETERMINISTIC_5dd891b77d481dbf
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
defmodule LoadTester do
  @moduledoc """
  A simple load testing tool that sends concurrent requests to a specified endpoint.
  
  ## Usage
  To run the load tester, use the `start/2` function with the URL and the number of requests.
  """

  require Logger

  @default_concurrency 10

  @doc """
  Starts the load testing process.

  ## Parameters
    - url: The endpoint URL to test.
    - number_of_requests: The total number of requests to send.
  """
  def start(url, number_of_requests) when is_binary(url) and is_integer(number_of_requests) do
    Logger.info("Starting load test on #{url} with #{number_of_requests} requests")

    # Launch concurrent tasks to send requests
    1..number_of_requests
    |> Enum.chunk_every(@default_concurrency)
    |> Enum.each(&send_requests(&1, url))

    Logger.info("Load test completed.")
  end

  @doc """
  Sends a batch of requests to the specified URL.

  ## Parameters
    - requests: A list of request identifiers.
    - url: The endpoint URL to test.
  """
  defp send_requests(requests, url) do
    tasks = Enum.map(requests, fn _ ->
      Task.async(fn -> send_request(url) end)
    end)

    # Await results and log any errors
    Enum.each(tasks, fn task ->
      case Task.await(task, 5000) do
        {:ok, response} -> Logger.info("Received response: #{response}")
        {:error, reason} -> Logger.error("Request failed: #{reason}")
      end
    end)
  end

  @doc """
  Sends a single request to the specified URL.

  ## Parameters
    - url: The endpoint URL to test.

  ## Returns
    - {:ok, response} on success
    - {:error, reason} on failure
  """
  defp send_request(url) do
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: code, body: body}} ->
        {:ok, %{status: code, body: body}}

      {:error, %HTTPoison.Error{reason: reason}} ->
        {:error, reason}
    end
  end
end

# Example: Run the load tester
# LoadTester.start("https://example.com", 100)
```

**Note**: To run this code, ensure you have the `httpoison` library added to your `mix.exs` dependencies.
