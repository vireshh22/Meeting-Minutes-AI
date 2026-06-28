import gradio as gr

from services.transcription import transcribe_audio
from services.llm import generate_meeting_minutes
from services.export import (
    export_to_txt,
    export_to_pdf,
    export_to_docx,
)


def process_meeting(
    audio_path: str,
    language: str,
    output_style: str,
    progress=gr.Progress(),
):
    if audio_path is None:
        raise gr.Error("Please upload an audio file before generating meeting minutes.")

    progress(0.1, desc="Loading audio...")

    try:
        transcript = transcribe_audio(audio_path)
    except Exception as e:
        raise gr.Error(f"Failed to transcribe audio.\n\n{str(e)}")

    if not transcript.strip():
        raise gr.Error("No speech was detected in the uploaded audio.")

    progress(0.6, desc="Generating meeting minutes...")

    try:
        meeting_minutes = generate_meeting_minutes(
            transcript,
            language,
            output_style,
        )
    except Exception as e:
        raise gr.Error(f"Failed to generate meeting minutes.\n\n{str(e)}")

    progress(0.9, desc="Preparing download...")

    try:
        txt_file = export_to_txt(meeting_minutes)
        pdf_file = export_to_pdf(meeting_minutes)
        docx_file = export_to_docx(meeting_minutes)
    except Exception as e:
        raise gr.Error(f"Failed to export meeting minutes.\n\n{str(e)}")

    progress(1.0, desc="Completed!")

    return (
        transcript,
        meeting_minutes,
        txt_file,
        pdf_file,
        docx_file,
    )
