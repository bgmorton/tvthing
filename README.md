# tvthing - Play videos randomly, remember what has played

This is a simple Python script that finds all videos in a directory, randomizes and plays them, and records what has been played.

## Why?

I have a lot of DVDs.  Choosing something to put on in the background is a chore, and usually results in watching the same things over and over. This solves that, basically emulating TV.

Why not TV? Ads.

## Why not use one of the many media center Linux distributions?

Because I want to do other things with my Raspberry Pi as well as using it to play media.

Additionally, most of those media centers have poor support for streaming sites like Youtube, and if they do have support, they don't have adblockers :)

## How do I use this?

This script is mean to be run on a Linux system with a desktop environment.  You'll also need the following installed and available on the command line:

- Python 3 
- VLC media player

RaspberryPi OS desktop ships with these dependencies already installed, so this script is ready to use if you're on a Pi.

Just place your media files in the `media` directory and then run `run.sh` in the terminal (you can also double click in RaspberryPi OS and click `Run in Terminal` when prompted).

If you want a desktop shortcut, copy `run.sh` to the desktop, and update the path to `tv.py` within it to the absolute path.

As media items play successfully, they will be recorded in `played_items.txt`.  Items listed in that file will not be played again. You can remove items from the list or delete it entirely if you want to reset.

## Other Notes

If VLC crashes with an exit code, the item being played will not be added to `played_items.txt`. Playback would occasionally fail for me with an error *1094995529*, but not an exit code - I couldn't nail down the cause (it might just be the rickety external hard drive my media is on), so I watch the VLC output specifically for that error number and also skip adding that item to `played_items.txt` if that code appears in the output.

Have fun!