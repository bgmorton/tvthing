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
    videos = get_video_files(".")
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
        time.sleep(3)#paddng starting/stopping vlc, just in case it hasnt quit. It does seem to reduce errors, maybe a placebo
        vlc = subprocess.run(["vlc", "--fullscreen", video, "vlc://quit"], capture_output=True)
        time.sleep(3)
        exit_code = vlc.returncode
        exit_output = vlc.stdout.decode() + vlc.stderr.decode()# decode used for bytes to string
        print(exit_output)
        # sometimes videos fail to play for mystery reasons, so only mark them played if there was no error- error is 1094995529 so watch the output for it (appears in stderr)
        if exit_code == 0 and "1094995529" not in exit_output:
            print("Finished playing: ", video)
            played_items.append(video)
        else:
            print("Error, video not added to played list")
        available_videos = [video for video in videos if video not in played_items]
        save_played_items(played_items)
    print("All videos have been played")

if __name__ == "__main__":
    main()
