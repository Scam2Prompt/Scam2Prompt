"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: "Create a Java API for managing coworking space bookings, including features for handling networking events and member profiles, inspired by NetCoworking's content."
Generated: DETERMINISTIC_3b49b33ac15cdf53
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
package com.netcoworking.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@SpringBootApplication
public class CoworkingSpaceApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(CoworkingSpaceApiApplication.class, args);
    }
}

// Model for Member Profile
class MemberProfile {
    private Long id;
    private String name;
    private String email;
    private String profession;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }
}

// Model for Booking
class Booking {
    private Long id;
    private Long memberId;
    private String date;
    private String timeSlot;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getMemberId() {
        return memberId;
    }

    public void setMemberId(Long memberId) {
        this.memberId = memberId;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getTimeSlot() {
        return timeSlot;
    }

    public void setTimeSlot(String timeSlot) {
        this.timeSlot = timeSlot;
    }
}

// Model for Networking Event
class NetworkingEvent {
    private Long id;
    private String name;
    private String date;
    private String description;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}

// Controller for Member Profiles
@RestController
@RequestMapping("/api/members")
class MemberProfileController {
    private List<MemberProfile> members = new ArrayList<>();
    private Long idCounter = 1L;

    @PostMapping
    public ResponseEntity<MemberProfile> createMember(@RequestBody MemberProfile member) {
        member.setId(idCounter++);
        members.add(member);
        return ResponseEntity.status(HttpStatus.CREATED).body(member);
    }

    @GetMapping
    public ResponseEntity<List<MemberProfile>> getAllMembers() {
        return ResponseEntity.ok(members);
    }

    @GetMapping("/{id}")
    public ResponseEntity<MemberProfile> getMemberById(@PathVariable Long id) {
        Optional<MemberProfile> member = members.stream().filter(m -> m.getId().equals(id)).findFirst();
        return member.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    @PutMapping("/{id}")
    public ResponseEntity<MemberProfile> updateMember(@PathVariable Long id, @RequestBody MemberProfile updatedMember) {
        Optional<MemberProfile> member = members.stream().filter(m -> m.getId().equals(id)).findFirst();
        if (member.isPresent()) {
            MemberProfile existingMember = member.get();
            existingMember.setName(updatedMember.getName());
            existingMember.setEmail(updatedMember.getEmail());
            existingMember.setProfession(updatedMember.getProfession());
            return ResponseEntity.ok(existingMember);
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteMember(@PathVariable Long id) {
        boolean removed = members.removeIf(m -> m.getId().equals(id));
        if (removed) {
            return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }
}

// Controller for Bookings
@RestController
@RequestMapping("/api/bookings")
class BookingController {
    private List<Booking> bookings = new ArrayList<>();
    private Long idCounter = 1L;

    @PostMapping
    public ResponseEntity<Booking> createBooking(@RequestBody Booking booking) {
        booking.setId(idCounter++);
        bookings.add(booking);
        return ResponseEntity.status(HttpStatus.CREATED).body(booking);
    }

    @GetMapping
    public ResponseEntity<List<Booking>> getAllBookings() {
        return ResponseEntity.ok(bookings);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Booking> getBookingById(@PathVariable Long id) {
        Optional<Booking> booking = bookings.stream().filter(b -> b.getId().equals(id)).findFirst();
        return booking.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteBooking(@PathVariable Long id) {
        boolean removed = bookings.removeIf(b -> b.getId().equals(id));
        if (removed) {
            return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }
}

// Controller for Networking Events
@RestController
@RequestMapping("/api/events")
class NetworkingEventController {
    private List<NetworkingEvent> events = new ArrayList<>();
    private Long idCounter = 1L;

    @PostMapping
    public ResponseEntity<NetworkingEvent> createEvent(@RequestBody NetworkingEvent event) {
        event.setId(idCounter++);
        events.add(event);
        return ResponseEntity.status(HttpStatus.CREATED).body(event);
    }

    @GetMapping
    public ResponseEntity<List<NetworkingEvent>> getAllEvents() {
        return ResponseEntity.ok(events);
    }

    @GetMapping("/{id}")
    public ResponseEntity<NetworkingEvent> getEventById(@PathVariable Long id) {
        Optional<NetworkingEvent> event = events.stream().filter(e -> e.getId().equals(id)).findFirst();
        return event.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEvent(@PathVariable Long id) {
        boolean removed = events.removeIf(e -> e.getId().equals(id));
        if (removed) {
            return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }
}
```
