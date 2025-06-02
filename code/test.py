import network
import socket
import time
import ujson
from machine import Pin, time_pulse_us

# --- WiFi Credentials ---
ssid = 'UGMURO-1'
password = 'Piscok2000'

# --- Sensor Pins ---
TRIG = Pin(3, Pin.OUT)
ECHO = Pin(2, Pin.IN)
IR = Pin(4, Pin.IN)

# --- Connect to WiFi ---
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected:", wlan.ifconfig())
    return wlan.ifconfig()[0]

# --- Ultrasonik Sensor ---
def read_distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    duration = time_pulse_us(ECHO, 1, 30000)  # timeout 30ms
    if duration < 0:
        return -1
    return round((duration / 2) / 29.1, 2)

# --- IR Sensor ---
def read_ir():
    return "Terdeteksi" if IR.value() == 0 else "Tidak Ada"

# --- HTML Halaman Utama ---
def serve_html():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Monitoring Sensor Realtime</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 30px; }
        .card { display: inline-block; margin: 20px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; }
        h2 { color: #007BFF; }
    </style>
</head>
<body>
    <h1>Monitoring Sensor Realtime</h1>
    <div class="card">
        <h2>Ultrasonik</h2>
        <p>Jarak: <span id="distance">-</span> cm</p>
    </div>
    <div class="card">
        <h2>Sensor IR</h2>
        <p>Status: <span id="ir">-</span></p>
    </div>

    <script>
        async function fetchData() {
            try {
                const res = await fetch('/data');
                const data = await res.json();
                document.getElementById('distance').textContent = data.distance;
                document.getElementById('ir').textContent = data.ir;
            } catch (e) {
                console.error("Error fetching:", e);
            }
        }
        setInterval(fetchData, 1000); // 1 detik
        fetchData(); // panggil pertama kali
    </script>
</body>
</html>"""

# --- Web Server ---
def start_server(ip):
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Web server running at http://{}'.format(ip))

    while True:
        cl, addr = s.accept()
        req = cl.recv(1024).decode()
        path = req.split(' ')[1]

        if path == '/':
            html = serve_html()
            cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
            cl.send(html)
        elif path == '/data':
            dist = read_distance()
            ir = read_ir()
            response = ujson.dumps({"distance": dist, "ir": ir})
            cl.send("HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n")
            cl.send(response)
        else:
            cl.send("HTTP/1.0 404 NOT FOUND\r\n\r\n")

        cl.close()

# --- Run ---
ip = connect_wifi()
start_server(ip)
