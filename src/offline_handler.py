import time

ALERTS_ENABLED = True  # feature toggle


def is_sensor_stale(last_update_time, threshold_seconds=60):
    return (time.time() - last_update_time) > threshold_seconds


def process_sensor(last_update_time):
    if ALERTS_ENABLED:
        stale = is_sensor_stale(last_update_time)
        if stale:
            print("Metric: offline_alerts_sent=1")  # observability
            return "stale"
        else:
            return "online"
    else:
        print("Feature disabled - rollback mode")
        return "disabled"
