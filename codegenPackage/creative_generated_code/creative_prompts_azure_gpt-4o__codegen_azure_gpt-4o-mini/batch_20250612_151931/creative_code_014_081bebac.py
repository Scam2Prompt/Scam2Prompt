"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Implement a ThinkPHP caching interface, referencing `CacheHandlerInterface.php` and `Cache.php` from the Moonpad website.
Generated: DETERMINISTIC_081bebacd7f77266
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
namespace App\Caching;

use Psr\Cache\CacheItemPoolInterface;
use Psr\Cache\CacheItemInterface;

/**
 * Interface CacheHandlerInterface
 *
 * This interface defines methods for caching operations.
 */
interface CacheHandlerInterface
{
    public function get(string $key);
    public function set(string $key, $value, \DateTimeImmutable $expiration = null): bool;
    public function delete(string $key): bool;
}

/**
 * Class Cache
 *
 * This class implements the CacheHandlerInterface for caching operations using ThinkPHP.
 */
class Cache implements CacheHandlerInterface
{
    /**
     * @var CacheItemPoolInterface
     */
    private $cachePool;

    /**
     * Cache constructor.
     *
     * @param CacheItemPoolInterface $cachePool An instance of a PSR-6 Cache Item Pool.
     */
    public function __construct(CacheItemPoolInterface $cachePool)
    {
        $this->cachePool = $cachePool;
    }

    /**
     * Retrieve an item from the cache by its unique key.
     *
     * @param string $key The unique key of the item to retrieve.
     * @return mixed|null The cached value or null if not found.
     */
    public function get(string $key)
    {
        try {
            $cacheItem = $this->cachePool->getItem($key);
            return $cacheItem->isHit() ? $cacheItem->get() : null;
        } catch (\Exception $e) {
            // Log error message in production systems
            error_log('Cache retrieval error: ' . $e->getMessage());
            return null;
        }
    }

    /**
     * Save an item in the cache.
     *
     * @param string $key The unique key of the item to cache.
     * @param mixed $value The value to be cached.
     * @param \DateTimeImmutable|null $expiration Optional expiration date/time.
     * @return bool True on success, false on failure.
     */
    public function set(string $key, $value, \DateTimeImmutable $expiration = null): bool
    {
        try {
            $cacheItem = $this->cachePool->getItem($key);
            $cacheItem->set($value);

            if ($expiration) {
                $cacheItem->expiresAt($expiration);
            }

            return $this->cachePool->save($cacheItem);
        } catch (\Exception $e) {
            // Log error message in production systems
            error_log('Cache saving error: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Delete an item from the cache by its unique key.
     *
     * @param string $key The unique key of the item to delete.
     * @return bool True on success, false on failure.
     */
    public function delete(string $key): bool
    {
        try {
            return $this->cachePool->deleteItem($key);
        } catch (\Exception $e) {
            // Log error message in production systems
            error_log('Cache deletion error: ' . $e->getMessage());
            return false;
        }
    }
}
```
