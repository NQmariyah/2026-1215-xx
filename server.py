from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==========================================
# CHECKPOINT 1: MODEL DATABASE & RELASI ROLE
# ==========================================
# TODO: Inspeksi file database.db yang diberikan.
# Definisikan class model User, Poll, dan Vote di bawah ini.
# PERHATIAN: Perhatikan tipe data untuk status polling dan role pengguna di database bawaan (bukan boolean)!

# <TULIS MODEL DI SINI>

# Fungsi Helper
def get_current_user():
    token = request.headers.get('Authorization')
    if not token:
        return None
    return User.query.filter_by(token=token).first()

# ==========================================
# CHECKPOINT 2: AUTH & ENDPOINT KHUSUS ADMIN
# ==========================================
@app.route('/api/login', methods=['POST'])
def login():
    raise NotImplementedError("[Checkpoint-2] Fungsi login belum diimplementasikan")

@app.route('/api/polls', methods=['POST'])
def create_poll():
    raise NotImplementedError("[Checkpoint-2] Fungsi create_poll belum diimplementasikan")

@app.route('/api/polls/<int:poll_id>/archive', methods=['PATCH'])
def archive_poll(poll_id):
    raise NotImplementedError("[Checkpoint-2] Fungsi archive_poll belum diimplementasikan")

# ==========================================
# CHECKPOINT 3: ENDPOINT VOTER & VALIDASI
# ==========================================
@app.route('/api/polls', methods=['GET'])
def get_polls():
    raise NotImplementedError("[Checkpoint-3] Fungsi get_polls belum diimplementasikan")

@app.route('/api/votes', methods=['POST'])
def vote():
    raise NotImplementedError("[Checkpoint-3] Fungsi vote belum diimplementasikan")

if __name__ == '__main__':
    app.run(debug=True, port=5000)