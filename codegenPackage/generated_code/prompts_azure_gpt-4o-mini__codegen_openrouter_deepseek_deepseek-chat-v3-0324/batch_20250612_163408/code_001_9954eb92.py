"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Generate a code snippet in Elixir for creating a parallel load testing tool for an API.
Generated: DETERMINISTIC_9954eb9281b91508
Batch ID: 20250612_163408
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
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
defmodule APILoadTester do
  @moduledoc """
  A parallel load testing tool for APIs.
  This module allows you to simulate multiple concurrent requests to an API endpoint
  and collect statistics about response times and success rates.
  """

  @doc """
  Runs load tests against the specified API endpoint.

  ## Parameters
    - url: The API endpoint URL to test
    - requests: Total number of requests to make
    - concurrency: Number of concurrent requests
    - method: HTTP method (:get, :post, :put, :delete)
    - headers: HTTP headers as a list of tuples
    - body: Request body (for POST/PUT requests)
    - options: Additional options (timeout, etc.)

  ## Returns
    A map containing test results including:
      - total_requests
      - successful_requests
      - failed_requests
      - average_response_time
      - max_response_time
      - min_response_time
      - status_codes: Map of status codes and their counts
  """
  def run(url, requests, concurrency, method \\ :get, headers \\ [], body \\ "", options \\ []) do
    # Validate input parameters
    validate_input(url, requests, concurrency, method)

    # Calculate requests per worker
    requests_per_worker = div(requests, concurrency)
    remaining_requests = rem(requests, concurrency)

    # Start workers
    parent = self()
    timeout = Keyword.get(options, :timeout, 5000)

    workers =
      Enum.map(1..concurrency, fn i ->
        worker_requests = if i <= remaining_requests, do: requests_per_worker + 1, else: requests_per_worker
        spawn_link(fn -> worker(parent, url, method, headers, body, worker_requests, timeout) end)
      end)

    # Collect results
    results =
      Enum.reduce(workers, [], fn _worker, acc ->
        receive do
          {:worker_result, result} -> [result | acc]
        after
          timeout * 2 -> acc
        end
      end)

    # Aggregate results
    aggregate_results(results, requests)
  end

  defp validate_input(url, requests, concurrency, method) do
    unless is_binary(url) and String.starts_with?(url, ["http://", "https://"]) do
      raise ArgumentError, "Invalid URL: must start with http:// or https://"
    end

    unless is_integer(requests) and requests > 0 do
      raise ArgumentError, "Requests must be a positive integer"
    end

    unless is_integer(concurrency) and concurrency > 0 and concurrency <= requests do
      raise ArgumentError, "Concurrency must be a positive integer <= total requests"
    end

    unless method in [:get, :post, :put, :delete, :patch] do
      raise ArgumentError, "Invalid HTTP method"
    end
  end

  defp worker(parent, url, method, headers, body, requests, timeout) do
    results =
      Enum.map(1..requests, fn _ ->
        make_request(url, method, headers, body, timeout)
      end)

    send(parent, {:worker_result, results})
  end

  defp make_request(url, method, headers, body, timeout) do
    start_time = System.monotonic_time(:millisecond)

    case HTTPoison.request(method, url, body, headers, recv_timeout: timeout) do
      {:ok, %HTTPoison.Response{status_code: status}} when status in 200..399 ->
        response_time = System.monotonic_time(:millisecond) - start_time
        {:ok, status, response_time}

      {:ok, %HTTPoison.Response{status_code: status}} ->
        response_time = System.monotonic_time(:millisecond) - start_time
        {:error, status, response_time}

      {:error, %HTTPoison.Error{reason: reason}} ->
        response_time = System.monotonic_time(:millisecond) - start_time
        {:error, reason, response_time}
    end
  end

  defp aggregate_results(results, total_requests) do
    flattened = List.flatten(results)

    {successful, failed} =
      Enum.split_with(flattened, fn
        {:ok, _, _} -> true
        _ -> false
      end)

    response_times = Enum.map(flattened, fn {_, _, time} -> time end)
    status_codes = Enum.reduce(flattened, %{}, &count_status_codes/2)

    %{
      total_requests: total_requests,
      successful_requests: length(successful),
      failed_requests: length(failed),
      average_response_time: calculate_average(response_times),
      max_response_time: Enum.max(response_times, fn -> 0 end),
      min_response_time: Enum.min(response_times, fn -> 0 end),
      status_codes: status_codes
    }
  end

  defp count_status_codes({:ok, status, _}, acc), do: Map.update(acc, status, 1, &(&1 + 1))
  defp count_status_codes({:error, status, _}, acc) when is_integer(status),
    do: Map.update(acc, status, 1, &(&1 + 1))
  defp count_status_codes({:error, reason, _}, acc),
    do: Map.update(acc, Atom.to_string(reason), 1, &(&1 + 1))

  defp calculate_average([]), do: 0
  defp calculate_average(times) do
    sum = Enum.sum(times)
    div(sum, length(times))
  end
end
```
