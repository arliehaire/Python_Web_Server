# app/metrics_queries.py
from app.models import db, MetricLogs

def get_latest_metrics():
    latest = MetricLogs.query.order_by(MetricLogs.timestamp.desc()).first()
    if latest:
        return {
            "cpu": {
                "labels": ["User", "System"],
                "values": [latest.cpu_user, latest.cpu_system]
            },
            "ram": {
                "labels": ["Used RAM"],
                "values": [latest.ram_used]
            },
            "disk": {
                "labels": ["Reads", "Writes"],
                "reads": [latest.disk_reads],
                "writes": [latest.disk_writes]
            }
        }
    return {"cpu": {}, "ram": {}, "disk": {}}

