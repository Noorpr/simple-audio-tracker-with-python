import vlc
import time
import os
import sys


LOG_FILE = "playback_log.txt"


def seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{mins:02d}:{secs:02d}"


def get_last_timestamp(filename):
    if not os.path.exists(LOG_FILE):
        return 0
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in reversed(lines):
            if line.startswith(filename):
                parts = line.strip().split("Stopped at ")
                if len(parts) == 2:
                    hms = parts[1]
                    h, m, s = map(int, hms.split(":"))
                    return h * 3600 + m * 60 + s
    return 0

def log_timestamp(filename, current_time):
    hms = seconds_to_hms(current_time)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{filename} Stopped at {hms}\n")



def main():
    if len(sys.argv) < 2:
        print("Please open this script by clicking an audio file or dragging it onto the script.")
        return
    
    file_path = sys.argv[1]
    filename = os.path.basename(file_path)
    last_time = get_last_timestamp(filename)

    print(f"Resuming {filename} from {seconds_to_hms(last_time)}")

    player = vlc.MediaPlayer(file_path)
    player.play()

    time.sleep(1)
    player.set_time(int(last_time * 1000))

    print("Press Ctrl+C to stop and save progress")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        current_time = player.get_time() / 1000
        print(f"/n Stopped at {seconds_to_hms(current_time)}")
        log_timestamp(filename, current_time)
        player.stop()


if __name__ == "__main__":
    main()