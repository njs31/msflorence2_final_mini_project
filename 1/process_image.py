from gradio_client import Client, handle_file

client = Client("gokaygokay/Florence-2")
result = client.predict(
    image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
    task_prompt="Caption",
    text_input=None,
    model_id="microsoft/Florence-2-large",
    api_name="/process_image"
)
print(result)