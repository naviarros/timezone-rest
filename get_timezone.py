import requests, json, xmltodict, datetime
from connection import check_mysql_connection
from timezone_helper import TimeZone
class TimeZoneList:
    def __init__(self):
        self.connect = check_mysql_connection()
        self.timezone = TimeZone().main()
    def main(self):
        cursor = self.connect.cursor()
        for timezones in self.timezone:
            insert_to_tz_table = """
                INSERT INTO tzdb_timezones (countrycode, countryname, zonename, gmtoffset, import_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_to_tz_table, (timezones['countryCode'], timezones['countryName'], timezones['zoneName'], timezones['gmtOffset'], timezones['timestamp']))

            self.connect.commit()

        cursor.close()
        self.connect.close()
        
if __name__ == "__main__":
    timezone = TimeZoneList()
    timezone.main()
