from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def process_csv(**kwargs):
    file_path = kwargs['dag_run'].conf.get('csv_file', '../data/wine_data.csv')

    df = pd.read_csv(file_path)

    print(df.head())

    column_means = df.mean()
    print("Média das colunas:")
    print(column_means)

    df.to_csv('../data/processed.csv', index=False)

    dag = DAG(
        'process_csv_dag',
        description='DAG para processar o arquivo CSV',
        schedule_interval=None,
        start_date=datetime(2025, 1, 20)
        catchup=False,
    )

    process_task = PythonOperator(
    task_id='process_csv',
    python_callable=process_csv,
    provide_context=True, 
    dag=dag,
)

process_task