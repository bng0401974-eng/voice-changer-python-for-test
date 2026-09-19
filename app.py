import gradio as gr


def transform_voice(audio_file):
    # Овде во иднина ќе ја вметнеш логиката со Python за обработка на гласот
    # За почеток, само го враќаме истиот фајл назад како тест
    if audio_file is None:
        return "Те молам прикачи аудио фајл."

    return audio_file


# Креирање на едноставен веб интерфејс преку Gradio
demo = gr.Interface(
    fn=transform_voice,
    inputs=gr.Audio(sources=["upload", "microphone"], type="filepath"),
    outputs=gr.Audio(label="Трансформирано аудио"),
    title="LATIVM Vocal Changer",
    description="Прикачи аудио или сними глас за да го промениме."
)

if __name__ == "__main__":
    demo.launch()
