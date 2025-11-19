"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Implement a feature in Flutter that supports high-quality real-time video and audio calls, inspired by Connexa's core functionality.
Generated: DETERMINISTIC_ce5fe6278ff28da0
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
// main.dart
import 'package:flutter/material.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:agora_rtc_engine/agora_rtc_engine.dart';

void main() {
  runApp(const VideoCallApp());
}

class VideoCallApp extends StatelessWidget {
  const VideoCallApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Connexa-like Video Call',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const VideoCallPage(),
    );
  }
}

class VideoCallPage extends StatefulWidget {
  const VideoCallPage({super.key});

  @override
  State<VideoCallPage> createState() => _VideoCallPageState();
}

class _VideoCallPageState extends State<VideoCallPage> {
  final String appId = 'YOUR_AGORA_APP_ID';
  final String channelName = 'test_channel';
  final String token = 'YOUR_AGORA_TEMP_TOKEN';

  bool isJoined = false;
  bool isMuted = false;
  bool isVideoDisabled = false;
  late RtcEngine agoraEngine;
  List<int> remoteUid = [];
  int? localUid;

  @override
  void initState() {
    super.initState();
    setupVideoSDKEngine();
  }

  Future<void> setupVideoSDKEngine() async {
    // Request microphone and camera permissions
    await [Permission.microphone, Permission.camera].request();

    // Create an instance of the Agora engine
    agoraEngine = createAgoraRtcEngine();
    await agoraEngine.initialize(RtcEngineContext(appId: appId));

    // Register the event handler
    agoraEngine.registerEventHandler(
      RtcEngineEventHandler(
        onJoinChannelSuccess: (RtcConnection connection, int elapsed) {
          setState(() {
            isJoined = true;
            localUid = connection.localUid;
          });
        },
        onUserJoined: (RtcConnection connection, int remoteUid, int elapsed) {
          setState(() {
            this.remoteUid.add(remoteUid);
          });
        },
        onUserOffline: (RtcConnection connection, int remoteUid, UserOfflineReasonType reason) {
          setState(() {
            this.remoteUid.remove(remoteUid);
          });
        },
        onError: (ErrorCodeType err, String msg) {
          debugPrint('Error: $err - $msg');
        },
      ),
    );

    // Enable video
    await agoraEngine.enableVideo();
  }

  Future<void> join() async {
    try {
      await agoraEngine.joinChannel(
        token: token,
        channelId: channelName,
        uid: 0,
        options: const ChannelMediaOptions(
          channelProfile: ChannelProfileType.channelProfileCommunication,
          clientRoleType: ClientRoleType.clientRoleBroadcaster,
        ),
      );
    } catch (e) {
      debugPrint('Error joining channel: $e');
    }
  }

  Future<void> leave() async {
    try {
      await agoraEngine.leaveChannel();
      setState(() {
        isJoined = false;
        remoteUid.clear();
      });
    } catch (e) {
      debugPrint('Error leaving channel: $e');
    }
  }

  void toggleMute() {
    setState(() {
      isMuted = !isMuted;
    });
    agoraEngine.muteLocalAudioStream(isMuted);
  }

  void toggleVideo() {
    setState(() {
      isVideoDisabled = !isVideoDisabled;
    });
    agoraEngine.muteLocalVideoStream(isVideoDisabled);
  }

  @override
  void dispose() {
    agoraEngine.leaveChannel();
    agoraEngine.release();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Video Call'),
      ),
      body: Stack(
        children: [
          // Local video preview
          Center(
            child: isJoined
                ? AgoraVideoView(
                    controller: VideoViewController(
                      rtcEngine: agoraEngine,
                      canvas: const VideoCanvas(uid: 0),
                    ),
                  )
                : const Text('Join a channel to start video call'),
          ),
          // Remote video views
          for (final uid in remoteUid)
            Positioned(
              top: 100,
              right: 20,
              width: 120,
              height: 150,
              child: AgoraVideoView(
                controller: VideoViewController.remote(
                  rtcEngine: agoraEngine,
                  canvas: VideoCanvas(uid: uid),
                  connection: RtcConnection(channelId: channelName),
                ),
              ),
            ),
          // Call controls
          Positioned(
            bottom: 20,
            left: 0,
            right: 0,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                IconButton(
                  onPressed: toggleMute,
                  icon: Icon(isMuted ? Icons.mic_off : Icons.mic),
                  color: Colors.white,
                  style: IconButton.styleFrom(
                    backgroundColor: Colors.blueGrey,
                    padding: const EdgeInsets.all(15),
                  ),
                ),
                IconButton(
                  onPressed: isJoined ? leave : join,
                  icon: Icon(isJoined ? Icons.call_end : Icons.call),
                  color: Colors.white,
                  style: IconButton.styleFrom(
                    backgroundColor: isJoined ? Colors.red : Colors.green,
                    padding: const EdgeInsets.all(15),
                  ),
                ),
                IconButton(
                  onPressed: toggleVideo,
                  icon: Icon(isVideoDisabled ? Icons.videocam_off : Icons.videocam),
                  color: Colors.white,
                  style: IconButton.styleFrom(
                    backgroundColor: Colors.blueGrey,
                    padding: const EdgeInsets.all(15),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

```yaml
# pubspec.yaml
name: video_call_app
description: A Connexa-like video calling app using Flutter and Agora

publish_to: 'none'

version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  agora_rtc_engine: ^6.2.0
  permission_handler: ^10.2.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
```
