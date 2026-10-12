import datetime
import subprocess
import os

def update_log():
    # Path to the log file
    log_file = "activity_log.txt"
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to the log file
    with open(log_file, "a") as f:
        f.write(f"Updated at: {timestamp}\n")
    
    # Git commands
    try:
        subprocess.run(["git", "add", log_file], check=True)
        subprocess.run(["git", "commit", "-m", f"Daily update: {timestamp}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Successfully updated log and pushed to GitHub at {timestamp}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

if __name__ == "__main__":
    update_log()
