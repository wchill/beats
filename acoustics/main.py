from flask import Flask, request, jsonify
from song import get_song
from queue import Queue
import player

app = Flask(__name__)
app.debug = True

queue = Queue()

@app.route('/v1/player/play', methods=['PUT'])
def play():
    song_id = request.args.get('id')
    return jsonify(player.play_id(song_id))

@app.route('/v1/player/play_next', methods=['PUT'])
def play_next():
    return jsonify(queue.play_next(force=True) or {})

@app.route('/v1/player/pause', methods=['PUT'])
def pause():
    return jsonify(player.pause())

@app.route('/v1/player/status', methods=['GET'])
def player_status():
    return jsonify(player.get_status())

@app.route('/v1/songs/<song_id>', methods=['GET'])
def show_song(song_id):
    song = get_song(song_id)
    return jsonify(song or {})

@app.route('/v1/queue', methods=['GET'])
def show_queue():
    return jsonify(queue.get_queue())

@app.route('/v1/queue', methods=['DELETE'])
def queue_clear():
    return jsonify(queue.clear())

@app.route('/v1/queue/add', methods=['PUT'])
def queue_add():
    song_id = request.args.get('id')
    return jsonify(queue.add(song_id))

@app.route('/v1/now_playing', methods=['GET'])
def now_playing():
    return jsonify(queue.now_playing() or {})

if __name__ == '__main__':
    print 'Acoustics Media Player'
    print 'VLC version: ' + player.get_vlc_version()
    app.run()