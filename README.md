# indisolar-final-layout



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
