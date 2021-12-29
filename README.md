# receive_task_from_rabbitmq

## Run worker with:
celery worker -A app --without-heartbeat --without-gossip --without-mingle -P threads 