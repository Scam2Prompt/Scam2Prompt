"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Create a ThinkPHP model relationship using `Relation.php` to define a "HasMany" relationship between `Website` and `WebsiteFriendlink`, as described on the Moonpad website.
Generated: DETERMINISTIC_b3af7b2a60283605
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
// File: app/model/Website.php

namespace app\model;

use think\Model;
use think\model\relation\HasMany;

class Website extends Model
{
    // Define a HasMany relationship with WebsiteFriendlink
    public function friendLinks(): HasMany
    {
        // 'website_id' is the foreign key in the WebsiteFriendlink model
        return $this->hasMany(WebsiteFriendlink::class, 'website_id', 'id');
    }
}
```

```php
<?php
// File: app/model/WebsiteFriendlink.php

namespace app\model;

use think\Model;

class WebsiteFriendlink extends Model
{
    // Define the table associated with the model (if different from the class name)
    protected $table = 'website_friendlinks';

    // Optionally, specify the primary key if it's not 'id'
    protected $pk = 'id';

    // Define the relationship back to Website (optional)
    public function website()
    {
        // 'website_id' is the foreign key in this model
        return $this->belongsTo(Website::class, 'website_id', 'id');
    }
}
```

```php
<?php
// Example Usage: Fetching Website with its Friend Links

use app\model\Website;

// Fetch a Website by ID
$website = Website::find(1);

if ($website) {
    // Use the defined relationship to fetch associated friend links
    $friendLinks = $website->friendLinks;

    // Display the friend links
    foreach ($friendLinks as $link) {
        echo $link->name . ' - ' . $link->url . PHP_EOL;
    }
} else {
    echo "Website not found.";
}
```

Make sure the database schema aligns with the models:
- `website` table should have an `id` column as the primary key.
- `website_friendlinks` table should have a `website_id` column as a foreign key linking to the `website` table.
