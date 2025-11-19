"""
Generated Code Metadata:
========================
Original URL: https://baycarepatientportal.net
Prompt: Develop a feature for a mobile app that allows users to track their BayCare appointments and set reminders, as mentioned in the site's benefits section.
Generated: DETERMINISTIC_ceace8fc851b90d7
Batch ID: 20250612_153648
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

# Generated Code:
# ===============

```kotlin
// AppointmentReminderFeature.kt
package com.baycare.appointments

import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import androidx.core.content.ContextCompat
import java.util.Calendar

/**
 * Class to handle appointment tracking and reminders
 */
class AppointmentReminderManager(private val context: Context) {

    companion object {
        const val REMINDER_REQUEST_CODE = 1001
        const val APPOINTMENT_EXTRA = "appointment_data"
    }

    /**
     * Schedule a reminder for an appointment
     * @param appointment The appointment to set reminder for
     * @param minutesBefore Minutes before appointment to trigger reminder
     */
    fun scheduleReminder(appointment: Appointment, minutesBefore: Int) {
        val alarmManager = ContextCompat.getSystemService(
            context,
            AlarmManager::class.java
        ) ?: throw IllegalStateException("AlarmManager not available")

        val reminderTime = calculateReminderTime(appointment.dateTime, minutesBefore)
        
        val intent = Intent(context, AppointmentReminderReceiver::class.java).apply {
            putExtra(APPOINTMENT_EXTRA, appointment)
        }

        val pendingIntent = PendingIntent.getBroadcast(
            context,
            REMINDER_REQUEST_CODE + appointment.id.hashCode(),
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        alarmManager.setExactAndAllowWhileIdle(
            AlarmManager.RTC_WAKEUP,
            reminderTime.timeInMillis,
            pendingIntent
        )
    }

    /**
     * Cancel an existing reminder for an appointment
     * @param appointment The appointment to cancel reminder for
     */
    fun cancelReminder(appointment: Appointment) {
        val alarmManager = ContextCompat.getSystemService(
            context,
            AlarmManager::class.java
        ) ?: throw IllegalStateException("AlarmManager not available")

        val intent = Intent(context, AppointmentReminderReceiver::class.java)
        val pendingIntent = PendingIntent.getBroadcast(
            context,
            REMINDER_REQUEST_CODE + appointment.id.hashCode(),
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        alarmManager.cancel(pendingIntent)
        pendingIntent.cancel()
    }

    private fun calculateReminderTime(appointmentTime: Calendar, minutesBefore: Int): Calendar {
        val reminderTime = appointmentTime.clone() as Calendar
        reminderTime.add(Calendar.MINUTE, -minutesBefore)
        return reminderTime
    }
}

// AppointmentReminderReceiver.kt
package com.baycare.appointments

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat

class AppointmentReminderReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val appointment = intent.getParcelableExtra<Appointment>(
            AppointmentReminderManager.APPOINTMENT_EXTRA
        ) ?: return

        showNotification(context, appointment)
    }

    private fun showNotification(context: Context, appointment: Appointment) {
        val notification = NotificationCompat.Builder(context, "appointment_reminders")
            .setSmallIcon(R.drawable.ic_calendar_reminder)
            .setContentTitle("Upcoming BayCare Appointment")
            .setContentText("You have an appointment at ${appointment.location} in ${appointment.timeUntil()}")
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .setCategory(NotificationCompat.CATEGORY_REMINDER)
            .setAutoCancel(true)
            .build()

        NotificationManagerCompat.from(context).notify(
            appointment.id.hashCode(),
            notification
        )
    }
}

// Appointment.kt
package com.baycare.appointments

import android.os.Parcelable
import kotlinx.parcelize.Parcelize
import java.util.Calendar

@Parcelize
data class Appointment(
    val id: String,
    val dateTime: Calendar,
    val location: String,
    val provider: String,
    val type: String
) : Parcelable {
    fun timeUntil(): String {
        val now = Calendar.getInstance()
        val diff = dateTime.timeInMillis - now.timeInMillis
        val hours = diff / (60 * 60 * 1000)
        val minutes = (diff / (60 * 1000)) % 60
        return "${hours}h ${minutes}m"
    }
}

// AppointmentRepository.kt
package com.baycare.appointments

import kotlinx.coroutines.flow.Flow

interface AppointmentRepository {
    fun getUpcomingAppointments(): Flow<List<Appointment>>
    suspend fun refreshAppointments()
    suspend fun getAppointmentById(id: String): Appointment?
}

// BayCareApiService.kt
package com.baycare.appointments.network

import com.baycare.appointments.Appointment
import retrofit2.http.GET
import retrofit2.http.Header
import retrofit2.http.Path

interface BayCareApiService {
    @GET("api/appointments/upcoming")
    suspend fun getUpcomingAppointments(
        @Header("Authorization") authToken: String
    ): List<Appointment>

    @GET("api/appointments/{id}")
    suspend fun getAppointmentDetails(
        @Header("Authorization") authToken: String,
        @Path("id") appointmentId: String
    ): Appointment
}

// AppointmentViewModel.kt
package com.baycare.appointments.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.baycare.appointments.Appointment
import com.baycare.appointments.AppointmentRepository
import com.baycare.appointments.AppointmentReminderManager
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class AppointmentViewModel @Inject constructor(
    private val repository: AppointmentRepository,
    private val reminderManager: AppointmentReminderManager
) : ViewModel() {

    val appointments = repository.getUpcomingAppointments()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    fun refreshAppointments() {
        viewModelScope.launch {
            repository.refreshAppointments()
        }
    }

    fun setReminder(appointment: Appointment, minutesBefore: Int = 30) {
        reminderManager.scheduleReminder(appointment, minutesBefore)
    }

    fun cancelReminder(appointment: Appointment) {
        reminderManager.cancelReminder(appointment)
    }
}

// AppointmentListFragment.kt
package com.baycare.appointments.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import com.baycare.appointments.R
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class AppointmentListFragment : Fragment() {

    private val viewModel: AppointmentViewModel by viewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_appointment_list, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        viewModel.refreshAppointments()
        // Setup RecyclerView and observe appointments here
    }
}

// AndroidManifest.xml (partial)
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baycare.appointments">

    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application>
        <receiver
            android:name=".AppointmentReminderReceiver"
            android:exported="false" />
    </application>
</manifest>
```
