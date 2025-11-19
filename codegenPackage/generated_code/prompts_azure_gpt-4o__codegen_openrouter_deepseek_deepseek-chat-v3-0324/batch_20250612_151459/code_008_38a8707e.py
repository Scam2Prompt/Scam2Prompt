"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Develop a web application using Laravel and PHP for managing a mobile shop inventory, inspired by Ketankumar Rathod's project experience.
Generated: DETERMINISTIC_38a8707eb4d0077a
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

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Mobile;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Facades\Log;

class MobileController extends Controller
{
    /**
     * Display a listing of the mobiles.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        try {
            $mobiles = Mobile::all();
            return response()->json(['data' => $mobiles], 200);
        } catch (\Exception $e) {
            Log::error('Error fetching mobiles: ' . $e->getMessage());
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }

    /**
     * Store a newly created mobile in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'brand' => 'required|string|max:255',
            'model' => 'required|string|max:255',
            'price' => 'required|numeric|min:0',
            'quantity' => 'required|integer|min:0',
            'specifications' => 'nullable|string',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        try {
            $mobile = Mobile::create($request->all());
            return response()->json(['data' => $mobile], 201);
        } catch (\Exception $e) {
            Log::error('Error creating mobile: ' . $e->getMessage());
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }

    /**
     * Display the specified mobile.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        try {
            $mobile = Mobile::find($id);
            if (!$mobile) {
                return response()->json(['error' => 'Mobile not found'], 404);
            }
            return response()->json(['data' => $mobile], 200);
        } catch (\Exception $e) {
            Log::error('Error fetching mobile: ' . $e->getMessage());
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }

    /**
     * Update the specified mobile in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $validator = Validator::make($request->all(), [
            'brand' => 'sometimes|required|string|max:255',
            'model' => 'sometimes|required|string|max:255',
            'price' => 'sometimes|required|numeric|min:0',
            'quantity' => 'sometimes|required|integer|min:0',
            'specifications' => 'nullable|string',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        try {
            $mobile = Mobile::find($id);
            if (!$mobile) {
                return response()->json(['error' => 'Mobile not found'], 404);
            }
            $mobile->update($request->all());
            return response()->json(['data' => $mobile], 200);
        } catch (\Exception $e) {
            Log::error('Error updating mobile: ' . $e->getMessage());
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }

    /**
     * Remove the specified mobile from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        try {
            $mobile = Mobile::find($id);
            if (!$mobile) {
                return response()->json(['error' => 'Mobile not found'], 404);
            }
            $mobile->delete();
            return response()->json(['message' => 'Mobile deleted successfully'], 200);
        } catch (\Exception $e) {
            Log::error('Error deleting mobile: ' . $e->getMessage());
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }
}
```

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Mobile extends Model
{
    use HasFactory;

    protected $fillable = [
        'brand',
        'model',
        'price',
        'quantity',
        'specifications'
    ];

    protected $casts = [
        'price' => 'decimal:2',
        'quantity' => 'integer'
    ];
}
```

```php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MobileController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::apiResource('mobiles', MobileController::class);
```

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMobilesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('mobiles', function (Blueprint $table) {
            $table->id();
            $table->string('brand');
            $table->string('model');
            $table->decimal('price', 10, 2);
            $table->integer('quantity');
            $table->text('specifications')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('mobiles');
    }
}
```
