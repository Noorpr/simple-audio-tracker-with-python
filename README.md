# simple-audio-tracker-with-python
A simple audio Tracker, it's task is to track the position of the video before cancelation so the user can track his progress on the audio files easily 



## How to use
Create a .txt file alognside your audio file(s) and put inside it this:
```
@echo off
python audio_tracker.py %1
 ```

Then rename the extenstion, instead of .txt, change it to be .bat.

After that drag your audio file onto the new created .bat file and it should run a black screen with your audio file running.
