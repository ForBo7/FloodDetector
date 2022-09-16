import gradio as gr


def main():

    def greet(name):
        return "Hello " + name + "!!"

    iface = gr.Interface(fn=greet, inputs="text", outputs="text")
    iface.launch()


if __name__ == '__main__':
    main()
