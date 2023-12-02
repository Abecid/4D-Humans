import os
import sys
from tqdm import tqdm


def main():
    data = []
    
    # Iterate over subreddits
    base_dir = "/home/amir/gymgpt/output/subreddits"
    pose_dir = "home/alee00/4D-Humans/demo_out"
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    subreddit_folders = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for subreddit_folder in tqdm(subreddit_folders, desc="Processing Subreddits"):
        print(f"Processing {subreddit_folder}")
        video_folder = os.path.join(subreddit_folder, "videos")
        submission_path = os.path.join(subreddit_folder, "submission.json")
        for video in os.listdir(video_folder):
            if video.endswith(('.mp4', '.avi', '.mkv')):
                video_name = os.path.splitext(video)[0]
                pose_path = os.path.join(pose_dir, f"{video_name}.npy")
                # for submission in submissions.json, check "Post ID" field equals to video_name
                comments = "Comments"
                
    # Iterate over videos/pose embeddings
    # Find the comments for each videos
    # Make the comments in the correct conversation format
    conversations = []
    
    data_json_object = {
        "id": "", # Pose ID (video filename)
        "pose": "", # Pose embedding filepath
        "conversations": conversations
    }
    
    # Save json file

if __name__ == "__main__":
    main()