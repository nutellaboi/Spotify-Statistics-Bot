from datetime import datetime
from datetime import timedelta

class DateTimeFormatting:

    def convert_string_to_datetime_ist(self,time_string):
        datetime_obj_utc=datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S.%fZ')#UTC format
        datetime_obj_ist=datetime_obj_utc+timedelta(hours=5,minutes=30)
        return datetime_obj_ist

    def convert_datetime_to_suitable_format(self,date):#dd-mm-yyyy h:m:s
        suitable_format=date.strftime('%d-%m-%Y %H:%M:%S')
        return suitable_format

    def get_todays_timestamp(self):#get todays timestamp with 00:00:00
        todays_timestamp=datetime.now()#exact time
        todays_timestamp_str=f'{todays_timestamp.day}-{todays_timestamp.month}-{todays_timestamp.year} 00:00:00'
        todays_timestamp_zero_hms=datetime.strptime(todays_timestamp_str, '%d-%m-%Y %H:%M:%S')
        return todays_timestamp_zero_hms.timestamp()
    
    def convert_ms_to_hms(self,duration_ms):
        seconds=round(duration_ms/1000)
        s=seconds%60
        m=(seconds/60)%60
        h=(seconds/(60 * 60))%24
        hms_str=f'{round(h)} hour {round(m)} minutes {round(s)} seconds'if round(h)==1 else f'{round(h)} hours {round(m)} minutes {round(s)} seconds'
        return hms_str