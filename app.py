import gradio as gr

from services.process import process_meeting

with gr.Blocks(
    title="AI Meeting Minutes Generator",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown("""
# 🎙️ AI Meeting Minutes Generator

### Convert meeting recordings into professional meeting minutes using **Whisper**, **Llama**, and **Transformers**.

Upload an audio recording, choose the output language and format, and let AI generate structured meeting minutes automatically.
""")

    with gr.Row():

        with gr.Column():
            audio_input = gr.Audio(type="filepath", label="Upload Meeting Audio")

        with gr.Column():
            audio_preview = gr.Audio(label="Audio Preview", interactive=False)

    audio_input.change(
        fn=lambda audio: audio, inputs=audio_input, outputs=audio_preview
    )

    with gr.Row():

        with gr.Column():
            language = gr.Dropdown(
                choices=["English", "Hindi", "Marathi"],
                value="English",
                label="Output Language",
            )

        with gr.Column():
            output_style = gr.Dropdown(
                choices=[
                    "Professional",
                    "Executive Summary",
                    "Bullet Points",
                    "Agile Sprint Notes",
                ],
                value="Professional",
                label="Output Style",
            )

    generate_btn = gr.Button(
        "🚀 Generate Transcript & Meeting Minutes", variant="primary"
    )

    with gr.Row():

        with gr.Column():

            transcript_output = gr.Textbox(
                label="Transcript",
                lines=18,
                interactive=False,
                placeholder="The generated transcript will appear here...",
            )

        with gr.Column():

            meeting_minutes_output = gr.Markdown(
                value="### Meeting minutes will appear here..."
            )

    gr.Markdown("## 📥 Downloads")

    with gr.Row():
        download_txt = gr.File(label="TXT")

        download_pdf = gr.File(label="PDF")

        download_docx = gr.File(label="DOCX")

    generate_btn.click(
        fn=process_meeting,
        inputs=[audio_input, language, output_style],
        outputs=[
            transcript_output,
            meeting_minutes_output,
            download_txt,
            download_pdf,
            download_docx,
        ],
    )

    gr.Markdown("""
---
Built using **Whisper**, **Llama**, and **Gradio**
""")


if __name__ == "__main__":
    demo.queue()
    demo.launch()
