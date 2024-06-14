import re
from datetime import datetime
from logs.models import LogEntry, db
import venv.config as config
import os
import glob

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>GET|POST|PUT|DELETE|HEAD) (?P<path>.*?) HTTP/1\.[01]" (?P<status>\d+) .*? "(?P<user_agent>.*?)"'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return {
            'ip_address': match.group('ip'),
            'timestamp': datetime.strptime(match.group('date'), '%d/%b/%Y:%H:%M:%S %z'),
            'request_method': match.group('method'),
            'request_path': match.group('path'),
            'status_code': int(match.group('status')),
            'user_agent': match.group('user_agent'),
        }
    return None

def parse_logs():
    for log_file in glob.glob(os.path.join(config.Config.LOG_FILE_PATH, config.Config.LOG_FILE_PATTERN)):
        with open(log_file, 'r') as f:
            for line in f:
                data = parse_log_line(line)
                if data:
                    log_entry = LogEntry(**data)
                    db.session.add(log_entry)
            db.session.commit()

if __name__ == '__main__':
    from venv.app import create_app
    app = create_app()
    with app.app_context():
        parse_logs()
