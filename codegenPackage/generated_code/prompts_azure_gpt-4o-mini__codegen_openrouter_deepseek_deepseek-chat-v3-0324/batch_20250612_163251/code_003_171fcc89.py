"""
Generated Code Metadata:
========================
Original URL: https://jcijobs.com
Prompt: Develop a code snippet in Ruby that fetches employee benefits information from the Johnson Controls API and formats it for display on a website.
Generated: DETERMINISTIC_171fcc8916217313
Batch ID: 20250612_163251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.johnsoncontrols.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

require 'net/http'
require 'json'
require 'uri'

module JohnsonControls
  class EmployeeBenefitsFetcher
    API_BASE_URL = 'https://api.johnsoncontrols.com'.freeze
    BENEFITS_ENDPOINT = '/employee/benefits'.freeze

    class ApiError < StandardError; end

    def initialize(employee_id:, api_key:)
      @employee_id = employee_id
      @api_key = api_key
    end

    # Fetches and formats employee benefits data
    # @return [Hash] Formatted benefits data ready for display
    # @raise [ApiError] if API request fails
    def fetch_and_format_benefits
      raw_data = fetch_benefits_data
      format_benefits_data(raw_data)
    rescue StandardError => e
      raise ApiError, "Failed to fetch benefits data: #{e.message}"
    end

    private

    def fetch_benefits_data
      uri = URI.parse("#{API_BASE_URL}#{BENEFITS_ENDPOINT}/#{@employee_id}")
      request = Net::HTTP::Get.new(uri)
      request['Authorization'] = "Bearer #{@api_key}"
      request['Accept'] = 'application/json'

      response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
        http.request(request)
      end

      unless response.is_a?(Net::HTTPSuccess)
        raise ApiError, "API request failed with status #{response.code}: #{response.body}"
      end

      JSON.parse(response.body)
    end

    def format_benefits_data(raw_data)
      {
        health_insurance: format_insurance(raw_data['health_insurance']),
        retirement: format_retirement(raw_data['retirement']),
        time_off: format_time_off(raw_data['time_off']),
        last_updated: Time.now.utc.iso8601
      }
    end

    def format_insurance(insurance_data)
      {
        provider: insurance_data['provider'],
        plan_type: insurance_data['plan_type'],
        coverage: insurance_data['coverage'],
        effective_date: insurance_data['effective_date']
      }
    end

    def format_retirement(retirement_data)
      {
        plan_type: retirement_data['plan_type'],
        employer_match: retirement_data['employer_match'],
        vested: retirement_data['vested']
      }
    end

    def format_time_off(time_off_data)
      {
        vacation_days: time_off_data['vacation_days'],
        sick_days: time_off_data['sick_days'],
        personal_days: time_off_data['personal_days']
      }
    end
  end
end

# Example usage:
# fetcher = JohnsonControls::EmployeeBenefitsFetcher.new(
#   employee_id: '12345',
#   api_key: 'your_api_key_here'
# )
# formatted_benefits = fetcher.fetch_and_format_benefits
```
