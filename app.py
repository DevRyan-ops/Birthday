# from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def intro():
#     return render_template('intro.html')

# @app.route('/slide/<int:num>')
# def slide(num):
#     slides = [
#         {"text": "Welcome to a special day!", "button": "Next"},
#         {"text": "Let’s celebrate together.", "button": "Continue"}
#     ]
#     if num < len(slides):
#         data = slides[num]
#         next_url = url_for('slide', num=num+1) if num+1 < len(slides) else url_for('final')
#         return render_template('slide.html', text=data["text"], button=data["button"], next_url=next_url)
#     else:
#         return redirect(url_for('final'))

# @app.route('/final')
# def final():
#     # Customize with name and age
#     name = "Alex"
#     age = 21
#     return render_template('final.html', name=name, age=age)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def intro():
#     return render_template('intro.html', title='Birthday Intro')

# @app.route('/slide/<int:num>')
# def slide(num):
#     slides = [
#         {"text": "Welcome to a special day!", "button": "Next"},
#         {"text": "Let’s celebrate together.", "button": "Continue"}
#     ]
#     if 0 <= num < len(slides):
#         data = slides[num]
#         next_url = url_for('slide', num=num+1) if num + 1 < len(slides) else url_for('final')
#         back_url = url_for('intro') if num == 0 else url_for('slide', num=num-1)
#         return render_template(
#             'slide.html',
#             num=num,
#             title=f'Slide {num + 1}',
#             text=data["text"],
#             button=data["button"],
#             next_url=next_url,
#             back_url=back_url
#         )
#     else:
#         return redirect(url_for('intro'))

# @app.route('/final')
# def final():
#     name = "Alex"
#     age = 21
#     return render_template('final.html', title='Happy Birthday', name=name, age=age)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

# --- EDIT THESE VALUES ---
# Store for personalized data
PERSON_NAME = 'DAD!!'  # <-- Change this to the person's name
PERSON_AGE = '51'    # <-- Change this to the person's age
# -------------------------

@app.route('/')
def index():
    """Renders the intro page."""
    return render_template('index.html')

@app.route('/messages')
def messages():
    """Renders the messages page."""
    return render_template('messages.html')

@app.route('/cake')
def cake():
    """Renders the final cake page with personalized data."""
    
    # Logic to determine the age suffix (e.g., 25th, 21st)
    age_suffix = 'th'
    if PERSON_AGE == '1' or (len(PERSON_AGE) > 1 and PERSON_AGE.endswith('1') and PERSON_AGE != '11'):
        age_suffix = 'st'
    elif PERSON_AGE == '2' or (len(PERSON_AGE) > 1 and PERSON_AGE.endswith('2') and PERSON_AGE != '12'):
        age_suffix = 'nd'
    elif PERSON_AGE == '3' or (len(PERSON_AGE) > 1 and PERSON_AGE.endswith('3') and PERSON_AGE != '13'):
        age_suffix = 'rd'
        
    age_string = f"{PERSON_AGE}{age_suffix}"

    return render_template('cake.html', name=PERSON_NAME, age_string=age_string)

if __name__ == '__main__':
    app.run(debug=True)