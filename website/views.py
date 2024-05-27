from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .models import Notes
from . import *
import json
import os
from groq import Groq

client = Groq(
    api_key='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'
)


views = Blueprint('views',__name__)

@views.route("/",methods=['GET','POST'])
@login_required #you can't get to the home page unless you login
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short',category='error')

        else:
            new_note = Notes(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added Successfully',category="success")


    return render_template("home.html",user=current_user)

@views.route("/delete-note", methods=['POST'])
@login_required
def delete_note():
    note_id = request.get_json().get('noteId')
    note = Notes.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({}), 200
    return jsonify({}), 400

@views.route('/chatwithgroq',methods=['GET','POST'])
@login_required
def chat_with_groq():
    # conetent_given=request.form.get("question")


    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": conetent_given,
    #         }
    #     ],
    #     model="llama3-8b-8192",
    # )

    # output=chat_completion.choices[0].message.content
    # # response_html = markdown.markdown(output)
    return render_template('groq.html',user=current_user)
