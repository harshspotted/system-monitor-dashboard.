from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def get_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    stats = {
        'cpu': cpu_usage,
        'memory': memory_info.percent,
        'disk': disk_info.percent
    }
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)
