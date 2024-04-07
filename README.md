# Taskmanager-Django-
# Api in django
# cmd to run project: python manage.py runserver
----------------------------------------------------------------------------------------
# API 1: create_task:
# http://127.0.0.1:8000/api/create-task/
# Method: POST
# Description: Accepts task details (e.g., title, description) and creates a new task.
----------------------------------------------------------------------------------------
# API 2: get_task_status
# http://127.0.0.1:8000/api/get-task-status/<int:task_id>/
# Method: GET
# Description: Retrieves the status of a task by task ID.
-----------------------------------------------------------------------------------------
# To run celery:
# celery -A TaskManager worker -l INFO
------------------------------------------------------------------------------------------
