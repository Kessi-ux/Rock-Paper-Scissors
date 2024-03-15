from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']
wins = 0
losses = 0
ties = 0

@app.route('/')
def index():
    return render_template('index.html', wins=wins, losses=losses, ties=ties)

@app.route('/play', methods=['POST'])
def play():
    global wins, losses, ties
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    if result == "You win!":
        wins += 1
    elif result == "You lose!":
        losses += 1
    else:
        ties += 1
    return render_template('index.html', result=result, user_choice=user_choice, computer_choice=computer_choice, wins=wins, losses=losses, ties=ties)

@app.route('/reset')
def reset():
    global wins, losses, ties
    wins = 0
    losses = 0
    ties = 0
    return redirect(url_for('index'))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

if __name__ == '__main__':
    app.run(debug=True)
