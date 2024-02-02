from credentials import ig_username,ig_password
from instagrapi import Client, exceptions
from PIL import Image
import pandas as pd
import requests
import io
import os

class Post:
    def __init__(self, post_id, caption, comments, image_data):
        self.post_id = post_id
        self.caption = caption
        self.comments = comments
        self.image_data = image_data

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'caption': self.caption,
            'comments': self.comments,
            'image_data': self.image_data
        }

hash_tag ='harcèlement'

cl = Client()
try:
    cl.login(ig_username, ig_password)
except exceptions.ClientError as e:
    print("Error logging in:", e)
    exit()

try:
    posts = cl.hashtag_medias_recent(hash_tag, 100)
except exceptions.ClientError as e:
    print("Error fetching posts:", e)
    posts = []

print(f"Number of posts scraped for #{hash_tag}: {len(posts)}")

csv_file_path = 'posts_data.csv'

try:
    # Créer une liste de dictionnaires pour stocker les données des posts
    posts_data = []
    for post in posts:
        try:
            response = requests.get(post.thumbnail_url, stream=True)
            response.raise_for_status()  # Raise an exception for non-200 status codes

            filename = f"image_{post.pk}.jpg"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            post_data = {
                'post_id': post.pk,
                'caption': post.caption_text,
                'comments': [comment.text for comment in cl.media_comments(post.pk)],
                'image_data': None
            }

            # Handle image storage in pandas DataFrame
            im = Image.open(filename)
            image_bytes = io.BytesIO()
            im.save(image_bytes, format='JPEG')
            post_data['image_data'] = image_bytes.getvalue()

            posts_data.append(post_data)
            os.remove(filename)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image {post.pk}: {e}")

    # Créer un DataFrame à partir des données des posts
    df = pd.DataFrame(posts_data)

    # Enregistrer le DataFrame dans un fichier CSV
    df.to_csv(csv_file_path, index=False, encoding='utf-8')

    print(f"Data saved to {csv_file_path}")
except Exception as e:
    print("Error saving data to CSV:", e)