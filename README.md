# indisolar-final-layout

ngrok link to get flask app over any network and it will change when you restart the ngrok cmd  
https://2e89-2409-40f0-11d7-5d9e-155d-3870-2084-ddd5.ngrok-free.app/

http://192.168.31.52:5000



db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=30,  # Adjust based on workload
    host="localhost",  # Or server IP if hosted remotely
    user="root",
    password="nare@2058",
    database="remedydb",
    autocommit=True,  # Prevents timeout issues
    connection_timeout=60  # 60 seconds is ideal
)

def get_db_connection():
    return db_pool.get_connection()
