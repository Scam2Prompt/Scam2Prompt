"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Implement a ThinkPHP paginator service for handling large datasets, based on `PaginatorService.php` from the Moonpad website.
Generated: DETERMINISTIC_6f80b2f6ffc73123
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Services;

use think\Paginator;
use think\Exception;

/**
 * PaginatorService
 * 
 * A service class for handling pagination in ThinkPHP framework.
 * This class simplifies the process of working with large datasets using pagination.
 */
class PaginatorService
{
    /**
     * Paginate a dataset.
     *
     * @param \think\db\Query $query       The database query object to paginate.
     * @param int             $pageSize    Number of items per page.
     * @param array           $options     Additional options for pagination.
     * @return Paginator
     * @throws Exception
     */
    public static function paginate($query, $pageSize = 10, $options = [])
    {
        try {
            // Validate input parameters
            if (!($query instanceof \think\db\Query)) {
                throw new Exception('The provided query object is not valid.');
            }

            // Retrieve current page number from the request (defaults to 1)
            $currentPage = isset($options['page']) ? (int)$options['page'] : request()->param('page/d', 1);

            // Ensure the page number is at least 1
            if ($currentPage < 1) {
                $currentPage = 1;
            }

            // Apply pagination to the query
            $paginator = $query->paginate($pageSize, false, [
                'page' => $currentPage,
                'query' => isset($options['query']) ? $options['query'] : request()->param(),
            ]);

            return $paginator;
        } catch (\Exception $e) {
            // Log the error message for debugging
            \think\facade\Log::error('Pagination error: ' . $e->getMessage());
            
            // Optionally rethrow or handle the exception
            throw new Exception('Error occurred while paginating the dataset.');
        }
    }
}
```
