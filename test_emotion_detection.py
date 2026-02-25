"""Unit tests for EmotionDetection."""
from EmotionDetection import emotion_detector

def test_emotions():
    """Tests dominant emotions for given statements."""
    assert emotion_detector("I am glad this happened")["dominant_emotion"] == "joy"
    assert emotion_detector("I am really mad about this")["dominant_emotion"] == "anger"
    assert emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"] == "disgust"
    assert emotion_detector("I am so sad about this")["dominant_emotion"] == "sadness"
    assert emotion_detector("I am really afraid that this will happen")["dominant_emotion"] == "fear"

if __name__ == "__main__":
    test_emotions()
    print("All tests passed!")