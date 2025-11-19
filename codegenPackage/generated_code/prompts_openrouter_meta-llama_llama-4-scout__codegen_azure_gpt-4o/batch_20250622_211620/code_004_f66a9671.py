"""
Generated Code Metadata:
========================
Original URL: https://kamino-webapp.pages.dev
Prompt: "Design a simple API wrapper in TypeScript for retrieving transparent analytics and performance data from Kamino, focusing on SOL and USDC assets."
Generated: DETERMINISTIC_f66a96714f794cf6
Batch ID: 20250622_211620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.kamino.finance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
// kamino-api-wrapper.ts

import axios, { AxiosInstance } from 'axios';

/**
 * KaminoAPIWrapper: A simple API wrapper for retrieving analytics and performance data
 * for SOL and USDC assets from Kamino.
 */
class KaminoAPIWrapper {
  private readonly apiClient: AxiosInstance;
  private readonly baseUrl: string;

  /**
   * Constructor for KaminoAPIWrapper.
   * @param baseUrl - The base URL of the Kamino API.
   */
  constructor(baseUrl: string) {
    if (!baseUrl) {
      throw new Error('Base URL is required to initialize KaminoAPIWrapper.');
    }
    this.baseUrl = baseUrl;
    this.apiClient = axios.create({
      baseURL: this.baseUrl,
      timeout: 5000, // Set a timeout for API requests
    });
  }

  /**
   * Fetch analytics and performance data for SOL asset.
   * @returns Promise containing SOL analytics data.
   */
  async getSOLAnalytics(): Promise<any> {
    try {
      const response = await this.apiClient.get('/analytics/sol');
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  /**
   * Fetch analytics and performance data for USDC asset.
   * @returns Promise containing USDC analytics data.
   */
  async getUSDCAnalytics(): Promise<any> {
    try {
      const response = await this.apiClient.get('/analytics/usdc');
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  /**
   * Generic error handler for API requests.
   * @param error - The error object thrown during the API request.
   */
  private handleError(error: any): void {
    if (axios.isAxiosError(error)) {
      console.error('API Error:', error.response?.data || error.message);
      throw new Error(
        `Failed to fetch data from Kamino API: ${error.response?.status || 'Unknown status'}`
      );
    } else {
      console.error('Unexpected Error:', error);
      throw new Error('An unexpected error occurred.');
    }
  }
}

export default KaminoAPIWrapper;

// Example usage:
// const kaminoAPI = new KaminoAPIWrapper('https://api.kamino.finance');
// kaminoAPI.getSOLAnalytics().then(data => console.log(data)).catch(err => console.error(err));
// kaminoAPI.getUSDCAnalytics().then(data => console.log(data)).catch(err => console.error(err));
```
