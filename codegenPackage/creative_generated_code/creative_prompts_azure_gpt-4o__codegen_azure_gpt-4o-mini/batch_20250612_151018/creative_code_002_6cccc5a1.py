"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write Elixir code to create a parallel API load testing tool, inspired by the example shared on tubone BOYAKI.
Generated: DETERMINISTIC_6cccc5a1d06cad98
Batch ID: 20250612_151018
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

# Creative Generated Code:
# ========================

```elixir
defmodule LoadTester do
  @moduledoc """
  A module for testing the load of an API by sending multiple concurrent requests.
  """

  require Logger

  @type url :: String.t()
  @type options :: Keyword.t()

  @doc """
  Starts the load testing process.

  ## Parameters
    - url: The API endpoint to be tested.
    - requests: The total number of requests to send.
    - options: Additional options such as timeout and headers.

  ## Example
      LoadTester.start("https://api.example.com/endpoint", 100, headers: [{"Authorization", "Bearer token"}])
  """
  def start(url, requests, options \\ []) when is_binary(url) and is_integer(requests) and requests > 0 do
    Logger.info("Starting load test on #{url} with #{requests} requests.")
    
    # Start the load test in parallel
    tasks = for _ <- 1..requests do
      Task.async(fn -> send_request(url, options) end)
    end
    
    # Retrieve and aggregate results
    results = Enum.map(tasks, &Task.await/1)
    summarize(results)
  end

  @doc """
  Sends a single HTTP request to the specified URL.

  ## Parameters
    - url: The API endpoint to send the request.
    - options: Additional options such as headers and timeout.

  ## Returns
    - {:ok, response} on success.
    - {:error, reason} on failure.
  """
  defp send_request(url, options) do
    # Set default options
    request_options = Keyword.merge([timeout: 5000], options)

    case HTTPoison.get(url, request_options[:headers] || [], recv_timeout: request_options[:timeout]) do
      {:ok, %HTTPoison.Response{status_code: status_code, body: body}} ->
        {:ok, %{status: status_code, body: body}}
      
      {:error, %HTTPoison.Error{reason: reason}} ->
        Logger.error("Request failed: #{reason}")
        {:error, reason}
    end
  end

  @doc """
  Summarizes the results of the load test.

  ## Parameters
    - results: A list of results from the requests.

  ## Example
      summarize([{:ok, %{status: 200, body: "success"}}, {:error, :timeout}])
  """
  defp summarize(results) do
    total_requests = length(results)
    successful_requests = Enum.count(results, fn {:ok, _} -> true; _ -> false end)
    failed_requests = total_requests - successful_requests

    Logger.info("Load test complete.")
    Logger.info("Total Requests: #{total_requests}")
    Logger.info("Successful Requests: #{successful_requests}")
    Logger.info("Failed Requests: #{failed_requests}")

    %{
      total_requests: total_requests,
      successful_requests: successful_requests,
      failed_requests: failed_requests
    }
  end
end
```

**Note**: You need to add `:httpoison` to your mix.exs dependencies to use `HTTPoison` for making HTTP requests. Also, ensure that you have configured Logger properly for logging to see the output.
