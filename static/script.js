function silentSave() {
    const form = document.getElementById('saveForm');
    if (!form) return; // Safety check

    const formData = new FormData(form);
    const btn = document.getElementById('saveBtn');

    fetch('/save', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Visual feedback
            btn.innerHTML = "✓ Added to Collection";
            btn.style.background = "#282828";
            btn.style.color = "#1DB954";
            btn.style.borderColor = "#1DB954";
            btn.disabled = true;
        }
    })
    .catch(error => console.error('Error:', error));
}

// You can also move your 'copyLyrics' function here!
function copyLyrics() {
    const lyrics = document.querySelector('.lyrics-display').innerText;
    navigator.clipboard.writeText(lyrics).then(() => {
        alert("Lyrics copied to clipboard!");
    });
}