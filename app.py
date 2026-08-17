from flask import Flask, render_template, request
from ai_caption import generate_caption
from ai_meme import generate_ai_meme

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    meme_path = None

    if request.method == "POST":
        topic = request.form["topic"]

        top_text, bottom_text = generate_caption(topic)
        caption_text = f"{top_text}\n{bottom_text}"

        meme_path = generate_ai_meme(topic, caption_text)

    return render_template("index.html", meme=meme_path)

if __name__ == "__main__":
    app.run(debug=True)
