from flask import Blueprint, render_template, request, jsonify
from Backend.learn.tliorai import get_response

homepage = Blueprint('homepage', __name__)


@homepage.post('/analy')
def analy():
    text = request.get_json().get("user_message")
    response = get_response(text)
    bot_reply = {"reply": response}
    return jsonify(bot_reply)
