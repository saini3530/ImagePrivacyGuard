from PIL import Image
from PIL.ExifTags import TAGS
import io

img = Image.new('RGB', (800, 600), color='blue')

exif_dict = {
    'Make': 'Canon',
    'Model': 'EOS 5D Mark IV',
    'DateTime': '2024:01:15 14:30:00',
    'Artist': 'John Doe',
    'Copyright': 'Copyright 2024 John Doe',
    'Software': 'Adobe Photoshop CC 2024',
}

exif_data = img.getexif()
for tag_name, value in exif_dict.items():
    tag_id = None
    for id, tag in TAGS.items():
        if tag == tag_name:
            tag_id = id
            break
    if tag_id:
        exif_data[tag_id] = value

img.save('test_image.jpg', 'JPEG', exif=exif_data, quality=95)
print("Image created successfully")
