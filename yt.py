import tkinter as tk          # when creating GUI components like windows, buttons, labels, etc.
from tkinter import filedialog     #Needed to let user choose folder or file

import subprocess             # Used to run external commands like yt-dlp from Python


def download_video(url, save_path):      # Define a function to download a video
    try:
        command = [                     # Create a list representing the yt-dlp command and its arguments
            "yt-dlp",                    #tells yt-dlp to download the extensions
            "-f", "bv*+ba/best",         # Tells yt-dlp to download:
                                            # - Best video (bv*) + best audio (ba)
                                            # - Fallback to 'best' if that fails
            "--merge-output-format", "mp4",      # Merge video and audio into a single .mp4 file


            "-o", f"{save_path}/%(title)s.%(ext)s",     # Output format: save as "<video title>.mp4" in given folder

            url                                     # The video URL to download
        ]
        subprocess.run(command, check=True)         # Runs the yt-dlp command and waits for it to finish
        print("Video downloaded in best quality!")     # Inform the user

    except subprocess.CalledProcessError as e:      # If something goes wrong
        print("Download failed:", e)                 # Print the error message

# Example usage
url = "https://www.youtube.com/watch?v=35YAXDG6M7I"     # A sample video URL (must be valid)
save_path = r"C:\Lalima s stuff\courses\you tube vedio downloader"    # Folder path to save the video
download_video(url, save_path)     # Call the function to start downloading
