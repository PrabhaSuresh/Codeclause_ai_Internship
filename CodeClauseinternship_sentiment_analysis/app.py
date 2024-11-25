from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            try:
                analysis = TextBlob(text)
                sentiment_polarity = analysis.sentiment.polarity
                if sentiment_polarity > 0:
                    review = "Positive"
                elif sentiment_polarity == 0:
                    review = "Neutral"
                else:
                    review = "Negative"
                return jsonify(review=review)
            except Exception as e:
                return jsonify(error_message=f"An error occurred during the analysis: {str(e)}"), 500
        else:
            return jsonify(error_message="Please enter a review text.")
    return render_template("front.html")

if __name__ == '__main__':
    app.run(debug=True)