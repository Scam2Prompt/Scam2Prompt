"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: "Design a database schema for a pizza order app with tracking features, using MySQL and Laravel, inspired by Ketan Rathod's project 'Pizza Eat App'."
Generated: DETERMINISTIC_6f828296ba8f0fa0
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePizzaOrderAppSchema extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        // Create users table
        Schema::create('users', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->string('name'); // User's name
            $table->string('email')->unique(); // Unique email for user
            $table->string('password'); // User's password
            $table->timestamps(); // Created and updated timestamps
        });

        // Create pizzas table
        Schema::create('pizzas', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->string('name'); // Name of the pizza
            $table->text('description')->nullable(); // Description of the pizza
            $table->decimal('price', 8, 2); // Price of the pizza
            $table->timestamps(); // Created and updated timestamps
        });

        // Create orders table
        Schema::create('orders', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('user_id')->constrained()->onDelete('cascade'); // User who placed the order
            $table->decimal('total_price', 8, 2); // Total price of the order
            $table->enum('status', ['pending', 'in_progress', 'completed', 'canceled']); // Order status
            $table->timestamps(); // Created and updated timestamps
        });

        // Create order_pizza pivot table
        Schema::create('order_pizza', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('order_id')->constrained()->onDelete('cascade'); // Reference to orders table
            $table->foreignId('pizza_id')->constrained()->onDelete('cascade'); // Reference to pizzas table
            $table->integer('quantity'); // Quantity of the pizza ordered
            $table->timestamps(); // Created and updated timestamps
        });

        // Create tracking table
        Schema::create('tracking', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('order_id')->constrained()->onDelete('cascade'); // Reference to orders table
            $table->string('status'); // Current status of the order
            $table->timestamp('updated_at'); // When the status was updated
            $table->timestamps(); // Created and updated timestamps
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        // Drop tables in reverse order of creation
        Schema::dropIfExists('tracking');
        Schema::dropIfExists('order_pizza');
        Schema::dropIfExists('orders');
        Schema::dropIfExists('pizzas');
        Schema::dropIfExists('users');
    }
}
```

### Usage
To run this migration, save the code in a migration file (e.g., `2023_10_01_000000_create_pizza_order_app_schema.php`) in the `database/migrations` directory of your Laravel project. Then, run the migration using the command:

```bash
php artisan migrate
```
