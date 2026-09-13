import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy_result = emotion_detector("I am glad this happened")
        self.assertEqual("joy", joy_result['dominant_emotion'])

        anger_result = emotion_detector("I am really mad about this")
        self.assertEqual("anger", anger_result['dominant_emotion'])

        disgust_result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual("disgust", disgust_result['dominant_emotion'])

        sad_result = emotion_detector("I am so sad about this")
        self.assertEqual("sadness", sad_result['dominant_emotion'])

        fear_result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual("fear", fear_result['dominant_emotion'])

unittest.main()