from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

# template_folder='templates' diyerek HTML'lerin yerini gösteriyoruz
app = Flask(__name__, template_folder='templates')
CORS(app)

# --- SAYFA YÖNLENDİRMELERİ (WebView İçin) ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/duyurular.html')
def duyurular_page():
    return render_template('duyurular.html')

@app.route('/kan_ilanlari.html')
def kan_page():
    return render_template('kan_ilanlari.html')

@app.route('/rektorluk.html')
def rektorluk_page():
    return render_template('rektorluk.html')

@app.route('/sohbet.html')
def sohbet_page():
    return render_template('sohbet.html')

@app.route('/admin.html')
def admin_page():
    return render_template('admin.html')

@app.route('/auth.html')
def auth_page():
    return render_template('auth.html')

@app.route('/ilmek_ana_ders_portal.html')
def ders_page():
    return render_template('ilmek_ana_ders_portal.html')

@app.route('/reklam_izle.html')
def reklam_page():
    return render_template('reklam_izle.html')

@app.route('/manevi_alan.html')
def manevi_page():
    return render_template('manevi_alan.html')

@app.route('/bagis.html')
def bagis_page():
    return render_template('bagis.html')

# --- API KISMI (Veri Alışverişi) ---
# Buraya senin API kodların gelecek (get_announcements vb.)
# Örnek bir API ucu:
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "online"})

if __name__ == '__main__':
    # Render'ın verdiği portu dinle
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)