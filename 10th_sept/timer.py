import time

class Timer:
    def __init__(self,seconds):
        self.seconds = seconds
    def timer(seconds):
        start_time = time.time()  # Record the start time
        end_time = start_time + seconds  # Calculate the end time
    
        while True:
            current_time = time.time()  # Get the current time
            remaining_time = end_time - current_time  # Calculate remaining time
        
            if remaining_time <= 0:
                break  # Exit the loop when the time is up
        
        # Display the remaining time (optional)
            print(f"Time remaining: {remaining_time:.2f} seconds", end='\r')
        
        # Short sleep to prevent high CPU usage
            time.sleep(0.1)
    
