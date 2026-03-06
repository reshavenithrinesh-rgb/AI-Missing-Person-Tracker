import PIL
import numpy as np
import streamlit as st
import mediapipe as mp


def image_obj_to_numpy(image_obj) -> np.ndarray:
    """Convert a Streamlit-uploaded image object to a numpy array."""
    image = PIL.Image.open(image_obj)
    return np.array(image)


def extract_face_mesh_landmarks(image: np.ndarray):
    """
    Extract face mesh landmarks from an image using MediaPipe.
    Returns a flattened list of all (x, y, z) landmarks if a face is found, else None.
    """
    return None
