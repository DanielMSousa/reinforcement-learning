import os

# Set environment variable to suppress Wayland-related warnings
os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.pause(.1)
    plt.show(block=False)

import os
import matplotlib.pyplot as plt

def save_plot(scores, filename='training_plot.png', folder='model_scores'):
    # Cria a pasta se ela não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Define o caminho completo para o arquivo, incluindo a pasta
    filepath = os.path.join(folder, filename)

    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.savefig(filepath)