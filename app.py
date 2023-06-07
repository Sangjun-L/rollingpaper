from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from dotenv import load_dotenv
import os 

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient(MONGODB_URL, tlsCAFile=ca)
db = client.rollingsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/member/<member_id>')
def member(member_id):
   return render_template('member.html')

@app.route('/api/team', methods=["GET"])
def member_list():
   all_member = list(db.member.find({}, {'_id': False, 'mbti': False, 'musicURL': False, 'location': False, 'location': False, 'hobby': False}).sort('name', 1))
   return jsonify({'result':'success','list':all_member})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)