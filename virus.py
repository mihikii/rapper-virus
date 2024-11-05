import os
import random
import requests
import string

directory = os.path.expanduser('~\\Pictures')

image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

image_urls = [
    'https://files.catbox.moe/18u4rl.jpg',
    'https://files.catbox.moe/kpz5m0.jpg',
    'https://files.catbox.moe/e2mldz.jpg',
    'https://files.catbox.moe/5j522o.jpg',
    'https://files.catbox.moe/tw4kb6.jpg',
    'https://files.catbox.moe/h8407m.jpg',
    'https://files.catbox.moe/84gbhh.jpg',
]

existing_images = [filename for filename in os.listdir(directory) if filename.lower().endswith(image_extensions)]
num_existing_images = len(existing_images)

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

for filename in existing_images:
    file_path = os.path.join(directory, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            print(f'Deleted: {file_path}')
    except Exception as e:
        print(f'Failed to delete {file_path}. Reason: {e}')

for i in range(num_existing_images):
    url = image_urls[i % len(image_urls)]
    try:
        response = requests.get(url)
        response.raise_for_status()

        filename = url.split('/')[-1]
        name, ext = os.path.splitext(filename)
        random_filename = f"{name}_{generate_random_string()}{ext}"
        file_path = os.path.join(directory, random_filename)

        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {file_path}')
        
    except Exception as e:
        print(f'Failed to download {url}. Reason: {e}')
