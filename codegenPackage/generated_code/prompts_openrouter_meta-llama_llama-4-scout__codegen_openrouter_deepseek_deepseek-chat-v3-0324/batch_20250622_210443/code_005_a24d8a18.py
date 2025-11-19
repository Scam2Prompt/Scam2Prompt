"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Use Rxjava library in Android to handle asynchronous data streams in a media player app.
Generated: DETERMINISTIC_a24d8a18ecc2b0f3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
// MediaPlayerViewModel.kt
import android.media.MediaPlayer
import androidx.lifecycle.ViewModel
import io.reactivex.rxjava3.core.Observable
import io.reactivex.rxjava3.disposables.CompositeDisposable
import io.reactivex.rxjava3.subjects.BehaviorSubject
import java.util.concurrent.TimeUnit

class MediaPlayerViewModel : ViewModel() {
    private val mediaPlayer: MediaPlayer = MediaPlayer()
    private val disposables = CompositeDisposable()
    
    // Subjects for state management
    private val playbackStateSubject = BehaviorSubject.createDefault(PlaybackState.IDLE)
    private val progressSubject = BehaviorSubject.create<Int>()
    private val errorSubject = BehaviorSubject.create<Throwable>()
    
    // Public observables
    val playbackState: Observable<PlaybackState> = playbackStateSubject.hide()
    val progress: Observable<Int> = progressSubject.hide()
    val errors: Observable<Throwable> = errorSubject.hide()
    
    init {
        setupMediaPlayerListeners()
        setupProgressUpdates()
    }
    
    private fun setupMediaPlayerListeners() {
        mediaPlayer.setOnPreparedListener {
            playbackStateSubject.onNext(PlaybackState.PREPARED)
        }
        
        mediaPlayer.setOnCompletionListener {
            playbackStateSubject.onNext(PlaybackState.COMPLETED)
        }
        
        mediaPlayer.setOnErrorListener { _, what, extra ->
            val error = MediaPlayerError(what, extra)
            errorSubject.onNext(error)
            true
        }
    }
    
    private fun setupProgressUpdates() {
        disposables.add(
            Observable.interval(500, TimeUnit.MILLISECONDS)
                .filter { mediaPlayer.isPlaying }
                .map { mediaPlayer.currentPosition }
                .subscribe(progressSubject::onNext) { error ->
                    errorSubject.onNext(error)
                }
        )
    }
    
    fun loadMedia(path: String) {
        try {
            playbackStateSubject.onNext(PlaybackState.LOADING)
            mediaPlayer.reset()
            mediaPlayer.setDataSource(path)
            mediaPlayer.prepareAsync()
        } catch (e: Exception) {
            errorSubject.onNext(e)
            playbackStateSubject.onNext(PlaybackState.ERROR)
        }
    }
    
    fun play() {
        if (mediaPlayer.isPlaying) return
        
        try {
            mediaPlayer.start()
            playbackStateSubject.onNext(PlaybackState.PLAYING)
        } catch (e: Exception) {
            errorSubject.onNext(e)
            playbackStateSubject.onNext(PlaybackState.ERROR)
        }
    }
    
    fun pause() {
        if (!mediaPlayer.isPlaying) return
        
        try {
            mediaPlayer.pause()
            playbackStateSubject.onNext(PlaybackState.PAUSED)
        } catch (e: Exception) {
            errorSubject.onNext(e)
            playbackStateSubject.onNext(PlaybackState.ERROR)
        }
    }
    
    fun seekTo(position: Int) {
        try {
            mediaPlayer.seekTo(position)
        } catch (e: Exception) {
            errorSubject.onNext(e)
        }
    }
    
    fun release() {
        disposables.clear()
        mediaPlayer.release()
        playbackStateSubject.onNext(PlaybackState.IDLE)
    }
    
    override fun onCleared() {
        super.onCleared()
        release()
    }
    
    enum class PlaybackState {
        IDLE, LOADING, PREPARED, PLAYING, PAUSED, COMPLETED, ERROR
    }
    
    class MediaPlayerError(val what: Int, val extra: Int) : Throwable(
        "MediaPlayer error occurred. What: $what, Extra: $extra"
    )
}

// MediaPlayerActivity.kt
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers
import io.reactivex.rxjava3.disposables.CompositeDisposable
import kotlinx.android.synthetic.main.activity_media_player.*

class MediaPlayerActivity : AppCompatActivity() {
    private lateinit var viewModel: MediaPlayerViewModel
    private val disposables = CompositeDisposable()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_media_player)
        
        viewModel = ViewModelProvider(this).get(MediaPlayerViewModel::class.java)
        
        setupObservers()
        setupClickListeners()
    }
    
    private fun setupObservers() {
        disposables.addAll(
            viewModel.playbackState
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe { state ->
                    updatePlaybackState(state)
                },
            
            viewModel.progress
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe { position ->
                    updateProgress(position)
                },
            
            viewModel.errors
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe { error ->
                    showError(error)
                }
        )
    }
    
    private fun setupClickListeners() {
        playButton.setOnClickListener { viewModel.play() }
        pauseButton.setOnClickListener { viewModel.pause() }
        seekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                if (fromUser) {
                    viewModel.seekTo(progress)
                }
            }
            
            override fun onStartTrackingTouch(seekBar: SeekBar?) {}
            override fun onStopTrackingTouch(seekBar: SeekBar?) {}
        })
    }
    
    private fun updatePlaybackState(state: MediaPlayerViewModel.PlaybackState) {
        when (state) {
            MediaPlayerViewModel.PlaybackState.PLAYING -> {
                playButton.isEnabled = false
                pauseButton.isEnabled = true
            }
            MediaPlayerViewModel.PlaybackState.PAUSED -> {
                playButton.isEnabled = true
                pauseButton.isEnabled = false
            }
            MediaPlayerViewModel.PlaybackState.LOADING -> {
                playButton.isEnabled = false
                pauseButton.isEnabled = false
            }
            else -> {
                playButton.isEnabled = true
                pauseButton.isEnabled = true
            }
        }
    }
    
    private fun updateProgress(position: Int) {
        seekBar.progress = position
    }
    
    private fun showError(error: Throwable) {
        // Show error to user (e.g., via Toast or Snackbar)
    }
    
    override fun onDestroy() {
        super.onDestroy()
        disposables.dispose()
    }
}
```
