import requests, json, xmltodict, datetime
from connection import check_mysql_connection

class TimeZone:
    def main(self):
        url = "http://api.timezonedb.com/v2.1/list-time-zone"
        response = requests.get(url, params="key=U8RQAAXEBIJS")
        data_dict = xmltodict.parse(response.content)
        timezones = []
        for zones in data_dict['result']['zones']['zone']:
            converted_timestamp = datetime.datetime.utcfromtimestamp(int(zones['timestamp']))
            zones['timestamp'] = converted_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            timezones.append(zones)
        
        return timezones

if __name__ == "__main__":
    timezone = TimeZone()
    timezones = timezone.main()
    print(json.dumps(timezones))
