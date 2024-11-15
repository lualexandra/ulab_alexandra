import numpy as np
import matplotlib.pyplot as plt


# function 1: side by side ???
def plot_horizontal_subplots():
    x = np.linspace(0, 2 * np.pi, 50)
#domain
    
    h_x = np.cos(x)  # h(x) = cos(x)
    k_x = np.sin(x)  # k(x) = sin(x)
#functions
    
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  
#plots
    
    axs[0].plot(x, h_x, color='blue')
    axs[0].set_title('h(x) = cos(x)')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('h(x)')
#left plot for h(X)

    axs[1].plot(x, k_x, color='red')
    axs[1].set_title('k(x) = sin(x)')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('k(x)')
#right plot for k(x)

    plt.tight_layout() 
    plt.show()

# function 2: stacked vertical subplots
def plot_vertical_subplots():
    x = np.linspace(0, 2 * np.pi, 500)
#domain

    h_x = np.cos(x)  # h(x) = cos(x)
    k_x = np.sin(x)  # k(x) = sin(x)
#functions

    fig, axs = plt.subplots(2, 1, figsize=(8, 10)) 
#plots

    axs[0].plot(x, h_x, color='blue')
    axs[0].set_title('h(x) = cos(x)')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('h(x)')
#top plot h(x)

    axs[1].plot(x, k_x, color='red')
    axs[1].set_title('k(x) = sin(x)')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('k(x)')
#bottom plot k(x)
    
    plt.tight_layout()  
    plt.show()