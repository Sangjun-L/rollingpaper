from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from dotenv import load_dotenv
import os 

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

from pymongo import MongoClient
client = MongoClient(MONGODB_URL)
db = client.rolling

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/member/<member_id>')
def member(member_id):
   return render_template('member.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)