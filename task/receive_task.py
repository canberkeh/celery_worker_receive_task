from app import celery

@celery.task(name="tasks.task_name", bind=True, default_retry_delay=30 * 60,
             soft_time_limit=1200, time_limit=1250, max_retry=3)

def task_name(self, **kwargs):
    print("task received")
    print(kwargs)