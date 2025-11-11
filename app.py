import os
import random
from flask import Flask, render_template

app = Flask(__name__)


def get_sides():
    """Return how many sides the die should have based on the DICE_SIDES env var."""
    DICE_SIDES = int(os.getenv("DICE_SIDES", "6"))
    if DICE_SIDES < 2:
        DICE_SIDES = 6
    
    return DICE_SIDES


@app.route("/")
def index():
    sides = get_sides()
    # TODO: generar un numero aleatorio entre 1 y `sides`
    result = random.randint(1, sides)
    return render_template("index.html", result=result, sides=sides)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
