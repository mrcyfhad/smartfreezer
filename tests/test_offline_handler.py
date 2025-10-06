import time
from src.offline_handler import is_sensor_stale, process_sensor

# Happy path T-ALR-001
def test_sensor_stale_after_61s():
    last_update = time.time() - 61
    assert is_sensor_stale(last_update) is True
    assert process_sensor(last_update) == "stale"

# Edge case T-ALR-002
def test_sensor_not_stale_at_59s():
    last_update = time.time() - 59
    assert is_sensor_stale(last_update) is False
    assert process_sensor(last_update) == "online"
