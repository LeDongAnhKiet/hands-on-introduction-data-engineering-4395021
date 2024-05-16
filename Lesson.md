# Hands-On Introduction: Data Engineering

![Hands-On Introduction: Data Engineering][lil-thumbnail-url]

## Installing Airflow

`!pip install apache-airflow`

### Initialze database

`airflow db migrate`

 ### Create user account

```
airflow users create \
    --username <your username> \
    --firstname <your firstname> \
    --lastname <your lastname> \
    --role <your role> \
    --email <your email> \
    --password <your password>
```

### Check airflow folder

`cd airflow/`
`ls`

### Disable CSRF to directly access Airflow codespace (enable it when in production)

Open webserver_config.py and change  this

`WTF_CSRF_ENABLED = False`

## Running Airflow webserver and scheduler

`airflow webserver -D`
`airflow scheduler -D`

### Check if you have DAGs (Directed Acyclic Graphs) in Airflow

`airflow dags list`

### Stop Airflow webserver and scheduler by kill their process IDs

`cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill`
`echo "" > $AIRFLOW_HOME/airflow-webserver.pid`
`cat $AIRFLOW_HOME/airflow-scheduler.pid | xargs kill`
`echo "" > $AIRFLOW_HOME/airflow-scheduler.pid`