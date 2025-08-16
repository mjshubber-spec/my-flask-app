from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
import io
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    # Generate data for normal distribution
    mu, sigma = 0, 1  # mean and standard deviation
    x = np.linspace(-5, 5, 1000)
    y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)

    # Create the plot
    plt.figure(figsize=(6,4))
    plt.plot(x, y, color='blue')
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)

    # Save it to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
