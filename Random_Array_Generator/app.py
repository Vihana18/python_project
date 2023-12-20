import numpy as np
import gradio as gr

def create_array(shape):
  shape = tuple(map(int, shape.split(',')))
  arr= np.random.randint(0,100, size=shape)
  return arr

x=gr.Interface(
      fn=create_array,
      inputs="text",
      outputs="text",
      title= "Random Array Generator",
      description= "Enter the shape is the format comma-seperated integers (e.g 2,3)"
  )
x.launch()
