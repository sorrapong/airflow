from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=None,
)

task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

task1
