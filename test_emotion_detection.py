""" My testing application """

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_happy_text(self):
        """Test joy"""
        result = emotion_detector("I'm happy!")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertGreater(result['joy'], 0.5)
    def test_sad_text(self):
        """Test sad"""
        result = emotion_detector("I feel very sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertGreater(result['sadness'], 0.3)
    def test_angry_text(self):
        """Test angry"""
        result = emotion_detector("I'm furious")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertGreater(result['anger'], 0.3)
    def test_fear_text(self):
        """Test fear"""
        result = emotion_detector("I'm scared")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertGreater(result['fear'], 0.3)
    def test_disgust_text(self):
        """Test disgust"""
        result = emotion_detector("That is disgusting")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertGreater(result['disgust'], 0.3)

if __name__ == '__main__':
    unittest.main()