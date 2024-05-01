

import openai
import gradio as gr

openai.api_key = "7099752426:AAFS_g9yhElCK5y1wuLGKBAqrb8DSEkqs98"

messages = messages = [
    {"role": "system", "content": "You are a helpful AI assistant that only provides vegan recipies using only ingredients in the input. Only if the recipie contains a sauce,  provide three options with different ingredients. You add a vegan fact after every recipe"}
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7,label="Enter the ingredients you would like to use")
outputs = gr.outputs.Textbox(label="Lets get cookin'")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Vegan AI Chatbot",
             description="Enter any ingredients you have so I can make a vegan",
css='div {margin-left: auto; margin-right: auto; width: 80%;\
            background-image: url("https://previews.123rf.com/images/petitelili/petitelili1507/petitelili150700059/42691847-modern-seamless-background-with-objects-in-cute-cartoon-hand-drawn-style-on-vegan-food-theme-fruit.jpg"); repeat 0 0;}')\
                .launch(share=True)



