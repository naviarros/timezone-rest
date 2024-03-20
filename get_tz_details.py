import requests, json, xmltodict, datetime
from connection import check_mysql_connection
from timezone_helper import TimeZone

class GetTimeZone:
    def __init__(self):
        self.connect = check_mysql_connection()
        self.timezone = TimeZone().main()
    def main(self):
        cursor = self.connect.cursor()
        for zones in self.timezone:
            get_zone_details = "http://api.timezonedb.com/v2.1/get-time-zone"
            response = requests.get(get_zone_details, params=f"key=U8RQAAXEBIJS&by=zone&zone={zones['zoneName']}&format=json")

            if response.status_code == 200:
                try:
                    data_dict = response.json()
                    
                    if data_dict['zoneEnd'] is None:
                        data_dict['zoneEnd'] = 0

                    insert_to_tz_details_table = """
                        INSERT INTO zone_details (countrycode, countryname, zonename, gmtoffset, dst, zonestart, zoneend, import_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    cursor.execute(insert_to_tz_details_table, (data_dict['countryCode'], data_dict['countryName'], data_dict['zoneName'], data_dict['gmtOffset'], data_dict['dst'], data_dict['zoneStart'], data_dict['zoneEnd'], data_dict['formatted']))

                    self.connect.commit()
                except ValueError:
                    # Handle JSON decoding error (e.g., empty response or invalid JSON format)
                    print("Error: Unable to decode JSON data from the response.")
            
        cursor.close()
        self.connect.close()

if __name__ == "__main__":
    timezone = GetTimeZone()
    timezone.main()
