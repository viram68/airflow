#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_bash_operator',
    schedule='0 0 * * *', #분,시,일,월,요일
    start_date=pendulum.datetime(2023, 11, 1, tz="Asia/seoul"),
    catchup=False, # True누락기간 모두 수행  False누락기간돌지않음
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['example', 'example2'], #airflow에서 dag아래 나오는 항목
    params={"example_key": "example_value"},
) as dag:
    # [END howto_operator_bash]
    run_bash_te = EmptyOperator(
        task_id='run_bash_te',
        bash_command='echo bash end',
    )

    # [START howto_operator_bash]
    run_bash_t0 = BashOperator(
        task_id='run_bash_t0',
         bash_command='echo bash start',
    )
  

    run_bash_t0 >> run_bash_te

    
if __name__ == "__main__":
    dag.cli()