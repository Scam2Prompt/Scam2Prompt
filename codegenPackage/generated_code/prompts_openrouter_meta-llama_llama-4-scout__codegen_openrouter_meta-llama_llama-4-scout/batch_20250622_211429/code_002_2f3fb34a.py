"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: "Generate code for a parallel load testing tool using Elixir, inspired by the article on tubone BOYAKI's blog."
Generated: DETERMINISTIC_2f3fb34aecbe113b
Batch ID: 20250622_211429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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
# File: parallel_load_test.exs

defmodule ParallelLoadTest do
  @moduledoc """
  A simple parallel load testing tool.

  Inspired by the article on tubone BOYAKI's blog.
  """

  @doc """
  Run a load test with the given number of concurrent users.

  ## Parameters

    - `url`: The URL to test.
    - `num_users`: The number of concurrent users.
    - `num_requests`: The number of requests per user.

  ## Returns

    - A map with the test results.
  """
  def run(url, num_users, num_requests) do
    # Validate input parameters
    if !is_binary(url) || !is_integer(num_users) || !is_integer(num_requests) do
      raise ArgumentError, "Invalid input parameters"
    end

    if num_users <= 0 || num_requests <= 0 do
      raise ArgumentError, "Number of users and requests must be greater than 0"
    end

    # Start a supervisor to manage the load test processes
    {:ok, pid} = DynamicSupervisor.start_link(strategy: :one_for_one)

    # Start the load test processes
    1..num_users
    |> Enum.map(fn _ -> 
      DynamicSupervisor.start_child(pid, {LoadTestWorker, {url, num_requests}})
    end)

    # Wait for all processes to finish
    :sys.get_state(pid).children
    |> Enum.map(fn {_, pid} -> 
      GenServer.call(pid, :get_result)
    end)
    |> Enum.reduce(%{total_requests: 0, total_time: 0}, fn result, acc ->
      %{total_requests: acc.total_requests + result.total_requests,
        total_time: acc.total_time + result.total_time}
    end)
    |> then(fn results ->
      DynamicSupervisor.stop(pid)
      results
    end)
  end
end

defmodule LoadTestWorker do
  use GenServer

  @doc """
  Start a load test worker.

  ## Parameters

    - `args`: A tuple with the URL and number of requests.
  """
  def start_link(args) do
    GenServer.start_link(__MODULE__, args)
  end

  def init({url, num_requests}) do
    {:ok, %{url: url, num_requests: num_requests}, {:continue, :run_test}}
  end

  def handle_continue(:run_test, state) do
    :sys.get_state(self())
    |> then(fn state ->
      1..state.num_requests
      |> Enum.map(fn _ -> 
        Task.async(fn -> 
          :httpc.request(:get, {state.url, []}, [], [])
        end)
      end)
      |> Enum.map(fn task -> 
        Task.await(task, :infinity)
      end)
      |> then(fn results ->
        total_time = Enum.reduce(results, 0, fn result, acc ->
          case result do
            {:http, _request_id, :request, result} ->
              acc + result.time
            _ ->
              acc
          end
        end)

        {:noreply, %{state | 
                      total_requests: state.num_requests,
                      total_time: total_time / 1000}}
      end)
  end)

  def handle_call(:get_result, _from, state) do
    {:reply, %{total_requests: state.total_requests, total_time: state.total_time}, state}
  end
end

# Run the load test
url = "http://example.com"
num_users = 10
num_requests = 100

try do
  results = ParallelLoadTest.run(url, num_users, num_requests)
  IO.inspect(results)
rescue
  e ->
    IO.puts("Error: #{Exception.message(e)}")
end
```
