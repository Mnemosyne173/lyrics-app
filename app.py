from flask import Flask, render_template, request, redirect
from music_api import get_lyrics, get_album_art

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def get_api_data():
    artist = None
    song = None
    lyrics = None
    image_url = None
    context = {}
    if request.method == 'POST':
        # 1. Grab the info the user typed in the form
        artist = request.form.get('artist_name')
        song = request.form.get('song_name')
        try:
            # 2. Use that info to customize your API call
            data = get_lyrics(artist, song)
            lyrics = data.get('lyrics', "Lyrics not found") 
            image_url = get_album_art(artist, song)
            # 3. Extract the specific piece of info
            context = {
                'name': artist,
                'song': song, 
                'lyrics' : lyrics,
                'album_art' : image_url,
            }
        except Exception as e:
            print(f"Error: {e}")
    # 4. Send it back to the HTML
    return render_template('index.html', context=context)

@app.route('/save', methods=['POST'])
def save_favorite():
    artist = request.form.get('artist')
    song = request.form.get('song')
    image_url = request.form.get('album_art')    

    with open("favorites.txt", "r") as f:
        existing = f.read()

    if f"{artist} - {song}" not in existing:
        if artist and song:
            entry = f"{artist} - {song} | {image_url}\n"
            with open("favorites.txt", "a") as f:
                f.write(entry)
    # Return an empty response with a 204 "No Content" success code
    return '', 204

@app.route('/delete', methods=['POST'])
def delete_favorite():
    item_to_delete = request.form.get('fav_item')
    
    # Read all lines, keep everything EXCEPT the one we want to delete
    with open("favorites.txt", "r") as f:
        lines = f.readlines()
    
    with open("favorites.txt", "w") as f:
        for line in lines:
            if line.strip() != item_to_delete.strip():
                f.write(line)           
    return redirect('/')

@app.route('/')
def index():
    favs = []
    try:
        with open("favorites.txt", "r") as f:
            favs = f.readlines()
    except FileNotFoundError:
        favs = [] # File doesn't exist yet        
    return render_template('home.html', favorites=favs)

if __name__ == '__main__':
    app.run() #debug=True