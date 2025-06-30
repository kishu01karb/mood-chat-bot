from flask import Flask , render_template , request
from transformers import pipeline

app = Flask(__name__)

# load the ai model
classifier = pipeline("text-classification", model="nateraw/distilbert-base-uncased-emotion-lite")

#replies for mood
responses ={
    "joy":{
        "quote":"Spread your JOY!!!",
        "tip":"Celebrate this moment.",
        "link":"https://lifewellwandered.com/feeling-happy/#:~:text=Share%20your%20happiness%20with%20others&text=Compliment%20someone.,feeling%20as%20good%20as%20you."
    },
    "sadness":{
        "quote":"It's okay to feel sad sometimes",
        "tip":"Talk to someone or write it down.",
        "link":"https://findahelpline.com/"
    },
    "anger":{
        "quote":"Take a deep breathe. you are in control.",
        "tip":"Go on walk or write how you feel.",
        "link":"https://www.calm.com/breathe"
    },
    "fear":{
        "quote":"Fear means you are growing .",
        "tip":"Breathe.Take one step forward",
        "link":"https://youtu.be/94Yz4NrZZ08?si=yuM5McBcNlserY7e"
    },
    "love":{
        "quote":"Love makes the world better.",
        "tip":"Tell someone you love them today!",
        "link":"https://greatergood.berkeley.edu/"
    },
    "surprise":{
        "quote":"Unexpected things can be wonderful.",
        "tip":"Embrace the moment!!!",
        "link":"https://youtu.be/MSCyADD8cuM?si=UQNzZSoWAkjsE4_7"
    }
    
}

@app.route("/", methods=["GET","POST"])
def index():
    mood =""
    result ={}
    if request.method =="POST":
        user_input = request.form.get("user_input")
        prediction = classifier(user_input)[0]
        mood = prediction["label"]
        result =responses.get(mood.lower(),{
            "quote": "You matter. Stay strong.",
            "tip": "Take care of yourself today.",
            "link": "https://www.mentalhealth.org.uk/"
        })
    return render_template("index.html", mood=mood,result= result)

if __name__ == "__main__":
    app.run(debug=True)
