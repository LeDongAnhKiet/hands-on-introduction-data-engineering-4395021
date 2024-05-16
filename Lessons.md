# Hands-On Introduction: Data Engineering

## 1. Installing Airflow

`!pip install apache-airflow`

### Initialze database

`airflow db migrate`

 ### Create a user account

```
airflow users create \
    --username <your username> \
    --firstname <your firstname> \
    --lastname <your lastname> \
    --role <your role> \
    --email <your email> \
    --password <your password>
```

### Check Airflow folder

```
cd airflow/
ls
```

### Disable CSRF to directly access Airflow codespace (Remember to enable it when in production)

Open webserver_config.py and change a similar line to `WTF_CSRF_ENABLED = False`

## 2. Running Airflow webserver & scheduler

```
airflow webserver -D
airflow scheduler -D
```

### Check if you have DAGs (Directed Acyclic Graphs) in Airflow

`airflow dags list`

### Stop Airflow webserver and scheduler by kill their process IDs

```
cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill
echo "" > $AIRFLOW_HOME/airflow-webserver.pid
cat $AIRFLOW_HOME/airflow-scheduler.pid | xargs kill
echo "" > $AIRFLOW_HOME/airflow-scheduler.pid
```

## 3. Adjusting Airflow configuration settings

### Check where Airflow folder is

`echo $AIRFLOW_HOME`

### List all configurations & options

`cat airflow/airflow.cfg | grep -oP '\[.*?\]'`

### Check enviorment variables in Airflow

`env | grep -i airflow`

### Disable example DAGs for production

Go to airflow.cfg and change a similar line to `load_examples = False`

## 4. Build a 1 Task DAG

### Check where DAGs suppose to be
`cat airflow/airflow.cfg | grep "dags_folder"`

Create a 1-task dag in airflow/dags/<your file>.py

### Ignore unnecessary warning from DAG task to diagnostic the correct 

`python -W ignore airflow/dags/<your file>.py`

Press the ▶️ button of the the DAG to run it

