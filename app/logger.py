from app.models import db, MetricLogs
from app.metrics import fetch_metrics

def log_metrics(ip):
    data = fetch_metrics(ip)
    if not data:
        print(f"[ERROR] No data for {ip}")
        return

    try:
        entry = MetricLogs(
            ip=ip,
            cpu_user=data.get("system.cpu", {}).get("dimensions", {}).get("user", {}).get("value", 0.0),
            cpu_system=data.get("system.cpu", {}).get("dimensions", {}).get("system", {}).get("value", 0.0),
            ram_used=data.get("system.ram", {}).get("dimensions", {}).get("used", {}).get("value", 0.0),
            disk_reads=data.get("system.io", {}).get("dimensions", {}).get("reads", {}).get("value", 0.0),
            disk_writes=data.get("system.io", {}).get("dimensions", {}).get("writes", {}).get("value", 0.0),
            net_in=data.get("system.net", {}).get("dimensions", {}).get("in", {}).get("value", 0.0),
            net_out=data.get("system.net", {}).get("dimensions", {}).get("out", {}).get("value", 0.0)
        )
        db.session.add(entry)
        db.session.commit()
        print(f"[LOGGED] Metrics logged for {ip}")
    except Exception as e:
        db.session.rollback()  # prevent lingering transaction state
        print(f"[ERROR] Failed to log metrics: {e}")

