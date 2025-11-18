"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Write a PHP script using Laravel to create an API endpoint for fetching products that are part of a promotion or sale, including discounted prices and original prices.
Generated: DETERMINISTIC_35f10a707037f3a1
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Product;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class PromotionController extends Controller
{
    /**
     * Fetch products that are part of a promotion or sale.
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function getPromotionalProducts(Request $request): JsonResponse
    {
        // Validate the request parameters
        $validator = Validator::make($request->all(), [
            'limit' => 'integer|min:1|max:100',
            'page' => 'integer|min:1',
        ]);

        // Return validation errors if any
        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'errors' => $validator->errors(),
            ], 422);
        }

        // Set pagination parameters
        $limit = $request->input('limit', 10); // default limit is 10
        $page = $request->input('page', 1); // default page is 1

        try {
            // Fetch products on promotion
            $products = Product::where('is_on_sale', true)
                ->select('id', 'name', 'original_price', 'discounted_price')
                ->paginate($limit, ['*'], 'page', $page);

            // Return successful response with products data
            return response()->json([
                'success' => true,
                'data' => $products,
            ]);
        } catch (\Exception $e) {
            // Handle errors and return a response
            return response()->json([
                'success' => false,
                'message' => 'Failed to fetch promotional products.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }
}
```

### Route Configuration
To make the API endpoint accessible, add the following route in `routes/api.php`:

```php
use App\Http\Controllers\API\PromotionController;

Route::get('/promotional-products', [PromotionController::class, 'getPromotionalProducts']);
```

### Model Example
Ensure your `Product` model is set up properly with the necessary attributes:

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'original_price',
        'discounted_price',
        'is_on_sale',
    ];
}
```

### Migration Example
Example migration file for creating the `products` table:

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateProductsTable extends Migration
{
    public function up()
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->decimal('original_price', 10, 2);
            $table->decimal('discounted_price', 10, 2);
            $table->boolean('is_on_sale')->default(false);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('products');
    }
}
```

Ensure that you run the migration using `php artisan migrate` to create the `products` table in your database.
