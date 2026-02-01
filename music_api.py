import requests

def get_lyrics(artist: str, title: str, timeout: int=30):
    search_url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    try:
        response = requests.get(search_url, timeout=timeout)
        print(response)
        data = response.json()
        return data
    except Exception as e:
        print(f"Unknown error: {e}")
        return None
    
def get_album_art(artist, song):
    try:
        search_url = f"https://itunes.apple.com/search?term={artist}+{song}&entity=song&limit=1"
        response = requests.get(search_url).json()
        if response['resultCount'] > 0:
            # Get the 100x100 or 600x600 image URL
            return response['results'][0]['artworkUrl100'].replace('100x100', '600x600')
    except Exception as e:
        print(f"Unknown error: {e}")
        return None
    return None