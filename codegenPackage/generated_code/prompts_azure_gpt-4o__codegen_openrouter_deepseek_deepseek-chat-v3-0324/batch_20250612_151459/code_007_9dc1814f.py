"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Provide a step-by-step guide for setting up a Laravel project with MySQL integration, referencing the technical skills listed in Ketankumar Rathod's portfolio.
Generated: DETERMINISTIC_9dc1814f82e70870
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Step 1: Install Laravel via Composer
// Run in terminal: composer create-project laravel/laravel projectName

// Step 2: Configure .env file for MySQL
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

// Step 3: Create a Model with Migration
// Run in terminal: php artisan make:model Product -m

// Migration file (database/migrations/xxxx_create_products_table.php)
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('description');
            $table->decimal('price', 8, 2);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('products');
    }
};

// Step 4: Run Migrations
// Run in terminal: php artisan migrate

// Step 5: Create Controller
// Run in terminal: php artisan make:controller ProductController --resource

// ProductController.php
<?php

namespace App\Http\Controllers;

use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    public function index()
    {
        return Product::all();
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'description' => 'required|string',
            'price' => 'required|numeric'
        ]);

        return Product::create($validated);
    }

    public function show(Product $product)
    {
        return $product;
    }

    public function update(Request $request, Product $product)
    {
        $validated = $request->validate([
            'name' => 'sometimes|string|max:255',
            'description' => 'sometimes|string',
            'price' => 'sometimes|numeric'
        ]);

        $product->update($validated);
        return $product;
    }

    public function destroy(Product $product)
    {
        $product->delete();
        return response(null, 204);
    }
}

// Step 6: Define API Routes (routes/api.php)
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductController;

Route::apiResource('products', ProductController::class);

// Step 7: Test the API
// Run in terminal: php artisan serve
// Test endpoints with Postman or cURL:
// GET /api/products
// POST /api/products
// GET /api/products/{id}
// PUT /api/products/{id}
// DELETE /api/products/{id}

// Step 8: Optional - Add Authentication
// Run in terminal: composer require laravel/sanctum
// Run in terminal: php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
// Run in terminal: php artisan migrate
```
