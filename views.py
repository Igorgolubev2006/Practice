from flask import request, jsonify
from logs.models import LogEntry
from logs.auth import auth

def register_views(app):
    @app.route('/logs', methods=['GET'])
    @auth.login_required
    def get_logs():
        ip = request.args.get('ip')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        query = LogEntry.query

        if ip:
            query = query.filter_by(ip_address=ip)
        if start_date:
            query = query.filter(LogEntry.timestamp >= start_date)
        if end_date:
            query = query.filter(LogEntry.timestamp <= end_date)

        logs = query.all()
        return jsonify([log.to_dict() for log in logs])
