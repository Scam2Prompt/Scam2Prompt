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

use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\DB;
use InvalidArgumentException;

class PaginatorService
{
    /**
     * Retrieves a paginated set of results from a database table.
     *
     * @param string $table The name of the table to paginate.
     * @param array $columns The columns to select.
     * @param int $currentPage The current page number.
     * @param int $perPage The number of items per page.
     * @param array $filters Optional filters to apply to the query.
     * @return LengthAwarePaginator A paginated collection of results.
     * @throws InvalidArgumentException If the table name is invalid.
     */
    public function paginate(string $table, array $columns = ['*'], int $currentPage = 1, int $perPage = 15, array $filters = []): LengthAwarePaginator
    {
        // Validate table name
        if (empty($table) || !preg_match('/^[a-zA-Z_]+$/', $table)) {
            throw new InvalidArgumentException("Invalid table name provided.");
        }

        // Build the query with filters
        $query = DB::table($table);
        
        foreach ($filters as $key => $value) {
            $query->where($key, $value);
        }

        // Get total number of items
        $totalItems = $query->count();

        // Fetch the items for the current page
        $items = $query->select($columns)
                       ->forPage($currentPage, $perPage)
                       ->get();

        // Create and return the LengthAwarePaginator instance
        return new LengthAwarePaginator(
            $items,
            $totalItems,
            $perPage,
            $currentPage,
            ['path' => request()->url(), 'query' => request()->query()]
        );
    }
}
```
