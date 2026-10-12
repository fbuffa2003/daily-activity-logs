import datetime
import subprocess
import random
import os

def update_log():
    # Path to the log file
    log_file = "activity_log.txt"
    
    # Generate a random time between 09:00 and 18:00 (9 AM to 6 PM)
    # This ensures the "contribution" looks like it happened during work hours.
    random_hour = random.randint(9, 18)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    now = datetime.datetime.now()
    # Create a "fake" time for today with the random hour/min/sec
    fake_time = now.replace(hour=random_hour, minute=random_minute, second=random_second, microsecond=0)
    timestamp_str = fake_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to the log file
    with open(log_file, "a") as f:
        f.write(f"Updated at: {timestamp_str}\n")
    
    # Git commands
    try:
        # We use --date to set the commit timestamp to our randomized time
        # This is what affects the GitHub contribution graph.
        subprocess.run(["git", "add", log_file], check=True)
        subprocess.run(["git", "commit", "-m", f"Daily update: {timestamp_str}", f"--date={timestamp_str}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Successfully updated log and pushed to GitHub with randomized time: {timestamp_str}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

if __name__ == "__main__":
    update_log()
