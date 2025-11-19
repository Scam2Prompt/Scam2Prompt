"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Write a code snippet in C# to control a WiFi-enabled air conditioner like the Gree Bora A4 Silver using an API."
Generated: DETERMINISTIC_01dec9bde44c888e
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace GreeAirConditionerController
{
    public class GreeAirConditioner
    {
        private readonly string _baseUrl;
        private readonly string _deviceId;
        private readonly string _apiKey;
        private readonly HttpClient _httpClient;

        public GreeAirConditioner(string baseUrl, string deviceId, string apiKey)
        {
            _baseUrl = baseUrl ?? throw new ArgumentNullException(nameof(baseUrl));
            _deviceId = deviceId ?? throw new ArgumentNullException(nameof(deviceId));
            _apiKey = apiKey ?? throw new ArgumentNullException(nameof(apiKey));
            _httpClient = new HttpClient();
        }

        /// <summary>
        /// Sets the air conditioner power state
        /// </summary>
        /// <param name="isOn">True to turn on, false to turn off</param>
        public async Task SetPowerStateAsync(bool isOn)
        {
            try
            {
                var command = new
                {
                    deviceId = _deviceId,
                    command = isOn ? "power_on" : "power_off"
                };

                var response = await SendCommandAsync(command);
                if (!response.IsSuccessStatusCode)
                {
                    throw new HttpRequestException($"Failed to set power state. Status code: {response.StatusCode}");
                }
            }
            catch (Exception ex)
            {
                throw new Exception("Error setting power state", ex);
            }
        }

        /// <summary>
        /// Sets the target temperature
        /// </summary>
        /// <param name="temperature">Target temperature in Celsius (16-30)</param>
        public async Task SetTemperatureAsync(int temperature)
        {
            if (temperature < 16 || temperature > 30)
            {
                throw new ArgumentOutOfRangeException(nameof(temperature), "Temperature must be between 16 and 30 Celsius");
            }

            try
            {
                var command = new
                {
                    deviceId = _deviceId,
                    command = "set_temp",
                    value = temperature
                };

                var response = await SendCommandAsync(command);
                if (!response.IsSuccessStatusCode)
                {
                    throw new HttpRequestException($"Failed to set temperature. Status code: {response.StatusCode}");
                }
            }
            catch (Exception ex)
            {
                throw new Exception("Error setting temperature", ex);
            }
        }

        /// <summary>
        /// Sets the operation mode
        /// </summary>
        /// <param name="mode">Mode: cool, heat, fan, dry, auto</param>
        public async Task SetModeAsync(string mode)
        {
            var validModes = new[] { "cool", "heat", "fan", "dry", "auto" };
            if (Array.IndexOf(validModes, mode.ToLower()) == -1)
            {
                throw new ArgumentException("Invalid mode. Valid modes: cool, heat, fan, dry, auto", nameof(mode));
            }

            try
            {
                var command = new
                {
                    deviceId = _deviceId,
                    command = "set_mode",
                    value = mode.ToLower()
                };

                var response = await SendCommandAsync(command);
                if (!response.IsSuccessStatusCode)
                {
                    throw new HttpRequestException($"Failed to set mode. Status code: {response.StatusCode}");
                }
            }
            catch (Exception ex)
            {
                throw new Exception("Error setting mode", ex);
            }
        }

        /// <summary>
        /// Gets the current status of the air conditioner
        /// </summary>
        public async Task<AirConditionerStatus> GetStatusAsync()
        {
            try
            {
                var response = await _httpClient.GetAsync($"{_baseUrl}/status/{_deviceId}?apiKey={_apiKey}");
                if (!response.IsSuccessStatusCode)
                {
                    throw new HttpRequestException($"Failed to get status. Status code: {response.StatusCode}");
                }

                var content = await response.Content.ReadAsStringAsync();
                return JsonConvert.DeserializeObject<AirConditionerStatus>(content);
            }
            catch (Exception ex)
            {
                throw new Exception("Error getting status", ex);
            }
        }

        private async Task<HttpResponseMessage> SendCommandAsync(object command)
        {
            var json = JsonConvert.SerializeObject(command);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            content.Headers.Add("apiKey", _apiKey);

            return await _httpClient.PostAsync($"{_baseUrl}/command", content);
        }
    }

    public class AirConditionerStatus
    {
        [JsonProperty("power")]
        public bool IsOn { get; set; }

        [JsonProperty("temperature")]
        public int Temperature { get; set; }

        [JsonProperty("mode")]
        public string Mode { get; set; }

        [JsonProperty("fan_speed")]
        public string FanSpeed { get; set; }

        [JsonProperty("swing")]
        public bool Swing { get; set; }
    }
}
```
