"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Generate a Laravel script that uses the Laravel Dusk library to automate browser testing for a login form.
Generated: DETERMINISTIC_b9dfd20693ebbf7b
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LoginFormTest.php**
```php
// File: tests/Browser/LoginFormTest.php

namespace Tests\Browser;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Tests\DuskTestCase;
use Laravel\Dusk\Browser;

class LoginFormTest extends DuskTestCase
{
    use DatabaseMigrations;

    /**
     * Test successful login.
     *
     * @return void
     * @throws \Exception
     */
    public function testSuccessfulLogin()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->type('email', 'test@example.com')
                ->type('password', 'password123')
                ->press('Login')
                ->assertPathIs('/home')
                ->assertSee('Logout');
        });
    }

    /**
     * Test failed login with invalid credentials.
     *
     * @return void
     * @throws \Exception
     */
    public function testFailedLogin()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->type('email', 'test@example.com')
                ->type('password', 'wrongpassword')
                ->press('Login')
                ->assertPathIs('/login')
                ->assertSee('Invalid credentials');
        });
    }

    /**
     * Test login form validation.
     *
     * @return void
     * @throws \Exception
     */
    public function testLoginFormValidation()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->press('Login')
                ->assertSee('The email field is required')
                ->assertSee('The password field is required');
        });
    }

    /**
     * Test login form with empty email field.
     *
     * @return void
     * @throws \Exception
     */
    public function testLoginFormEmptyEmail()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->type('password', 'password123')
                ->press('Login')
                ->assertSee('The email field is required');
        });
    }

    /**
     * Test login form with empty password field.
     *
     * @return void
     * @throws \Exception
     */
    public function testLoginFormEmptyPassword()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->type('email', 'test@example.com')
                ->press('Login')
                ->assertSee('The password field is required');
        });
    }
}
```

**User Model and Migration**
```php
// File: app/Models/User.php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Auth\Authenticatable;

class User extends Model
{
    use Authenticatable;

    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    protected $hidden = [
        'password',
    ];
}
```

```php
// File: database/migrations/2023_12_01_000000_create_users_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateUsersTable extends Migration
{
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('password');
            $table->timestamps();
        });

        // Insert test user
        \App\Models\User::create([
            'name' => 'Test User',
            'email' => 'test@example.com',
            'password' => bcrypt('password123'),
        ]);
    }

    public function down()
    {
        Schema::dropIfExists('users');
    }
}
```

**Login Controller and Route**
```php
// File: app/Http/Controllers/Auth/LoginController.php

namespace App\Http\Controllers\Auth;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function showLoginForm()
    {
        return view('auth.login');
    }

    public function login(Request $request)
    {
        $credentials = $request->validate([
            'email' => ['required', 'email'],
            'password' => ['required'],
        ]);

        if (Auth::attempt($credentials)) {
            return redirect('/home');
        }

        return back()->withErrors([
            'Invalid credentials',
        ]);
    }
}
```

```php
// File: routes/web.php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Auth\LoginController;

Route::get('/login', [LoginController::class, 'showLoginForm'])->name('login');
Route::post('/login', [LoginController::class, 'login']);
Route::get('/home', function () {
    return view('home');
})->middleware('auth');
```

**Login View**
```php
<!-- File: resources/views/auth/login.blade.php -->

<x-app-layout>
    <form method="POST" action="/login">
        @csrf
        <div>
            <label for="email">Email</label>
            <input type="email" id="email" name="email" :value="old('email')">
            @error('email')
                <div>{{ $message }}</div>
            @enderror
        </div>

        <div>
            <label for="password">Password</label>
            <input type="password" id="password" name="password">
            @error('password')
                <div>{{ $message }}</div>
            @enderror
        </div>

        <button type="submit">Login</button>
    </form>
</x-app-layout>
```
