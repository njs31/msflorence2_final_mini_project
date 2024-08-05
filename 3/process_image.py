from gradio_client import Client, handle_file

client = Client("gokaygokay/Florence-2")

# List of image URLs
image_urls = [
    'bathing.jpg',
    'brushing.jpg',
    'coffedrinking.jpg',
    'eating.jpg',
    'playingpool.jpg',
    'sleeping.jpg',
    'traveelingincycle.jpg',
    'travellingback.jpg',
    'watchingtv.jpg',
    'working.jpg'
]

task_prompt = "Caption"  
model_id = "microsoft/Florence-2-large"

# Initialize an array to store the output captions
captions = []

# Loop through the image URLs and get predictions
for image_url in image_urls:
    result = client.predict( 
        image=handle_file(image_url),  # URL pointing to an image
        task_prompt=task_prompt,       # Task prompt for the model
        text_input=None,               # No additional text information
        model_id=model_id,             # Identifier for the specific model
        api_name="/process_image"      # API endpoint for processing the image
    )
    
    output_text, output_image_filepath = result
    
    # Extract the caption and append it to the captions array
    if output_image_filepath is not None:
        captions.append(f"Output for {image_url}:\nText: {output_text}\nImage Path: {output_image_filepath}\n")
    else:
        captions.append(f"Output for {image_url}:\nText: {output_text}\n")

# Write the captions to output.txt
with open('output.txt', 'w') as f:
    for caption in captions:
        f.write(caption + "\n")