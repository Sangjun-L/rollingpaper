import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')

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
    all_member = list(db.member.find({}, {'_id': False, 'mbti': False, 'musicURL': False,
        'location': False, 'location': False, 'hobby': False}).sort('name', 1))
    return jsonify({'result': 'success', 'list': all_member})


@app.route('/api/member/<member_id>', methods=["GET"])
def get_member(member_id):
    member_info = db.member.find_one({'memberId': member_id}, {'_id': False})
    if (member_info is None):
        return jsonify({'result': 'fail', 'message': '없는 팀원인데요!'})
    return jsonify({'result': 'success', 'data': member_info})


@app.route('/api/rollingpaper', methods=["POST"])
def make_rolling():
    rolling_list = list(db.comment.find({}, {'_id': False}))
    count = len(rolling_list) + 1
    doc = {
        'memberId': request.form['memberId'],
        'commentId': count,
        'name': request.form['name'],
        'password': request.form['password'],
        'comment': request.form['comment'],
        'date': request.form['date'],
    }
    db.comment.insert_one(doc)
    return jsonify({'result': 'success', 'message': '등록이 완료되었습니다.'})


@app.route('/api/rollingpaper/<member_id>', methods=["GET"])
def get_rolling(member_id):
    rolling_list = list(db.comment.find({'memberId': member_id}, {
                        '_id': False, 'memberId': False, 'password': False}).sort('date', -1))
    return jsonify({'result': 'success', 'list': rolling_list})

# 페이퍼 삭제
@app.route('/api/rollingpaper', methods=["DELETE"])
def del_rolling():
    comment_id = request.form['commentId']
    input_password = request.form['password']
    comment = db.comment.find_one({"commentId": int(comment_id)})

    if comment['password'] == input_password:
        db.comment.delete_one({"commentId":int(comment_id)})
        return jsonify({'result': 'success', 'message': '삭제 완료되었습니다.'})
    else:
        return jsonify({'result':'fail', 'message':'비밀번호가 다릅니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
