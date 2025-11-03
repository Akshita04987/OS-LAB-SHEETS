import time
import logging
# Dummy function to simulate a process task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate some work
    logging.info(f"{task_name} ended")
