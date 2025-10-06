from offline_handler import process_sensor
import time

# simulate a sensor last updated 61 seconds ago
process_sensor(time.time() - 61)
