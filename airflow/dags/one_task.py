from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'admin',
    'depends_on past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'catchup': False,
    'start date': datetime(2024, 1, 1)
}

with DAG(
    dag_id='one_task dag',
    description='A 1-task Airflow DAG',
    schedule_interval=None,
    default_args=default_args
    ) as dag:

    task1 = BashOperator(task_id='one_task', dag=dag,
        bash_command='echo "Hello!" > /workspaces/hands-on-introduction-data-engineering-4395021/lab/temp/file.txt')