from kubernetes import client, config
from kubernetes.client.rest import ApiException
import time

def create_musicplayer_object(name, songs):
    return {
        "apiVersion": "example.com/v1",
        "kind": "MusicPlayer",
        "metadata": {"name": name},
        "spec": {"songs": songs},
    }

def create_musicplayer(api_instance, name, songs):
    body = create_musicplayer_object(name, songs)
    try:
        api_instance.create_namespaced_custom_object(
            "example.com", "v1", "default", "musicplayers", body
        )
        print("MusicPlayer created.")
    except ApiException as e:
        print(f"Exception when calling CustomObjectsApi->create_namespaced_custom_object: {e}")

def main():
    config.load_kube_config()
    api_instance = client.CustomObjectsApi()

    create_musicplayer(api_instance, "example-musicplayer", [{"name": "Song1", "url": "http://example.com/song1.mp3", "imageUrl": "http://example.com/song1.jpg"}])

if __name__ == "__main__":
    main()
