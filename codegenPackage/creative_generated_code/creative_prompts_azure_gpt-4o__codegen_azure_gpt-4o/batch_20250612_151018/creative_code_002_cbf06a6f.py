"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create an Elixir-based parallel load testing tool for APIs, inspired by the example provided in the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_cbf06a6fdb718afe
Batch ID: 20250612_151018
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
defmodule ParallelApiLoadTester do
  @moduledoc """
  A simple Elixir-based parallel load testing tool for APIs.

  Usage:
    ParallelApiLoadTester.run("https://example.com/api", 100, 10)

  This will make 100 requests to the API in batches of 10 concurrent requests.
  """

  require Logger
  alias Task.Supervisor

  @doc """
  Starts the load testing process.

  ## Parameters:
    - url: The API endpoint to test (String).
    - total_requests: The total number of requests to send (Integer).
    - concurrency: The number of concurrent requests (Integer).

  ## Returns:
    - :ok when all requests have been completed.
  """
  def run(url, total_requests, concurrency) when is_binary(url) and is_integer(total_requests) and is_integer(concurrency) do
    Logger.info("Starting load test for #{url}")
    Logger.info("Total Requests: #{total_requests}, Concurrency: #{concurrency}")

    Supervisor.start_link([], strategy: :one_for_one, name: LoadTestSupervisor)

    # Split requests into batches based on concurrency
    1..total_requests
    |> Enum.chunk_every(concurrency)
    |> Enum.each(fn batch ->
      Logger.info("Processing batch of size #{length(batch)}")
      tasks =
        batch
        |> Enum.map(fn _ ->
          Task.Supervisor.async(LoadTestSupervisor, fn -> make_request(url) end)
        end)

      # Await results for the current batch
      Enum.each(tasks, fn task ->
        case Task.await(task, 5_000) do
          {:ok, response} ->
            Logger.info("Request succeeded: #{inspect(response)}")

          {:error, reason} ->
            Logger.error("Request failed: #{inspect(reason)}")
        end
      end)
    end)

    Logger.info("All requests completed.")
    :ok
  end

  @doc """
  Makes an HTTP GET request to the given URL.

  ## Parameters:
    - url: The URL to send the GET request to.

  ## Returns:
    - {:ok, response} if the request is successful.
    - {:error, reason} if the request fails.
  """
  defp make_request(url) do
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: 200, body: body}} ->
        {:ok, body}

      {:ok, %HTTPoison.Response{status_code: status_code}} ->
        {:error, "Non-200 status code: #{status_code}"}

      {:error, %HTTPoison.Error{reason: reason}} ->
        {:error, reason}
    end
  rescue
    exception ->
      {:error, Exception.message(exception)}
  end
end
```

### Notes:
- This code assumes `HTTPoison` is available as a dependency. Add it to your `mix.exs` file:
  ```elixir
  defp deps do
    [
      {:httpoison, "~> 1.8"}
    ]
  end
  ```
- Run `mix deps.get` to fetch the dependency before running the tool.
- Adjust the timeout (`5_000` ms) as needed for your use case.
