### Gradio Course 2021 - 9 Sections - 1 hour 50 minutes.
 1. What's the problem with current ML prototyping
   
 2. **What's gradio and Advantages of Gradio**
 3. **Getting Started with Gradio.**
 4. **Gradio Components**
 5. Gradio Multiple Inputs
 6. **Debugging and Flagging**
 7. Improving UI + UX
 8. **Gradio Sharing + Auth**
 9. **Deploying with Spaces**
---
### 1: streamlit vs. django vs flask vs dash vs gradio.
 - MVP - Minimum Viable Product
 - Gradio is used for minimal ML model deployment.
 - django, flask, streamlit and dash are much more inclusive and used for making web applications on big scale.

### 2: What's Gradio & Advantages of Gradio:
 - Build and share delightful machine learning apps
 - Gradio is the fastest way to demo your code machine learning model with a friendly web interface so that anyone can use it, anywhere!
 -  [Here](https://gradio.app/, (gradio website)) we can see basic example models in gradio
 -  Fast, easy setup, present and share features, permanent web hosting are some pros of using gradio.
 -  Can be embedded into google colab, jupyter notebook.
 -  [*Huggingface Spaces*](https://huggingface.co/spaces) let's you deploy your models  for **free**

### 3: First Gradio Application:
```python
gr.Interface(fn = hello_world, inputs="text", outputs = "text")
```
[docs](https://gradio.app/docs/)

### 4: Customise Gradio Components:
```python
1. gr.inputs.Textbox(lines=5, placeholder="Enter your input here ... ")
2. gr.inputs.Image(shape=(200, 200))
```
### 5: Gradio Multipe Inputs:

### 6: Debugging and Flagging:
 - Debugging gives the idea about the bugs in the application
 - We can tell gradio while launching the application that debug = True
 - Flagging in gradio is helpful when there is some erroneous results experienced by the user.
 - Flagging can be done, and we get flags for those specific inputs, and we can later improve our algorithms for better.

### 7: Improved user experience.
 - Examples are predefined answers in gradle, like placeholders, where it indicates the user, the input to be given to a particular box.
 - Examples can be provided to the gradio interface functions which contains the array of inputs.
 - The Interface can be made live as well, and if it is live, it changes the output in real-time and the user doesn't need to press submit all the time.
 - We can also provid the flagging options, to label things, according to the user.
 - We can also provide state to the UI.
 - We can also have different CSS and theme.

### 8: Sharing gradio application.
 - share option can be used to share the app, also we can share the api.
 - We can also add the authentication page on top of the application.
 - We can use the auth and auth_message option on the interface launch().

### 9. Deploying a DL Gradio App with 🤗 Spaces
  - [App deployed here](https://huggingface.co/spaces/AmmarHuggingFaces/intro-to-hugging-face)