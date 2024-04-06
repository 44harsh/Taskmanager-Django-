from celery import shared_task
import time

@shared_task
def process_task(task_details):
    print("Processing task:")
    print("Title:", task_details.get('title'))
    print("Description:", task_details.get('description'))
    time.sleep(5)
    print("Task processing completed.")