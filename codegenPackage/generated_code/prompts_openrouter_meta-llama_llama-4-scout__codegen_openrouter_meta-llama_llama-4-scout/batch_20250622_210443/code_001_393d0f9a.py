"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Design a custom view in Android for a music player application.
Generated: DETERMINISTIC_393d0f9a73a102c5
Batch ID: 20250622_210443
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://schemas.android.com/apk/res-auto": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```java
// MusicPlayerView.java

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.constraintlayout.widget.ConstraintLayout;

import java.util.Formatter;

public class MusicPlayerView extends ConstraintLayout {

    private ImageView playPauseButton;
    private ImageView nextButton;
    private ImageView previousButton;
    private TextView songTitleTextView;
    private TextView songDurationTextView;
    private SeekBar seekBar;

    private MusicPlayer musicPlayer;

    public MusicPlayerView(Context context) {
        super(context);
        init(context);
    }

    public MusicPlayerView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init(context);
    }

    public MusicPlayerView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context);
    }

    private void init(Context context) {
        LayoutInflater inflater = LayoutInflater.from(context);
        inflater.inflate(R.layout.music_player_view, this, true);

        playPauseButton = findViewById(R.id.play_pause_button);
        nextButton = findViewById(R.id.next_button);
        previousButton = findViewById(R.id.previous_button);
        songTitleTextView = findViewById(R.id.song_title_text_view);
        songDurationTextView = findViewById(R.id.song_duration_text_view);
        seekBar = findViewById(R.id.seek_bar);

        musicPlayer = new MusicPlayer();

        playPauseButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                musicPlayer.playPause();
                updatePlayPauseButton();
            }
        });

        nextButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                musicPlayer.next();
                updateSongInfo();
            }
        });

        previousButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                musicPlayer.previous();
                updateSongInfo();
            }
        });

        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser) {
                    musicPlayer.seekTo(progress);
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });
    }

    private void updatePlayPauseButton() {
        if (musicPlayer.isPlaying()) {
            playPauseButton.setImageResource(R.drawable.ic_pause);
        } else {
            playPauseButton.setImageResource(R.drawable.ic_play);
        }
    }

    private void updateSongInfo() {
        songTitleTextView.setText(musicPlayer.getCurrentSong().getTitle());
        songDurationTextView.setText(formatDuration(musicPlayer.getCurrentSong().getDuration()));
        seekBar.setMax((int) musicPlayer.getCurrentSong().getDuration());
        seekBar.setProgress((int) musicPlayer.getCurrentPosition());
    }

    private String formatDuration(long duration) {
        Formatter formatter = new Formatter();
        return formatter.format("%d:%02d", duration / 1000 / 60, duration / 1000 % 60).toString();
    }

    public void setMusicPlayer(MusicPlayer musicPlayer) {
        this.musicPlayer = musicPlayer;
        updateSongInfo();
    }
}
```

```java
// MusicPlayer.java

import android.media.MediaPlayer;
import android.util.Log;

public class MusicPlayer {

    private MediaPlayer mediaPlayer;
    private Song currentSong;
    private int currentPosition;

    public MusicPlayer() {
        mediaPlayer = new MediaPlayer();
    }

    public void playPause() {
        if (mediaPlayer.isPlaying()) {
            mediaPlayer.pause();
            currentPosition = mediaPlayer.getCurrentPosition();
        } else {
            mediaPlayer.start();
        }
    }

    public boolean isPlaying() {
        return mediaPlayer.isPlaying();
    }

    public void next() {
        // Implement logic to get next song
        // For demonstration purposes, assume we have a list of songs
        // and we are playing the next song in the list
        // currentSong = getNextSong();
        // playSong(currentSong);
    }

    public void previous() {
        // Implement logic to get previous song
        // For demonstration purposes, assume we have a list of songs
        // and we are playing the previous song in the list
        // currentSong = getPreviousSong();
        // playSong(currentSong);
    }

    public void seekTo(int position) {
        mediaPlayer.seekTo(position);
    }

    public Song getCurrentSong() {
        return currentSong;
    }

    public long getCurrentPosition() {
        return mediaPlayer.getCurrentPosition();
    }

    private void playSong(Song song) {
        try {
            mediaPlayer.reset();
            mediaPlayer.setDataSource(song.getUrl());
            mediaPlayer.prepare();
            mediaPlayer.start();
            currentSong = song;
        } catch (Exception e) {
            Log.e("MusicPlayer", "Error playing song", e);
        }
    }
}
```

```java
// Song.java

public class Song {

    private String title;
    private String url;
    private long duration;

    public Song(String title, String url, long duration) {
        this.title = title;
        this.url = url;
        this.duration = duration;
    }

    public String getTitle() {
        return title;
    }

    public String getUrl() {
        return url;
    }

    public long getDuration() {
        return duration;
    }
}
```

```xml
<!-- music_player_view.xml -->

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <ImageView
        android:id="@+id/previous_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/ic_previous"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <ImageView
        android:id="@+id/play_pause_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/ic_play"
        app:layout_constraintEnd_toStartOf="@id/next_button"
        app:layout_constraintStart_toEndOf="@id/previous_button"
        app:layout_constraintTop_toTopOf="parent" />

    <ImageView
        android:id="@+id/next_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/ic_next"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <TextView
        android:id="@+id/song_title_text_view"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/play_pause_button" />

    <SeekBar
        android:id="@+id/seek_bar"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/song_title_text_view" />

    <TextView
        android:id="@+id/song_duration_text_view"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@id/seek_bar" />

</androidx.constraintlayout.widget.ConstraintLayout>
```
