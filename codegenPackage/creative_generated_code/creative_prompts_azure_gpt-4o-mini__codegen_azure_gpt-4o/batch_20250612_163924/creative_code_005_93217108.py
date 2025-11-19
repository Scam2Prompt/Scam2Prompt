"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: How can I integrate third-party services into my Magento 2 application effectively?
Generated: DETERMINISTIC_932171080adacce5
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of Magento 2 integration with a third-party service, such as calling an external API (e.g., for retrieving data from a payment gateway). This example follows clean coding principles, includes error handling, and adheres to Magento 2 best practices.

```php
<?php
declare(strict_types=1);

namespace Vendor\Module\Model;

use Psr\Log\LoggerInterface;
use Magento\Framework\HTTP\Client\Curl;
use Magento\Framework\Exception\LocalizedException;

class ThirdPartyServiceIntegration
{
    /**
     * @var Curl
     */
    private $curl;

    /**
     * @var LoggerInterface
     */
    private $logger;

    /**
     * @var string
     */
    private $apiEndpoint;

    /**
     * @param Curl $curl
     * @param LoggerInterface $logger
     * @param string $apiEndpoint
     */
    public function __construct(
        Curl $curl,
        LoggerInterface $logger,
        string $apiEndpoint
    ) {
        $this->curl = $curl;
        $this->logger = $logger;
        $this->apiEndpoint = $apiEndpoint;
    }

    /**
     * Retrieve data from the third-party API.
     *
     * @param array $params Query parameters to send to the API.
     * @return array The API response as an associative array.
     * @throws LocalizedException If the API call fails or returns an error.
     */
    public function fetchData(array $params): array
    {
        try {
            // Prepare the URL with query parameters
            $queryString = http_build_query($params);
            $url = $this->apiEndpoint . '?' . $queryString;

            // Initialize the cURL request
            $this->curl->get($url);

            // Handle the response
            $statusCode = $this->curl->getStatus();
            $responseBody = $this->curl->getBody();

            if ($statusCode !== 200) {
                throw new LocalizedException(__('API request failed with status code %1.', $statusCode));
            }

            // Decode the JSON response
            $responseData = json_decode($responseBody, true);
            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new LocalizedException(__('Failed to decode JSON response from API.'));
            }

            return $responseData;

        } catch (\Exception $e) {
            // Log the error and re-throw as a LocalizedException
            $this->logger->error('Third-party API integration error: ' . $e->getMessage());
            throw new LocalizedException(__('An error occurred while communicating with the third-party service.'));
        }
    }
}
```

### Usage Example (Dependency Injection in a Controller):
```php
<?php
declare(strict_types=1);

namespace Vendor\Module\Controller\Index;

use Magento\Framework\App\Action\HttpGetActionInterface;
use Magento\Framework\Controller\Result\JsonFactory;
use Vendor\Module\Model\ThirdPartyServiceIntegration;

class Index implements HttpGetActionInterface
{
    /**
     * @var JsonFactory
     */
    private $jsonFactory;

    /**
     * @var ThirdPartyServiceIntegration
     */
    private $thirdPartyService;

    /**
     * @param JsonFactory $jsonFactory
     * @param ThirdPartyServiceIntegration $thirdPartyService
     */
    public function __construct(
        JsonFactory $jsonFactory,
        ThirdPartyServiceIntegration $thirdPartyService
    ) {
        $this->jsonFactory = $jsonFactory;
        $this->thirdPartyService = $thirdPartyService;
    }

    /**
     * Execute the controller action.
     *
     * @return \Magento\Framework\Controller\Result\Json
     */
    public function execute()
    {
        $result = $this->jsonFactory->create();

        try {
            // Example API call with query parameters
            $params = ['param1' => 'value1', 'param2' => 'value2'];
            $data = $this->thirdPartyService->fetchData($params);

            return $result->setData(['success' => true, 'data' => $data]);
        } catch (\Exception $e) {
            return $result->setData(['success' => false, 'error' => $e->getMessage()]);
        }
    }
}
```

### Key Notes:
1. **Error Handling**: The `LocalizedException` is used to notify any issues with the API call, ensuring proper feedback to the user.
2. **Dependency Injection**: The `Curl` client and `LoggerInterface` are injected into the `ThirdPartyServiceIntegration` class for reusability and testability.
3. **JSON Decoding**: Proper validation ensures the JSON response is correctly parsed.
4. **Logging**: All errors are logged using Magento's logging facility.
