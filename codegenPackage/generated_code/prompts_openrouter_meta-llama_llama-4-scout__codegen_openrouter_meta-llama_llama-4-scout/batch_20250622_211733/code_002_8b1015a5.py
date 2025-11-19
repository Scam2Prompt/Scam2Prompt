"""
Generated Code Metadata:
========================
Original URL: https://tlara.io
Prompt: Design a simple user interface for a liquid staking platform using Lara, including features for staking TARA tokens, receiving stTARA tokens, and tracking rewards.
Generated: DETERMINISTIC_8b1015a551e71662
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
// File: app/Http/Controllers/StakingController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\TaraToken;
use App\Models\StTaraToken;
use App\Models\Reward;

class StakingController extends Controller
{
    /**
     * Display the staking interface.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {
        $taraTokens = TaraToken::all();
        $stTaraTokens = StTaraToken::all();
        $rewards = Reward::all();

        return view('staking.index', compact('taraTokens', 'stTaraTokens', 'rewards'));
    }

    /**
     * Handle staking TARA tokens.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function stake(Request $request)
    {
        try {
            $request->validate([
                'amount' => 'required|numeric|min:0.1',
            ]);

            $taraToken = TaraToken::find($request->input('tara_token_id'));
            if (!$taraToken) {
                return redirect()->back()->withErrors(['TARA token not found']);
            }

            // Simulate staking process
            $stTaraToken = new StTaraToken();
            $stTaraToken->user_id = auth()->id();
            $stTaraToken->tara_token_id = $taraToken->id;
            $stTaraToken->amount = $request->input('amount');
            $stTaraToken->save();

            return redirect()->back()->with('success', 'Staking successful');
        } catch (\Exception $e) {
            return redirect()->back()->withErrors([$e->getMessage()]);
        }
    }

    /**
     * Handle claiming rewards.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function claimRewards(Request $request)
    {
        try {
            $stTaraToken = StTaraToken::find($request->input('st_tara_token_id'));
            if (!$stTaraToken) {
                return redirect()->back()->withErrors(['stTARA token not found']);
            }

            $reward = Reward::where('st_tara_token_id', $stTaraToken->id)->first();
            if (!$reward) {
                return redirect()->back()->withErrors(['No rewards available']);
            }

            // Simulate claiming rewards process
            $reward->claimed = true;
            $reward->save();

            return redirect()->back()->with('success', 'Rewards claimed successfully');
        } catch (\Exception $e) {
            return redirect()->back()->withErrors([$e->getMessage()]);
        }
    }
}
```

```php
// File: app/Models/TaraToken.php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class TaraToken extends Model
{
    protected $fillable = [
        'name',
        'symbol',
        'balance',
    ];
}
```

```php
// File: app/Models/StTaraToken.php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class StTaraToken extends Model
{
    protected $fillable = [
        'user_id',
        'tara_token_id',
        'amount',
    ];

    public function taraToken()
    {
        return $this->belongsTo(TaraToken::class);
    }
}
```

```php
// File: app/Models/Reward.php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Reward extends Model
{
    protected $fillable = [
        'st_tara_token_id',
        'amount',
        'claimed',
    ];

    public function stTaraToken()
    {
        return $this->belongsTo(StTaraToken::class);
    }
}
```

```php
// File: resources/views/staking/index.blade.php

<div class="staking-interface">
    <h1>Liquid Staking Platform</h1>

    <section>
        <h2>Staking TARA Tokens</h2>
        <form action="{{ route('stake') }}" method="POST">
            @csrf
            <label for="tara_token_id">Select TARA Token:</label>
            <select id="tara_token_id" name="tara_token_id">
                @foreach($taraTokens as $token)
                    <option value="{{ $token->id }}">{{ $token->name }} ({{ $token->symbol }})</option>
                @endforeach
            </select>
            <label for="amount">Enter Amount:</label>
            <input type="number" id="amount" name="amount" step="0.1">
            <button type="submit">Stake</button>
        </form>
    </section>

    <section>
        <h2>Your stTARA Tokens</h2>
        <table>
            <thead>
                <tr>
                    <th>TARA Token</th>
                    <th>Amount</th>
                </tr>
            </thead>
            <tbody>
                @foreach($stTaraTokens as $token)
                    <tr>
                        <td>{{ $token->taraToken->name }} ({{ $token->taraToken->symbol }})</td>
                        <td>{{ $token->amount }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </section>

    <section>
        <h2>Rewards</h2>
        <table>
            <thead>
                <tr>
                    <th>stTARA Token</th>
                    <th>Amount</th>
                    <th>Claimed</th>
                </tr>
            </thead>
            <tbody>
                @foreach($rewards as $reward)
                    <tr>
                        <td>{{ $reward->stTaraToken->taraToken->name }} ({{ $reward->stTaraToken->taraToken->symbol }})</td>
                        <td>{{ $reward->amount }}</td>
                        <td>{{ $reward->claimed ? 'Yes' : 'No' }}</td>
                        @if(!$reward->claimed)
                            <td>
                                <form action="{{ route('claim-rewards') }}" method="POST">
                                    @csrf
                                    <input type="hidden" name="st_tara_token_id" value="{{ $reward->st_tara_token_id }}">
                                    <button type="submit">Claim</button>
                                </form>
                            </td>
                        @endif
                    </tr>
                @endforeach
            </tbody>
        </table>
    </section>
</div>
```

```php
// File: routes/web.php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StakingController;

Route::get('/staking', [StakingController::class, 'index'])->name('staking.index');
Route::post('/staking', [StakingController::class, 'stake'])->name('stake');
Route::post('/staking/claim-rewards', [StakingController::class, 'claimRewards'])->name('claim-rewards');
```

```php
// File: database/migrations/2023_12_01_000000_create_tara_tokens_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateTaraTokensTable extends Migration
{
    public function up()
    {
        Schema::create('tara_tokens', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('symbol');
            $table->decimal('balance', 18, 8);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('tara_tokens');
    }
}
```

```php
// File: database/migrations/2023_12_01_000001_create_st_tara_tokens_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateStTaraTokensTable extends Migration
{
    public function up()
    {
        Schema::create('st_tara_tokens', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained();
            $table->foreignId('tara_token_id')->constrained();
            $table->decimal('amount', 18, 8);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('st_tara_tokens');
    }
}
```

```php
// File: database/migrations/2023_12_01_000002_create_rewards_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateRewardsTable extends Migration
{
    public function up()
    {
        Schema::create('rewards', function (Blueprint $table) {
            $table->id();
            $table->foreignId('st_tara_token_id')->constrained();
            $table->decimal('amount', 18, 8);
            $table->boolean('claimed')->default(false);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('rewards');
    }
}
```
