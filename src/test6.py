"""
DO NOT EDIT THIS FILE!!!
"""
import unittest
import tensorflow as tf
PATH_TO_MODEL = 'models/model_6'


class TestAccuracyDemo(unittest.TestCase):
    def testCategoricalAccuracy(self):
        m = tf.keras.metrics.CategoricalAccuracy()
        y_true = tf.convert_to_tensor([[0, 0, 1], [0, 1, 0]])
        y_pred = tf.convert_to_tensor([[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
        m.update_state(y_true, y_pred)
        res = m.result().numpy()
        self.assertEqual(res, 0.5)


class TestModelLocal(unittest.TestCase):
    def test_model(self):
        model = tf.keras.models.load_model(PATH_TO_MODEL)
        X = tf.ones((1, 180, 180, 3))
        y = model(X)
        self.assertIsInstance(y, tf.Tensor)


if __name__ == '__main__':
    unittest.main()
