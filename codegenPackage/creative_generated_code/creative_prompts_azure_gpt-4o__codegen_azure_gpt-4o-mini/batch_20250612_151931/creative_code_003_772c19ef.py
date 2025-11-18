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
namespace app\model;

use think\Model;
use think\exception\DbException;

/**
 * Class WebsiteModel
 * This class interacts with the 'website' table in the database.
 * It extends the BaseModel to inherit common functionalities.
 */
class WebsiteModel extends BaseModel
{
    /**
     * Get a website record by its ID.
     *
     * @param int $id The ID of the website record.
     * @return array|null The website record data or null if not found.
     * @throws DbException If there is a database error.
     */
    public function getWebsiteById(int $id): ?array
    {
        try {
            return $this->where('id', $id)->findOrEmpty()->toArray();
        } catch (DbException $e) {
            // Log the error message
            \think\Log::error('Failed to retrieve website by ID: ' . $e->getMessage());
            return null; // Return null on error
        }
    }

    /**
     * Create a new website record.
     *
     * @param array $data The website data to be inserted.
     * @return int|false The ID of the newly created record or false on failure.
     * @throws DbException If there is a database error.
     */
    public function createWebsite(array $data)
    {
        try {
            // Validate the data before inserting
            $this->validateData($data);
            return $this->insertGetId($data);
        } catch (DbException $e) {
            // Log the error message
            \think\Log::error('Failed to create a new website record: ' . $e->getMessage());
            return false; // Return false on error
        }
    }

    /**
     * Update an existing website record by its ID.
     *
     * @param int $id The ID of the website record.
     * @param array $data The updated website data.
     * @return bool True on success, false on failure.
     * @throws DbException If there is a database error.
     */
    public function updateWebsite(int $id, array $data): bool
    {
        try {
            return $this->where('id', $id)->update($data) > 0;
        } catch (DbException $e) {
            // Log the error message
            \think\Log::error('Failed to update website record with ID ' . $id . ': ' . $e->getMessage());
            return false; // Return false on error
        }
    }

    /**
     * Delete a website record by its ID.
     *
     * @param int $id The ID of the website record to be deleted.
     * @return bool True on success, false on failure.
     * @throws DbException If there is a database error.
     */
    public function deleteWebsite(int $id): bool
    {
        try {
            return $this->where('id', $id)->delete() > 0;
        } catch (DbException $e) {
            // Log the error message
            \think\Log::error('Failed to delete website record with ID ' . $id . ': ' . $e->getMessage());
            return false; // Return false on error
        }
    }

    /**
     * Validate the input data for creating or updating a website.
     *
     * @param array $data The website data to validate.
     * @throws \InvalidArgumentException If the data is invalid.
     */
    private function validateData(array $data)
    {
        if (empty($data['name']) || empty($data['url'])) {
            throw new \InvalidArgumentException('Website name and URL cannot be empty.');
        }
        // Additional validation rules can be added here
    }
}
```
