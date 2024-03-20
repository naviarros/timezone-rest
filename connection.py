import pymysql as PyMySQL

def check_mysql_connection():
    try:
        connect = PyMySQL.connect(host="localhost", user="root", password="ivansorra11", database="timezonedb", use_unicode=True, charset="utf8", 
			cursorclass=PyMySQL.cursors.DictCursor,
			connect_timeout=30)
        return connect
    except BaseException as e:
        print(f"Error connecting to MySQL: {e}")

if __name__ == "__main__":
    check_mysql_connection()
