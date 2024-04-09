# Celsius to Fahrenheit Converter using TensorFlow

This Python script demonstrates a simple Celsius to Fahrenheit converter using a neural network model built with TensorFlow. It trains the model on a small dataset of Celsius and Fahrenheit pairs and then predicts Fahrenheit values for given Celsius inputs.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- TensorFlow (`pip install tensorflow`)
- NumPy (`pip install numpy`)

## Usage

1. Clone the repository or download the script.
2. Run the script using the command `python celsius_to_fahrenheit_converter.py`.
3. The script will train the neural network model on the provided dataset.
4. After training, it will prompt you to input a Celsius temperature.
5. After entering a Celsius temperature, the script will predict the corresponding Fahrenheit temperature using the trained model and display the result.

## Script Overview

- The script uses TensorFlow to build a simple neural network model for converting Celsius temperatures to Fahrenheit temperatures.
- It defines a single dense layer in the model with one unit, as the problem involves a single input feature and a single output.
- The model is compiled with mean squared error loss and the Adam optimizer.
- It is trained on the provided Celsius and Fahrenheit data pairs.
- After training, the model predicts Fahrenheit temperatures for new Celsius inputs.

## Acknowledgments

- This script utilizes the TensorFlow library for building and training neural network models.
- Special thanks to the creators of TensorFlow for providing a powerful framework for machine learning.

## References

- [TensorFlow](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)

Feel free to modify and extend this script according to your requirements! If you have any questions or suggestions, please feel free to reach out.
