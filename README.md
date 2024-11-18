Image Service Generator Microservice


Overview
This microservice is designed to generate images based on the parameters provided by the user. It supports three key operations:
⦁	Random Image Generation
⦁	Specific Image Generation
⦁	Adjusting Image Centering
The microservice communicates through a REST API.

Communication Contract

The microservice uses HTTP GET requests to perform the following operations:
⦁	GET /generate_random_image: Returns a random image.
⦁	GET /generate_specific_image: Returns a specific image based on the parameters provided (e.g., album name, image format, resolution).
⦁	GET /adjust_image_center: Returns an image with the specified centering adjustments.

Requesting Data from the Microservice

General Instructions:
To request data from the image service, you can use HTTP GET requests with the necessary query parameters. The microservice will respond with the requested image in binary format (e.g., PNG or JPEG).
Example Call for Requesting Data
You can use the Python requests library to make a call to the microservice. Below is an example of how to request a random image:
import requests

# Define the base URL of the microservice
BASE_URL = "http://127.0.0.1:5000"

# Request a random image
response = requests.get(f"{BASE_URL}/generate_random_image", params={
    "format": "PNG",           # Specify the format (e.g., PNG, JPEG)
    "resolution": "200",       # Specify resolution (width x height)
    "position_x": "10",        # Horizontal axis for centering (in pixels or percentage)
    "position_y": "20"         # Vertical axis for centering (in pixels or percentage)
})

# Save the response image to a file
with open("random_image.png", "wb") as f:
    f.write(response.content)

print("Random image saved as 'random_image.png'")

Request Parameters:
⦁	action: Specifies whether the image generation will be "random" or "specific".
⦁	format: Specifies the format of the image (e.g., "PNG", "JPEG").
⦁	resolution: Specifies the resolution of the image (e.g., "1024x768").
⦁	position_x: Specifies the horizontal position of the image in the frame.
⦁	position_y: Specifies the vertical position of the image in the frame.
Example Call for Specific Image Generation:
To request a specific image (e.g., album cover for "Sample Album"):
response = requests.get(f"{BASE_URL}/generate_specific_image", params={
    "album": "Sample Album",    # Specify the album or other specific data
    "format": "PNG",            # Specify the format
    "resolution": "1024x768",   # Specify the resolution
    "position_x": "50",         # Horizontal position
    "position_y": "50"          # Vertical position
})

# Save the response image to a file
with open("specific_image.png", "wb") as f:
    f.write(response.content)

print("Specific image saved as 'specific_image.png'")

Receiving Data from the Microservice
General Instructions:
Once a request is made to the microservice, it will return the image data as binary content. You can handle this content and save it to a file for display or use in your application.
Example Call for Receiving Data
The response.content will contain the binary data of the image. You can write this content to a file as shown in the above examples, or use it in your application for further processing.
Example Response Data:
The microservice will return an image in binary format. If your request was successful, you will receive image data in the response. If the request fails, the response will include an error message with the appropriate status code.For example, the following Python code receives the image data and writes it to a file:
# Assuming `response` is the result of the GET request to the image service
if response.status_code == 200:
    with open("received_image.png", "wb") as f:
        f.write(response.content)
    print("Image received successfully and saved.")
else:
    print(f"Error: Unable to fetch image. Status Code: {response.status_code}")

Expected Response:
⦁	Status Code: 200 (OK) if the request is successful.
⦁	Content: Binary data of the image in the requested format (e.g., PNG or JPEG).
UML Sequence Diagram
Below is a detailed UML sequence diagram illustrating how the data is requested and received from the microservice.
 

Sequence Description:
1. Client Program Initiates Request
The sequence begins with the Client Program initiating an HTTP GET request to generate a random image.
The request includes parameters like image format, resolution, and centering positions (position_x and position_y).
2. Write Request to CommPipe.txt
Upon receiving the request, the Client Program writes the request details to the CommPipe.txt file.
This file acts as a communication medium between the Client Program and the Image Service Microservice.
3. Read Request from CommPipe.txt
The Image Service Microservice reads the request details from the CommPipe.txt file.
It processes the request to understand the required image generation specifications.
4. Process Request (Generate Image)
The Image Service Microservice processes the request parameters and generates the image accordingly.
Depending on the request type, it may generate a random image, a specific image based on provided data (e.g., album name), or adjust the image centering.
5. Image Generation
Once the processing is complete, the Image Service Microservice generates the image.
The generated image is temporarily stored to facilitate the next step of communication.
6. Write Image to CommPipe.txt
The Image Service Microservice writes the generated image data (in binary format) back to the CommPipe.txt file.
This step ensures that the image data is available for retrieval by the Client Program.
7. Receive Image by Client Program
The Client Program reads the image data from the CommPipe.txt file.
This marks the completion of the data retrieval process.
8. Save or Display Image
The Client Program saves the received image data to a file for display or further use.
For example, the image may be saved as random_image.png or specific_image.png, depending on the request type.
Communication Pipe
The microservice uses a REST API to communicate, ensuring that other programs can make requests via HTTP to interact with it. All responses from the microservice are returned as binary image data.
