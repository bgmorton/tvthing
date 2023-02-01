import os
import random
import subprocess
import time

def get_video_files(directory):
    videos = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            if file.lower().endswith((".mp4", "mkv", "avi", "flv")):
                videos.append(os.path.join(root, file))
    return sorted(videos)

def save_played_items(played_items):
    with open("played_items.txt", "w") as f:
        for item in played_items:
            f.write(item + "\n")

def main():
    videos = get_video_files("./media")
    played_items = []
    try:
        with open("played_items.txt") as f:
            for line in f:
                played_items.append(line.strip())
    except FileNotFoundError:
        pass
    available_videos = [video for video in videos if video not in played_items]
    while available_videos:
        video = random.choice(available_videos)
        print("Now playing: ", video)
        time.sleep(3) # Padding starting/stopping VLC, just in case is slow to quit. It does seem to reduce the error mentioned below, but maybe a placebo.
        vlc = subprocess.run(["vlc", "--fullscreen", video, "vlc://quit"], capture_output=True) # "vlc://quit" is a special VLD URL that quits the application when played, and will be queued after the video.
        time.sleep(3)
        exit_code = vlc.returncode
        exit_output = vlc.stdout.decode() + vlc.stderr.decode() # Decode used for bytes to string.
        print(exit_output)
        if exit_code == 0 and "1094995529" not in exit_output: # Do not mark video as played if VLC exits with an error. Sometimes videos fail to play for mystery reasons, with an error that does not cause an exit code - error is 1094995529 so watch the output for it (appears in STDERR).
            print("Finished playing: ", video)
            played_items.append(video)
        else:
            print("Error, video not added to played list")
        available_videos = [video for video in videos if video not in played_items]
        save_played_items(played_items)
    print("All videos have been played")

if __name__ == "__main__":
    main()
