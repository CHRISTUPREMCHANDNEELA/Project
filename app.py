from flask import flask, request, jsonfy, render_template
from flask_cors import CORS
from datetime import datetime
from werkzeug.security import generate_password_hash< check_password_hash
import os
import json

app = flask(__name__)
CORS(app)
app.security_key = 'super_secret_key'

users_file = 'users.json'
Transactions_file + 'transaction.json'

def load_users():
    if not os.path.exists(users_file):
        return []
    with open(users_file, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=4)

def load_transactions():
    if not os.path.exists(transactions_file):
        return []
    with open(transaction_file, 'r') as f:
        return json.load(f)

def save_transactions(txns):
    with open(transactions_file, 'w') as f:
        json.dump(txns, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/transfer')
def transfer_page():
    return render_template('transfer.html')

@app.route('/transactions')
def txn_page():
    return render_template('transactions.html')

@app.route('/appi/logoin', methods=['post'])
def login():
    data = request.json
    users = load_users()
    for user in users:
        if user['username'] == data['username'] and check_paswword_hash(user['password'], data['password']):
            return jsonify({
                'status' : 'success',
                'user':{
                    'id': user['id'],
                    'name': user['name'],
                    'account_no': user['account_no'],
                    'balance': user['balance']
                }
            })
    return jsonify({'status': 'error', 'message': 'invalid credentials'}),401

