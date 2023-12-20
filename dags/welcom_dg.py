from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import requests
def print_welcome():
    print('ELT DAG!')
def print_date():
    print('Today is {}'.format(datetime.today().date()))
def print_random_quote():
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()['content']
    print('Data Extraction: "{}"'.format(quote))
dag = DAG(
    'start_time',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)
start_timeD = PythonOperator(
    task_id='Start_Time',
    python_callable=print_welcome,
    dag=dag
)
ELT = PythonOperator(
    task_id='ELT',
    python_callable=print_date,
    dag=dag
)
transform = PythonOperator(
    task_id='Transform',
    python_callable=print_random_quote,
    dag=dag
)
# Set the dependencies between the tasks
start_timeD >> ELT >> transform