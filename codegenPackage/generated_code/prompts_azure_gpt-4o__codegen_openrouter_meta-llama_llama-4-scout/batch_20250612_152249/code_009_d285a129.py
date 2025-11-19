"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Generate code for a mobile app that provides access to SKI Foundation's "Training & Coaching Bisnis" materials, with offline access and progress tracking features.
Generated: DETERMINISTIC_d285a1294061c0db
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Java for Android. I'll use SQLite for local database storage, Room persistence library for database interactions, and JSON for storing data.

**Model Classes**

```java
// Training.java
@Entity(tableName = "trainings")
public class Training {
    @PrimaryKey
    private int id;
    private String title;
    private String description;
    private String videoUrl;

    // Getters and setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getVideoUrl() { return videoUrl; }
    public void setVideoUrl(String videoUrl) { this.videoUrl = videoUrl; }
}

// Progress.java
@Entity(tableName = "progress")
public class Progress {
    @PrimaryKey
    private int id;
    private int trainingId;
    private int completed;

    // Getters and setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public int getTrainingId() { return trainingId; }
    public void setTrainingId(int trainingId) { this.trainingId = trainingId; }
    public int getCompleted() { return completed; }
    public void setCompleted(int completed) { this.completed = completed; }
}
```

**Room Database**

```java
// AppDatabase.java
@Database(entities = {Training.class, Progress.class}, version = 1)
public abstract class AppDatabase extends RoomDatabase {
    public abstract TrainingDao trainingDao();
    public abstract ProgressDao progressDao();

    private static volatile AppDatabase INSTANCE;

    static AppDatabase getDatabase(Context context) {
        if (INSTANCE == null) {
            synchronized (AppDatabase.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(),
                            AppDatabase.class, "ski_foundation_db")
                            .build();
                }
            }
        }
        return INSTANCE;
    }
}
```

**DAO Interfaces**

```java
// TrainingDao.java
@Dao
public interface TrainingDao {
    @Query("SELECT * FROM trainings")
    List<Training> getAllTrainings();

    @Insert
    void insertTraining(Training training);
}

// ProgressDao.java
@Dao
public interface ProgressDao {
    @Query("SELECT * FROM progress WHERE trainingId = :trainingId")
    Progress getProgressByTrainingId(int trainingId);

    @Insert
    void insertProgress(Progress progress);

    @Update
    void updateProgress(Progress progress);
}
```

**Repository**

```java
// TrainingRepository.java
public class TrainingRepository {
    private TrainingDao trainingDao;
    private ProgressDao progressDao;

    public TrainingRepository(Application application) {
        AppDatabase db = AppDatabase.getDatabase(application);
        trainingDao = db.trainingDao();
        progressDao = db.progressDao();
    }

    public List<Training> getAllTrainings() {
        return trainingDao.getAllTrainings();
    }

    public void insertTraining(Training training) {
        trainingDao.insertTraining(training);
    }

    public Progress getProgressByTrainingId(int trainingId) {
        return progressDao.getProgressByTrainingId(trainingId);
    }

    public void insertProgress(Progress progress) {
        progressDao.insertProgress(progress);
    }

    public void updateProgress(Progress progress) {
        progressDao.updateProgress(progress);
    }
}
```

**ViewModel**

```java
// TrainingViewModel.java
public class TrainingViewModel extends AndroidViewModel {
    private TrainingRepository repository;

    public TrainingViewModel(Application application) {
        super(application);
        repository = new TrainingRepository(application);
    }

    public List<Training> getAllTrainings() {
        return repository.getAllTrainings();
    }

    public void insertTraining(Training training) {
        repository.insertTraining(training);
    }

    public Progress getProgressByTrainingId(int trainingId) {
        return repository.getProgressByTrainingId(trainingId);
    }

    public void insertProgress(Progress progress) {
        repository.insertProgress(progress);
    }

    public void updateProgress(Progress progress) {
        repository.updateProgress(progress);
    }
}
```

**Activity**

```java
// TrainingActivity.java
public class TrainingActivity extends AppCompatActivity {
    private TrainingViewModel viewModel;
    private RecyclerView recyclerView;
    private TrainingAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_training);

        recyclerView = findViewById(R.id.recycler_view);

        viewModel = new ViewModelProvider(this).get(TrainingViewModel.class);

        viewModel.getAllTrainings().observe(this, trainings -> {
            adapter = new TrainingAdapter(trainings);
            recyclerView.setAdapter(adapter);
        });
    }
}
```

**Adapter**

```java
// TrainingAdapter.java
public class TrainingAdapter extends RecyclerView.Adapter<TrainingAdapter.ViewHolder> {
    private List<Training> trainings;

    public TrainingAdapter(List<Training> trainings) {
        this.trainings = trainings;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_training, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Training training = trainings.get(position);
        holder.titleTextView.setText(training.getTitle());
        holder.descriptionTextView.setText(training.getDescription());
    }

    @Override
    public int getItemCount() {
        return trainings.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        public TextView titleTextView;
        public TextView descriptionTextView;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            titleTextView = itemView.findViewById(R.id.title_text_view);
            descriptionTextView = itemView.findViewById(R.id.description_text_view);
        }
    }
}
```

**Service for downloading data**

```java
// DataDownloadService.java
public class DataDownloadService extends IntentService {
    private static final String ACTION_DOWNLOAD_DATA = "com.example.action.DOWNLOAD_DATA";

    public DataDownloadService() {
        super("DataDownloadService");
    }

    public static void startActionDownloadData(Context context) {
        Intent intent = new Intent(context, DataDownloadService.class);
        intent.setAction(ACTION_DOWNLOAD_DATA);
        context.startService(intent);
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if (intent != null) {
            final String action = intent.getAction();
            if (ACTION_DOWNLOAD_DATA.equals(action)) {
                downloadData();
            }
        }
    }

    private void downloadData() {
        // Download JSON data from API
        String jsonData = downloadJsonDataFromApi();

        // Parse JSON data
        List<Training> trainings = parseJsonData(jsonData);

        // Insert trainings into database
        AppDatabase db = AppDatabase.getDatabase(this);
        TrainingDao trainingDao = db.trainingDao();
        for (Training training : trainings) {
            trainingDao.insertTraining(training);
        }
    }

    private String downloadJsonDataFromApi() {
        // Implement API call to download JSON data
        // For demonstration purposes, assume we have a JSON string
        return "[{\"id\":1,\"title\":\"Training 1\",\"description\":\"Description 1\"}]";
    }

    private List<Training> parseJsonData(String jsonData) {
        // Implement JSON parsing
        // For demonstration purposes, assume we have a list of Training objects
        List<Training> trainings = new ArrayList<>();
        trainings.add(new Training());
        return trainings;
    }
}
```

**BroadcastReceiver for handling network changes**

```java
// NetworkChangeReceiver.java
public class NetworkChangeReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.getAction().equals(ConnectivityManager.CONNECTIVITY_ACTION)) {
            boolean isConnected = isConnected(context);
            if (isConnected) {
                // Download data when network is available
                DataDownloadService.startActionDownloadData(context);
            }
        }
    }

    private boolean isConnected(Context context) {
        ConnectivityManager cm = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
        return activeNetwork != null && activeNetwork.isConnectedOrConnecting();
    }
}
```

**AndroidManifest.xml**

```xml
<application
    ...>

    <receiver
        android:name=".NetworkChangeReceiver"
        android:enabled="true">
        <intent-filter>
            <action android:name="android.net.conn.CONNECTIVITY_ACTION" />
        </intent-filter>
    </receiver>

    <service
        android:name=".DataDownloadService"
        android:enabled="true"
        android:exported="true" />
</application>
```
