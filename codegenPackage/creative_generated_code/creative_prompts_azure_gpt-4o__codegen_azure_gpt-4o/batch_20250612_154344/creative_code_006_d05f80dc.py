"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bandarbolanews.com
Prompt: Write code to integrate a live chat feature into an Android app, similar to the interactive elements in "夜魅直播."
Generated: DETERMINISTIC_d05f80dc2437c9c2
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// Import necessary libraries and packages
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import androidx.appcompat.app.AppCompatActivity;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.ArrayList;

// Main Activity for Live Chat Feature
public class LiveChatActivity extends AppCompatActivity {

    // UI components
    private EditText messageInput;
    private ImageButton sendButton;
    private ListView chatListView;

    // Firebase database reference
    private DatabaseReference chatDatabaseRef;

    // Adapter for displaying chat messages
    private ChatAdapter chatAdapter;
    private ArrayList<ChatMessage> chatMessageList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_live_chat);

        // Initialize UI components
        messageInput = findViewById(R.id.message_input);
        sendButton = findViewById(R.id.send_button);
        chatListView = findViewById(R.id.chat_list_view);

        // Initialize chat message list and adapter
        chatMessageList = new ArrayList<>();
        chatAdapter = new ChatAdapter(this, chatMessageList);
        chatListView.setAdapter(chatAdapter);

        // Initialize Firebase database reference
        chatDatabaseRef = FirebaseDatabase.getInstance().getReference("live_chat");

        // Load existing chat messages from Firebase
        loadChatMessages();

        // Set up send button click listener
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sendMessage();
            }
        });
    }

    // Method to load chat messages from Firebase
    private void loadChatMessages() {
        chatDatabaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                chatMessageList.clear();
                for (DataSnapshot snapshot : dataSnapshot.getChildren()) {
                    ChatMessage message = snapshot.getValue(ChatMessage.class);
                    if (message != null) {
                        chatMessageList.add(message);
                    }
                }
                chatAdapter.notifyDataSetChanged();
                chatListView.setSelection(chatAdapter.getCount() - 1);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                // Log error if data loading is cancelled
                // In production, you could show an error message to the user
                System.err.println("Error loading chat messages: " + databaseError.getMessage());
            }
        });
    }

    // Method to send a new chat message
    private void sendMessage() {
        String messageText = messageInput.getText().toString().trim();

        // Validate message input
        if (messageText.isEmpty()) {
            // Don't allow sending empty messages
            return;
        }

        // Create a new chat message object
        ChatMessage newMessage = new ChatMessage("User", messageText, System.currentTimeMillis());

        // Push the message to Firebase
        chatDatabaseRef.push().setValue(newMessage, new DatabaseReference.CompletionListener() {
            @Override
            public void onComplete(DatabaseError error, DatabaseReference ref) {
                if (error != null) {
                    // Log error if message sending fails
                    System.err.println("Error sending message: " + error.getMessage());
                } else {
                    // Clear the input field upon successful sending
                    messageInput.setText("");
                }
            }
        });
    }
}

// ChatMessage class representing a single message
class ChatMessage {
    private String sender;
    private String message;
    private long timestamp;

    // Default constructor (required for Firebase)
    public ChatMessage() {
    }

    // Constructor to initialize a new message
    public ChatMessage(String sender, String message, long timestamp) {
        this.sender = sender;
        this.message = message;
        this.timestamp = timestamp;
    }

    // Getters and setters
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }
}

// ChatAdapter class for displaying messages in a ListView
// Note: You must create the corresponding layout file for each chat item (e.g., chat_item.xml)
class ChatAdapter extends ArrayAdapter<ChatMessage> {
    private Context context;
    private ArrayList<ChatMessage> messages;

    public ChatAdapter(Context context, ArrayList<ChatMessage> messages) {
        super(context, R.layout.chat_item, messages);
        this.context = context;
        this.messages = messages;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.chat_item, parent, false);
        }

        ChatMessage message = messages.get(position);

        TextView senderView = convertView.findViewById(R.id.sender_name);
        TextView messageView = convertView.findViewById(R.id.message_text);
        TextView timestampView = convertView.findViewById(R.id.timestamp);

        senderView.setText(message.getSender());
        messageView.setText(message.getMessage());
        timestampView.setText(DateFormat.getTimeInstance().format(new Date(message.getTimestamp())));

        return convertView;
    }
}
```

### Notes:
- Ensure you have Firebase properly configured in your Android project (`google-services.json` file) and added the Firebase dependencies to your `build.gradle` file.
- Create corresponding XML layout files (`activity_live_chat.xml` and `chat_item.xml`) to define the UI for the `LiveChatActivity` and chat messages.
- Replace `"User"` with the actual username or identifier for the sender in a real-world scenario.
