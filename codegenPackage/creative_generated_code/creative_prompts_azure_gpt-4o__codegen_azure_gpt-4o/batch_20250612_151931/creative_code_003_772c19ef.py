"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Implement a custom ThinkPHP model that extends `BaseModel.php` and interacts with the `website` table, as described on the Moonpad website.
Generated: DETERMINISTIC_772c19efbce7008d
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

// Custom model for interacting with the `website` table in ThinkPHP
namespace app\common\model;

use app\common\model\BaseModel;
use think\Exception;

class Website extends BaseModel
{
    // Specify the corresponding table name
    protected $table = 'website';

    // Enable auto-write timestamp fields (created_at, updated_at)
    protected $autoWriteTimestamp = true;

    /**
     * Retrieve a website record by its ID.
     *
     * @param int $id The ID of the website record.
     * @return array|null The website record as an associative array or null if not found.
     */
    public function getWebsiteById($id)
    {
        try {
            // Validate input
            if (!is_int($id) || $id <= 0) {
                throw new Exception('Invalid ID parameter.');
            }

            // Fetch the record
            $website = $this->where('id', $id)->find();
            return $website ? $website->toArray() : null;
        } catch (Exception $e) {
            // Log error message for further debugging
            error_log('Error in getWebsiteById: ' . $e->getMessage());
            return null;
        }
    }

    /**
     * Create a new website record.
     *
     * @param array $data The data to insert into the `website` table.
     * @return bool|int The ID of the newly created record or false on failure.
     */
    public function createWebsite(array $data)
    {
        try {
            // Validate input data
            if (empty($data) || !is_array($data)) {
                throw new Exception('Invalid input data.');
            }

            // Insert new record and return its ID
            $website = $this->create($data);
            return $website ? $website->id : false;
        } catch (Exception $e) {
            // Log error message
            error_log('Error in createWebsite: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Update an existing website record by its ID.
     *
     * @param int $id The ID of the record to update.
     * @param array $data The data to update in the `website` table.
     * @return bool True if the update was successful, false otherwise.
     */
    public function updateWebsite($id, array $data)
    {
        try {
            // Validate input
            if (!is_int($id) || $id <= 0 || empty($data)) {
                throw new Exception('Invalid parameters.');
            }

            // Perform the update
            $result = $this->where('id', $id)->update($data);
            return $result !== false;
        } catch (Exception $e) {
            // Log error message
            error_log('Error in updateWebsite: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Delete a website record by its ID.
     *
     * @param int $id The ID of the record to delete.
     * @return bool True if the deletion was successful, false otherwise.
     */
    public function deleteWebsite($id)
    {
        try {
            // Validate input
            if (!is_int($id) || $id <= 0) {
                throw new Exception('Invalid ID parameter.');
            }

            // Perform the deletion
            $result = $this->where('id', $id)->delete();
            return $result !== false;
        } catch (Exception $e) {
            // Log error message
            error_log('Error in deleteWebsite: ' . $e->getMessage());
            return false;
        }
    }
}
```
