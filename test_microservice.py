import requests

BASE_URL = "http://127.0.0.1:5000"

def test_random_image():
    response = requests.get(f"{BASE_URL}/generate_random_image", params={"format": "PNG", "resolution": "200", "position_x": "10", "position_y": "20"})
    with open("random_image.png", "wb") as f:
        f.write(response.content)
    print("Random image saved as 'random_image.png'")

def test_specific_image(album):
    response = requests.get(f"{BASE_URL}/generate_specific_image", params={"album": album, "format": "PNG", "resolution": "200", "position_x": "10", "position_y": "20"})
    with open("specific_image.png", "wb") as f:
        f.write(response.content)
    print("Specific image saved as 'specific_image.png'")

def test_adjust_image_center():
    response = requests.get(f"{BASE_URL}/adjust_image_center", params={"format": "PNG", "resolution": "200", "position_x": "50", "position_y": "50"})
    with open("centered_image.png", "wb") as f:
        f.write(response.content)
    print("Centered image saved as 'centered_image.png'")

# Run test cases
test_random_image()
test_specific_image("Sample Album")
test_adjust_image_center()
