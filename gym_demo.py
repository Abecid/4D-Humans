import os
import subprocess
import sys

from tqdm import tqdm
import cv2

def extract_median_frame(video_folder, output_folder):
    """
    Extract the median frame from all videos in the video_folder
    and save it to the output_folder.
    """
    for video in os.listdir(video_folder):
        if video.endswith(('.mp4', '.avi', '.mkv')):
            video_path = os.path.join(video_folder, video)
            cap = cv2.VideoCapture(video_path)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            median_frame_no = frame_count // 2
            cap.set(cv2.CAP_PROP_POS_FRAMES, median_frame_no)
            ret, frame = cap.read()
            if ret:
                output_image_path = os.path.join(output_folder, f"{os.path.splitext(video)[0]}.jpg")
                cv2.imwrite(output_image_path, frame)
            cap.release()

def run_demo_script(img_folder):
    """Run the demo.py script."""
    cmd = [
        "python", "demo.py",
        "--img_folder", img_folder,
        "--out_folder", "demo_out",
        "--batch_size=48", "--side_view", "--save_pose" # "--save_mesh", "--full_frame"
    ]
    subprocess.run(cmd)

def main():
    # The parent directory containing all the video folders.
    base_dir = "/home/amir/gymgpt/output/subreddits"
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    subreddit_folders = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for subreddit_folder in tqdm(subreddit_folders, desc="Processing Subreddits"):
        print(f"Processing {subreddit_folder}")
        video_folder = os.path.join(subreddit_folder, "videos")
        images_folder = os.path.join(subreddit_folder, "images")
        
        os.makedirs(images_folder, exist_ok=True)

        # Extract median frame from each video in the current video folder.
        extract_median_frame(video_folder, images_folder)

        # Run the demo.py script on the images folder.
        run_demo_script(images_folder)

if __name__ == "__main__":
    main()
