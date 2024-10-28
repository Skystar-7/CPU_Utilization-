from flask import Flask, jsonify, render_template
import psutil
import time
import threading

app = Flask(__name__)

# Global variable to hold current stats
current_stats = {"cpu": 0, "memory": 0, "disk": 0}

# List to store historical data
historical_data = []

def update_stats():
    global current_stats
    while True:
        # Measure CPU usage with a 1-second interval
        current_stats["cpu"] = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()
        current_stats["memory"] = mem_info.percent
        disk_info = psutil.disk_usage('/')
        current_stats["disk"] = disk_info.percent

        # Store historical data
        historical_data.append({
            "cpu": current_stats["cpu"],
            "memory": current_stats["memory"],
            "disk": current_stats["disk"]
        })

        time.sleep(1)  # Update every second

# Start the stats update thread
threading.Thread(target=update_stats, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system-stats', methods=['GET'])
def get_system_stats():
    return jsonify(current_stats)

@app.route('/api/historical-data', methods=['GET'])
def get_historical_data():
    return jsonify(historical_data)

if __name__ == '__main__':
    app.run(debug=True, host='10.0.1.142', port=12345)
