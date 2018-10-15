from flask import render_template

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html', username=username)

