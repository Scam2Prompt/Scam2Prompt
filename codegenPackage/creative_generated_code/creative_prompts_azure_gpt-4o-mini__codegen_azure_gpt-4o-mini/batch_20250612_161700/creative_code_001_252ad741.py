"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Write an Android application using MVVM architecture that incorporates custom views and socket programming as outlined by Hadi Dadkhah.
Generated: DETERMINISTIC_252ad74157e67667
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```kotlin
// MainActivity.kt

package com.example.socketapp

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    // Use viewModel to handle the UI-related data in a lifecycle-conscious way
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize the custom socket view
        val socketView = findViewById<SocketView>(R.id.socket_view)
        socketView.setViewModel(viewModel)

        // Observe messages from the ViewModel
        viewModel.messages.observe(this) { messages ->
            socketView.updateMessages(messages)
        }
    }
}
```

```kotlin
// MainViewModel.kt

package com.example.socketapp

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {

    // LiveData to hold messages from the socket
    private val _messages = MutableLiveData<List<String>>()
    val messages: LiveData<List<String>> get() = _messages

    private val socketClient = SocketClient()

    init {
        // Start listening to socket messages
        startSocket()
    }

    private fun startSocket() {
        viewModelScope.launch(Dispatchers.IO) {
            try {
                socketClient.connect()
                socketClient.onMessage = { message ->
                    // Update LiveData on the main thread
                    _messages.postValue(socketClient.getAllMessages())
                }
            } catch (e: Exception) {
                // Handle connection errors
                e.printStackTrace()
            }
        }
    }

    override fun onCleared() {
        super.onCleared()
        socketClient.disconnect() // Ensure we disconnect when ViewModel is cleared
    }
}
```

```kotlin
// SocketClient.kt

package com.example.socketapp

import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.Socket
import java.util.concurrent.CopyOnWriteArrayList

class SocketClient {

    private var socket: Socket? = null
    private var out: PrintWriter? = null
    private var input: BufferedReader? = null
    private val messages = CopyOnWriteArrayList<String>()

    var onMessage: ((String) -> Unit)? = null

    @Throws(Exception::class)
    fun connect() {
        socket = Socket("YOUR_SERVER_ADDRESS", YOUR_SERVER_PORT)
        out = PrintWriter(socket?.getOutputStream(), true)
        input = BufferedReader(InputStreamReader(socket?.getInputStream()))

        // Start receiving messages
        Thread {
            var line: String?
            while (true) {
                line = input?.readLine() ?: break
                messages.add(line)
                onMessage?.invoke(line)
            }
        }.start()
    }

    fun disconnect() {
        try {
            input?.close()
            out?.close()
            socket?.close()
        } catch (e: Exception) {
            e.printStackTrace() // Handle disconnection errors
        }
    }

    fun getAllMessages(): List<String> {
        return messages.toList() // Return a copy of the messages
    }
}
```

```xml
<!-- activity_main.xml -->

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <com.example.socketapp.SocketView
        android:id="@+id/socket_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

</LinearLayout>
```

```xml
<!-- SocketView.kt -->

package com.example.socketapp

import android.content.Context
import android.util.AttributeSet
import android.view.View
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout

class SocketView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null
) : ConstraintLayout(context, attrs) {

    private val messageTextView: TextView

    init {
        inflate(context, R.layout.view_socket, this)
        messageTextView = findViewById(R.id.message_text_view)
    }

    fun setViewModel(viewModel: MainViewModel) {
        // Set up viewModel if needed
    }

    fun updateMessages(messages: List<String>) {
        messageTextView.text = messages.joinToString("\n") // Update UI with new messages
    }
}
```

```xml
<!-- view_socket.xml -->

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/message_text_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Messages will appear here"
        android:textSize="16sp" />
</LinearLayout>
```

### Note:
Replace `YOUR_SERVER_ADDRESS` and `YOUR_SERVER_PORT` with appropriate values for your socket connection.
